from django.shortcuts import render
from utils.views import TableIndexView
from comments.tables.comments_table import CommentProcess

# Create your views here.


class CommentsIndexView(TableIndexView):
    process_class = CommentProcess
