from django.contrib import admin
from .models import *

#OJ_Models = [models.Problems, models.Solutions, models.TestCases, models.UserAdmission]
#admin.site.register(OJ_Models)
admin.site.register(Problems)
admin.site.register(Solutions)
admin.site.register(TestCases)
admin.site.register(UserAdmission)
