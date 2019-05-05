import logging
import random
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core import serializers

from .models import DummyActivatableOrderableModel, DummyActivatableModel

logger = logging.getLogger(__name__)
User = get_user_model()


# class UserGeneratorTest(TestCase):
#     def setUp(self):
#         self.possible_first_names = ["Pedro", "Diogo", "Inês", "Marta"]
#         self.possible_first_names_length = len(self.possible_first_names)
#         self.possible_last_names = ["Freitas", "Mendes", "Gouveia", "Abreu"]
#         self.possible_last_names_length = len(self.possible_first_names)
#         self.id = 1

#     def create_random_user(self):
#         user = User()
#         user.first_name = self.possible_first_names[random.randint(
#             0, self.possible_first_names_length - 1)]
#         user.last_name = self.possible_last_names[random.randint(
#             0, self.possible_last_names_length - 1)]
#         user.email = "{}_{}_{}@gmail.com".format(
#             user.first_name, user.last_name, self.id)
#         user.username = user.first_name + user.last_name + str(self.id)
#         user.set_password("Não importa")
#         user.save()
#         self.id += 1
#         return user

# Create your tests here.


class ActivatableTestModel(TestCase):
    def setUp(self):
        self.non_initialize = DummyActivatableModel()
        self.inactive = DummyActivatableModel(active=False)
        self.active = DummyActivatableModel(active=True)
        self.log_equals_format = "{} = {}"
        self.log_not_equals_format = "{} != {}"

    def test_Activatable_model(self):
        self.non_initialize.save()
        self.inactive.save()
        self.active.save()

        logger.info(self.log_equals_format.format(
            self.non_initialize.active, True))
        self.assertEqual(self.non_initialize.active, True)

        logger.info(self.log_equals_format.format(self.inactive.active, False))
        self.assertEqual(self.inactive.active, False)

        logger.info(self.log_equals_format.format(self.active.active, True))
        self.assertEqual(self.active.active, True)

        logger.info(self.log_not_equals_format.format(
            self.active.active_at, None))
        self.assertNotEqual(self.active.active_at, None)

        # Now will change

        self.active.active = False
        self.active.save()

        logger.info(self.log_equals_format.format(self.active.active, False))
        self.assertEqual(self.active.active, False)

        logger.info(self.log_not_equals_format.format(
            self.active.inactive_at, None))
        self.assertNotEqual(self.active.inactive_at, None)

        self.inactive.active = True
        self.inactive.save()

        logger.info(self.log_equals_format.format(self.inactive.active, True))
        self.assertEqual(self.inactive.active, True)

        logger.info(self.log_not_equals_format.format(
            self.inactive.active_at, None))
        self.assertNotEqual(self.inactive.active_at, None)


class ActivatableOrderableTestModel(TestCase):
    def setUp(self):
        self.non_initialize = DummyActivatableOrderableModel()
        self.inactive = DummyActivatableOrderableModel(active=False)
        self.active = DummyActivatableOrderableModel(active=True)
        self.log_equals_format = "{} = {}"
        self.log_not_equals_format = "{} != {}"

    def test_Activatable_model(self):
        self.non_initialize.save()
        logger.info(self.log_equals_format.format(
            self.non_initialize.sort_order, 1))
        self.assertEqual(self.non_initialize.sort_order, 1)

        self.inactive.save()
        logger.info(self.log_equals_format.format(
            self.inactive.sort_order, 2))
        self.assertEqual(self.inactive.sort_order, 2)

        self.active.save()
        logger.info(self.log_equals_format.format(self.active.sort_order, 3))
        self.assertEqual(self.active.sort_order, 3)

        logger.info(self.log_equals_format.format(
            self.non_initialize.active, True))
        self.assertEqual(self.non_initialize.active, True)

        logger.info(self.log_equals_format.format(self.inactive.active, False))
        self.assertEqual(self.inactive.active, False)

        logger.info(self.log_equals_format.format(self.active.active, True))
        self.assertEqual(self.active.active, True)

        logger.info(self.log_not_equals_format.format(
            self.active.active_at, None))
        self.assertNotEqual(self.active.active_at, None)

        # Now will change

        self.active.active = False
        self.active.save()

        logger.info(self.log_equals_format.format(self.active.active, False))
        self.assertEqual(self.active.active, False)

        logger.info(self.log_not_equals_format.format(
            self.active.inactive_at, None))
        self.assertNotEqual(self.active.inactive_at, None)

        self.inactive.active = True
        self.inactive.save()

        logger.info(self.log_equals_format.format(self.inactive.active, True))
        self.assertEqual(self.inactive.active, True)

        logger.info(self.log_not_equals_format.format(
            self.inactive.active_at, None))
        self.assertNotEqual(self.inactive.active_at, None)

        self.active.sort_order = 1
        self.active.save()

        self.non_initialize.refresh_from_db()
        self.inactive.refresh_from_db()
        self.active.refresh_from_db()

        logger.info(self.log_equals_format.format(
            self.non_initialize.sort_order, 2))
        self.assertEqual(self.non_initialize.sort_order, 2)

        logger.info(self.log_equals_format.format(
            self.inactive.sort_order, 3))
        self.assertEqual(self.inactive.sort_order, 3)

        logger.info(self.log_equals_format.format(self.active.sort_order, 1))
        self.assertEqual(self.active.sort_order, 1)
