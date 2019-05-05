import logging
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel
from wagtail.core.models import Page
from users.models import ProfessionalCommentator, Client, Reporter
from utils.models import ActivatableOrderableModel

User = get_user_model()


logger = logging.getLogger("comments")


class CommentStatusFactory(object):
    @staticmethod
    def create(comment_status):
        if comment_status.status == CommentStatus.PENDING:
            return PendingCommentState(comment_status)
        elif comment_status.status == CommentStatus.DRAFT:
            return DraftCommentState(comment_status)
        elif comment_status.status == CommentStatus.ACCEPTED:
            return AcceptedCommentState(comment_status)
        elif comment_status.status == CommentStatus.REFUSED:
            return RefusedCommentState(comment_status)


class CommentState(object):
    def __init__(self, comment_status, *args, **kwargs):
        self.comment_status = comment_status

    def to_edit(self):
        pass

    def to_evaluation(self):
        pass

    def accept(self):
        pass

    def refuse(self):
        pass


class DraftCommentState(CommentState):
    def __init__(self, comment_status, *args, **kwargs):
        super().__init__(comment_status, *args, **kwargs)

    def to_edit(self):
        logger.info("Already it is in a editable state")

    def to_evaluation(self):
        logger.info("Transiting from draft state to pending state")
        self.comment_status.status = CommentStatus.PENDING
        self.comment_status.save(update_fields=["status"])

    def accept(self):
        logger.info("To be accepted, first he must transit to pending state")

    def refuse(self):
        logger.info("To be refused, first he must transit to pending state")


class PendingCommentState(CommentState):
    def __init__(self, comment_status, *args, **kwargs):
        super().__init__(comment_status, *args, **kwargs)

    def to_edit(self):
        logger.info("Transiting from pending state to draft state")
        self.comment_status.status = CommentStatus.DRAFT
        self.comment_status.save(update_fields=["status"])

    def to_evaluation(self):
        logger.info("Already is in pending state")

    def accept(self):
        logger.info("Transiting from pending state to accepted state")
        self.comment_status.status = CommentStatus.ACCEPTED
        self.comment_status.active = True
        self.comment_status.save(update_fields=["status", "active"])

    def refuse(self):
        logger.info("Transiting from pending state to refused state")
        self.comment_status.status = CommentStatus.REFUSED
        self.comment_status.active = False
        self.comment_status.save(update_fields=["status", "active"])


class RefusedCommentState(CommentState):
    def __init__(self, status, *args, **kwargs):
        super().__init__(status, *args, **kwargs)

    def to_edit(self):
        logger.info("It's not allowed transit from refused to editable")

    def to_evaluation(self):
        logger.info("It's not allowed transit from refused to pending")

    def accept(self):
        logger.info("It's not allowed transit from refused to accepted")

    def refuse(self):
        logger.info("Already it's in refused state")


class AcceptedCommentState(CommentState):
    def __init__(self, status, *args, **kwargs):
        super().__init__(status, *args, **kwargs)

    def to_edit(self):
        logger.info("It's not allowed transit from accepted to editable")

    def to_evaluation(self):
        logger.info("It's not allowed transit from accepted to pending")

    def accept(self):
        logger.info("Already it's in accepted state")

    def refuse(self):
        logger.info("It's not allowed transit from accepted to refused")


class CommentFactory(object):
    @staticmethod
    def create(user):
        if isinstance(user, ProfessionalCommentator):
            return ProfessionalComment(commentator=user)
        elif isinstance(user, Client):
            return NormalComment(client=user)
        elif isinstance(user, Reporter):
            return ReporterComment(reporter=user)
        raise Exception("doesn't have the correct correspondence")


class CommentStatus(ActivatableOrderableModel):
    PENDING = "1"
    DRAFT = "2"
    ACCEPTED = "3"
    REFUSED = "4"
    # status - pending, accepted, refused
    status = models.CharField(verbose_name=_("status"), choices=(
        (DRAFT, _("Draft")),
        (PENDING, _("Pending")),
        (ACCEPTED, _("Accepted")),
        (REFUSED, _("Refused"))
    ), null=False, blank=False, max_length=32, default=DRAFT)
    active = models.BooleanField(verbose_name=_(
        "Active"), null=False, blank=True, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = CommentStatusFactory.create(self)
        self.initialize_status()

    def initialize_status(self):
        try:
            self.pre_active = self.active
        except ObjectDoesNotExist:
            self.pre_active = False

    def to_edit(self):
        self.state.to_edit()

    def accept(self):
        self.state.accept()

    def to_evaluation(self):
        self.state.to_evaluation()

    def refuse(self):
        self.state.refuse()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.state = CommentStatusFactory.create(self)
        self.pre_active = self.active

    def on_activation(self):
        comments = self.comment.all()
        if comments.count() > 0:
            comment = comments.first()
            comment.recursive_enable()

    def on_desactivation(self):
        comments = self.comment.all()
        if comments.count() > 0:
            comment = comments.first()
            comment.recursive_disable()


class Comment(PolymorphicModel):
    content = models.TextField(verbose_name=_(
        "Content"), null=False, blank=False)
    origin = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="children",
                               related_query_name="children")
    page = models.ForeignKey(Page, null=False, blank=False, on_delete=models.CASCADE, related_name="comments",
                             related_query_name="comments")
    status = models.ForeignKey(CommentStatus, null=False, blank=False, verbose_name=_("Comment status"),
                               on_delete=models.CASCADE,
                               related_name="comment", related_query_name="comment")

    def __init__(self, *args, **kwargs):
        super(Comment, self).__init__(*args, **kwargs)

    def inactivate(self):
        self.status.active = False
        self.status.save()
        self.save()

    def activate(self):
        self.status.active = True
        self.status.save()
        self.save()

    @staticmethod
    def create(page, user, content):
        comment = CommentFactory.create(user)
        comment.content = content
        comment.origin = None
        comment.page = page

        status = CommentStatus()
        status.save()

        comment.status = status
        comment.save()
        return comment

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

    def get_active_children(self):
        return Comment.objects.filter(origin=self, status__active=True)

    def get_pending_children(self):
        return Comment.objects.filter(origin=self, status__active=False, is_spam=False)

    def recursive_disable(self):
        responses = Comment.objects.filter(origin=self)
        for response in responses:
            response.status.active = False
            response.status.save()
            response.recursive_disable()

    def recursive_enable(self):
        responses = Comment.objects.filter(origin=self)
        for response in responses:
            response.status.active = True
            response.status.save()
            response.recursive_enable()

    def answer(self, content, user, *args, **kwargs):
        comment = CommentFactory.create(user)
        comment.content = content
        comment.origin = self
        comment.page = self.page

        status = CommentStatus(status=CommentStatus.PENDING)
        status.save()

        comment.status = status
        comment.save()

        comment.save(*args, **kwargs)

        return comment


class ProfessionalComment(Comment):
    commentator = models.ForeignKey(ProfessionalCommentator, null=False, blank=False, on_delete=models.CASCADE,
                                    related_query_name="comments", related_name="comments")

    def __init__(self, *args, **kwargs):
        super(ProfessionalComment, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(ProfessionalComment, self).save(*args, **kwargs)


class NormalComment(Comment):
    client = models.ForeignKey(Client, null=False, blank=False, on_delete=models.CASCADE,
                               related_query_name="comments", related_name="comments")
    is_spam = models.BooleanField(verbose_name=_(
        "Is spam"), null=False, blank=False, default=False)
    marked_as_spam_at = models.DateTimeField(
        verbose_name=_("Marked as spam at"), null=True, blank=True)
    marked_as_spam_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,
                                          related_query_name="comments", related_name="comments")

    def __init__(self, *args, **kwargs):
        super(NormalComment, self).__init__(*args, **kwargs)
        self.initialize_spam()

    def initialize_spam(self):
        try:
            self.pre_spammed = self.is_spam
        except ObjectDoesNotExist:
            self.pre_spammed = False

    def mark_as_spam(self, user):
        self.is_spam = True
        self.save(user=user)

    def mark_as_not_spam(self):
        self.is_spam = False
        self.save()

    def save(self, *args, **kwargs):
        user = kwargs.pop("user") if "user" in kwargs else None
        if self.pre_spammed != self.is_spam and self.pk:
            if self.is_spam:
                if user is None:
                    raise Exception(
                        "Must have one user associated with the change!!!")
                self.marked_as_spam_at = timezone.now()
                self.marked_as_spam_by = user
                self.status.active = False
            else:
                self.status.active = True
            self.status.save()
        super(NormalComment, self).save(*args, **kwargs)
        self.pre_spammed = self.is_spam


class ReporterComment(Comment):
    reporter = models.ForeignKey(Reporter, null=False, blank=False, on_delete=models.CASCADE,
                                 related_query_name="comments", related_name="comments")

    def __init__(self, *args, **kwargs):
        super(ReporterComment, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(ReporterComment, self).save(*args, **kwargs)
