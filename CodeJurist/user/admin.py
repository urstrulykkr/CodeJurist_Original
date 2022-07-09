from django.contrib import admin
from .models import Submission
from user.models import Submission

admin.site.register(Submission)