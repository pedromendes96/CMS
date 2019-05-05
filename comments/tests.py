import random

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.test import TestCase
from wagtail.core.models import Page

from .models import Client, ProfessionalCommentator, Reporter, Comment, NormalComment

User = get_user_model()


# Create your tests here.
class CommentsTest(TestCase):
    def setUp(self):
        self.possible_first_names = ["Pedro", "Diogo", "Inês", "Marta"]
        self.possible_first_names_length = len(self.possible_first_names)
        self.possible_last_names = ["Freitas", "Mendes", "Gouveia", "Abreu"]
        self.possible_last_names_length = len(self.possible_first_names)
        self.id = 1
        self.initial_comments = []
        self.reporter = self.create_reporter(self.create_random_user())
        self.special_commentator = self.create_commentator(
            self.create_random_user())
        self.client = self.create_client(self.create_random_user())
        self.page = Page.objects.all().first()

    def create_client(self, user):
        client = Client(user=user)
        client.save()
        return client

    def create_commentator(self, user):
        commentator = ProfessionalCommentator()
        commentator.user = user
        commentator.company = "TestingCompany"
        commentator.profession = "Tester"
        commentator.save()
        return commentator

    def create_reporter(self, user):
        reporter = Reporter(user=user)
        reporter.department = "Editorial"
        reporter.save()
        return reporter

    def create_random_user(self):
        user = User()
        user.first_name = self.possible_first_names[random.randint(
            0, self.possible_first_names_length - 1)]
        user.last_name = self.possible_last_names[random.randint(
            0, self.possible_last_names_length - 1)]
        user.email = "{}_{}_{}@gmail.com".format(
            user.first_name, user.last_name, self.id)
        user.username = user.first_name + user.last_name + str(self.id)
        user.set_password("Não importa")
        user.save()
        self.id += 1
        return user

    def test_comments_example(self):
        first_comment = Comment.create(
            self.page, self.client, "Isto é tudo mentira!!!")
        first_comment.status.to_evaluation()
        first_comment.status.accept()

        first_answer_first_comment = first_comment.answer(
            "Não é não!!!!", self.reporter)
        first_answer_first_comment.status.accept()

        second_answer_first_comment = first_comment.answer("O meu amigo reporter tem razão!!!!",
                                                           self.special_commentator)
        second_answer_first_comment.status.accept()

        answer_of_the_first_answer_first_comment = first_answer_first_comment.answer(
            "Tenho provas!!!!!!!!!!!!", self.reporter)
        answer_of_the_first_answer_first_comment.status.accept()

        answer_of_the_second_answer_first_comment = second_answer_first_comment.answer(
            "Ora tu não defenderes os da tua laia!!!", self.client)
        answer_of_the_second_answer_first_comment.status.accept()

        # number of initial topic comments
        self.assertEqual(Comment.objects.filter(origin=None).count(), 1)

        # number of direct answers
        self.assertEqual(first_comment.get_active_children().count(), 2)

        # number of total of active answers
        self.assertEqual(Comment.objects.all().count(), 5)

        first_comment.inactivate()

        self.assertEqual(Comment.objects.filter(
            status__active=True).count(), 0)

        first_comment.activate()

        self.assertEqual(Comment.objects.filter(
            status__active=True).count(), 5)

        first_comment.mark_as_spam(self.reporter.user)

        self.assertEqual(NormalComment.objects.filter(is_spam=True).count(), 1)
        self.assertEqual(NormalComment.objects.filter(
            ~Q(marked_as_spam_at=None)).count(), 1)
        self.assertEqual(Comment.objects.filter(
            status__active=False).count(), 5)
