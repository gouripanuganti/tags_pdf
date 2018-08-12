from django.contrib import admin

from .models import Board
from .models import *

admin.site.register(Sales)
admin.site.register(Products)

admin.site.register(Board)