from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Newsletter, Template, NewsletterMessage, NewsletterSubscription, NewsletterMessageUser
from users.models import NewsletterAuthor

import random

User = get_user_model()

# Create your tests here.


class TestNewsletter(TestCase):
    def setUp(self):
        self.users = []

        self.possible_first_names = ["Pedro", "Diogo", "Inês", "Marta"]
        self.possible_first_names_length = len(self.possible_first_names)
        self.possible_last_names = ["Freitas", "Mendes", "Gouveia", "Abreu"]
        self.possible_last_names_length = len(self.possible_first_names)
        self.id = 1

        for i in range(random.randint(5, 10)):
            self.users.append(self.create_random_user())

        self.author = self.create_newsletter_author(
            self.create_random_user())

        self.newsletter = self.create_example_newsletter()
        self.page = self.get_template_page()
        self.newsletter_message = self.create_newsletter_message()

    def create_example_newsletter(self):
        instance = Newsletter()
        instance.title = "Extra"
        instance.frequency = Newsletter.DAILY
        instance.description = "Informação extra do dia bla bla bla bla"
        instance.save()
        return instance

    def get_template_page(self):
        return None

    def create_newsletter_message(self):
        instance = NewsletterMessage()
        instance.author = self.author
        instance.newsletter = self.newsletter
        instance.template = self.page
        instance.save()
        return instance

    def create_newsletter_author(self, user):
        instance = NewsletterAuthor()
        instance.description = "ADSDASDASadsdsads"
        instance.img = "media/img.png"
        instance.user = user
        instance.save()
        return instance

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

    def test_newsletter(self):
        for user in self.users:
            self.newsletter.subscribe(user)

        self.assertEqual(NewsletterSubscription.objects.filter(
            newsletter=self.newsletter, active=True).count(), len(self.users))

        self.newsletter_message.send_to_subscribers()

        self.assertEqual(
            NewsletterMessageUser.objects.all().count(), len(self.users))
