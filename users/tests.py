from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import NewsletterAuthor, Reporter, OpinionArticleAuthor, ProfessionalCommentator, UsersFollowingAuthors
import random

User = get_user_model()
# Create your tests here.


class UsersTest(TestCase):
    def setUp(self):
        self.possible_first_names = ["Pedro", "Diogo", "Inês", "Marta"]
        self.possible_first_names_length = len(self.possible_first_names)
        self.possible_last_names = ["Freitas", "Mendes", "Gouveia", "Abreu"]
        self.possible_last_names_length = len(self.possible_first_names)
        self.id = 1

        self.user = self.create_random_user()
        self.newsletter_author = self.create_newsletter_author(
            self.create_random_user())
        self.reporter = self.create_reporter(self.create_random_user())
        self.opinion_article_user = self.create_opinion_article_user(
            self.create_random_user())
        self.professional_commentator = self.create_professional_commentator(
            self.create_random_user())

    def test_users(self):
        self.newsletter_author.follow(self.user)
        self.reporter.follow(self.user)
        self.opinion_article_user.follow(self.user)
        self.professional_commentator.follow(self.user)

        self.assertEqual(UsersFollowingAuthors.objects.filter(
            active=True).count(), 4)

        self.newsletter_author.unfollow(self.user)

        self.assertEqual(UsersFollowingAuthors.objects.filter(
            active=True).count(), 3)

        self.assertEqual(UsersFollowingAuthors.objects.all().count(), 4)

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

    def create_newsletter_author(self, user):
        instance = NewsletterAuthor()
        instance.description = "ADSDASDASadsdsads"
        instance.img = "media/img.png"
        instance.user = user
        instance.save()
        return instance

    def create_reporter(self, user):
        reporter = Reporter(user=user)
        reporter.department = "Editorial"
        reporter.save()
        return reporter

    def create_opinion_article_user(self, user):
        opinion_author = OpinionArticleAuthor(user=user)
        opinion_author.company = "DNOTICIAS"
        opinion_author.profession = "DIRETOR"
        opinion_author.save()
        return opinion_author

    def create_professional_commentator(self, user):
        commentator = ProfessionalCommentator(user=user)
        commentator.company = "DNOTICIAS"
        commentator.profession = "DIRETOR"
        commentator.save()
        return commentator
