from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FacebookLiveStreamGroup, FacebookLiveStreamPage

import logging

logger = logging.getLogger("multimedia")


def on_save_stream(sender, *args, **kwargs):
    instance = kwargs.get("instance")
    created = kwargs.get("created")
    update_fields = kwargs.get("update_fields", [])

    logger.info("on_save_stream:\ninstance:{}\ncreated:{}\nupdate_fields:{}\nvars:{}".format(
        instance, created, update_fields, vars(instance)))

    if (not created and "is_live" in update_fields and instance.is_live) or (created and instance.is_live):
        import pdb
        pdb.set_trace()
        logger.info("Starting at the instance {}".format(instance))
        instance.start()

    if not created and "is_live" in update_fields and not instance.is_live:
        logger.info("Ending at the instance {}".format(instance))
        instance.end()


post_save.connect(on_save_stream, dispatch_uid="facebook_live_stream_group_save",
                  sender=FacebookLiveStreamGroup)
post_save.connect(on_save_stream, dispatch_uid="facebook_live_stream_page_save",
                  sender=FacebookLiveStreamPage)
