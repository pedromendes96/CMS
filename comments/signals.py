from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NormalComment, ReporterComment, ProfessionalComment


@receiver(post_save, sender=NormalComment)
def notify_pending_comment(sender, **kwargs):
    pass


@receiver(post_save, sender=NormalComment)
def notify_that_is_spam(sender, **kwargs):
    pass


@receiver(post_save, sender=NormalComment)
def notify_that_was_validated(sender, **kwargs):
    pass


@receiver(post_save, sender=NormalComment)
def notify_answer_to_the_comment(sender, **kwargs):
    pass


@receiver(post_save, sender=ReporterComment)
@receiver(post_save, sender=ProfessionalComment)
def notify_people_that_follow_entity(sender, **kwargs):
    pass
