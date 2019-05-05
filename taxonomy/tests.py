from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category, Section, UsersFollowingSection

import random

User = get_user_model()

# Create your tests here.


class TestTaxonomy(TestCase):
    def setUp(self):
        self.user = self.create_random_user()

        self.section = self.create_section("sport")

        # 1º nodes
        self.regional = self.create_category("regional")
        self.national = self.create_category("national")
        self.international = self.create_category("international")

        self.volleyball_for_regional = self.create_category("volleyball")
        self.volleyball_for_national = self.create_category("volleyball")
        self.volleyball_for_international = self.create_category("volleyball")

        self.soccer_for_regional = self.create_category("soccer")

    def create_section(self, name):
        instance = Section()
        instance.name = name
        instance.hex_color = "#FFFFFF"
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

    def create_category(self, name):
        category = Category(
            name=name, description="Category - {}".format(name))
        category.save()
        category.tags.add(name)
        return category

    def test_categories_mechanism(self):
        self.assertEqual(Section.get_active_sections().count(), 1)

        self.section.add_category(self.regional)
        self.section.add_category(self.national)
        self.section.add_category(self.international)

        self.assertEqual(self.section.get_active_main_categories().count(), 3)

        self.regional.add_child(self.volleyball_for_regional)
        self.national.add_child(self.volleyball_for_national)
        self.international.add_child(self.volleyball_for_international)

        self.assertEqual(self.regional.get_active_children().count(), 1)
        self.assertEqual(self.national.get_active_children().count(), 1)
        self.assertEqual(self.international.get_active_children().count(), 1)

        self.regional.add_child(self.soccer_for_regional)
        self.assertEqual(self.regional.get_active_children().count(), 2)

        self.assertEqual(UsersFollowingSection.objects.filter(
            user=self.user, section=self.section).count(), 0)
        self.section.follow(self.user)
        self.assertEqual(UsersFollowingSection.objects.filter(
            user=self.user, section=self.section, active=True).count(), 1)
        self.section.unfollow(self.user)
        self.assertEqual(UsersFollowingSection.objects.filter(
            user=self.user, section=self.section, active=False).count(), 1)
