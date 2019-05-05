from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from polymorphic.models import PolymorphicModel
from simple_history.models import HistoricalRecords

from utils.models import ActivatableModel

User = get_user_model()


# Create your models here.

class Author(PolymorphicModel, ActivatableModel):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), null=False, blank=False, on_delete=models.CASCADE, related_name="author_user", related_query_name="author")
    history = HistoricalRecords(inherit=True)
    followers = models.ManyToManyField(User, through="UsersFollowingAuthors")

    def follow(self, user):
        users_following_authors = UsersFollowingAuthors.objects.filter(
            user=user, author=self)
        if users_following_authors.count() == 0:
            instance = UsersFollowingAuthors.objects.create(
                user=user, author=self)
        else:
            instance = users_following_authors.first()
            instance.active = True
            instance.save(update_fields=["active"])

    def unfollow(self, user):
        users_following_authors = UsersFollowingAuthors.objects.filter(
            user=user, author=self)
        if users_following_authors.count() > 0:
            instance = users_following_authors.first()
            instance.active = False
            instance.save(update_fields=["active"])


class UsersFollowingAuthors(ActivatableModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class NewsletterAuthor(Author):
    description = models.TextField(verbose_name=_(
        "Description"), null=False, blank=False)
    img = models.ImageField(verbose_name=_("Image"), null=False, blank=False)


class OpinionArticleAuthor(Author):
    company = models.CharField(verbose_name=_(
        "Company"), null=False, blank=False, max_length=32)
    profession = models.CharField(verbose_name=_(
        "Profession"), null=False, blank=False, max_length=32)


class Reporter(Author):
    department = models.CharField(verbose_name=_(
        "Department"), null=False, blank=False, max_length=32)


class ProfessionalCommentator(Author):
    company = models.CharField(verbose_name=_(
        "Company"), null=False, blank=False, max_length=32)
    profession = models.CharField(verbose_name=_(
        "Profession"), null=False, blank=False, max_length=32)


class Client(ActivatableModel):
    user = models.ForeignKey(User, verbose_name=_(
        "User"), null=False, blank=False, on_delete=models.CASCADE, related_query_name="client")
    is_spammer = models.BooleanField(verbose_name=_(
        "Is a spammer"), null=False, blank=False, default=False)
    marked_as_spam_at = models.DateTimeField(
        verbose_name=_("Marked as spam at"), null=True, blank=True)
    history = HistoricalRecords()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pre_is_spammer = self.is_spammer

    def mark_as_spammer(self):
        self.is_spammer = True
        self.save(update_fields=["is_spammer"])

    def save(self, *args, **kwargs):
        if self.pk:
            if self.pre_is_spammer != self.is_spammer and self.is_spammer:
                self.marked_as_spam_at = timezone.now()
        super().save(*args, **kwargs)
        self.pre_is_spammer = self.is_spammer
