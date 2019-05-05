from django.utils.translation import gettext as _
from utils.tables.process import Process
from comments.models import Comment
import logging

logger = logging.getLogger("administration_section")


class CommentProcess(Process):

    def __init__(self, request, *args, **kwargs):
        super(CommentProcess, self).__init__(request)

    def get_view_details(self):
        return "CommentProcess request"

    def set_thead(self):
        return [
            # user 1º
            ["origin", _("Parent Comment")],
            ["status__status", _("Status of the comment")],
            ["page__title", _("Title of page")],
        ]

    def set_searchable(self):
        return [
            ["origin__icontains", _("Parent Comment")],
            ["status__status__icontains", _("Status of the comment")],
            ["page__title__icontains", _("Title of page")],
        ]

    def set_query_set(self):
        return Comment.objects.all()
