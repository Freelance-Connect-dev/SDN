from django.contrib import admin

# Register your models here.
from .models import Posting
from .models import Member
from .models import Tag
from .models import Contract
from .models import Application

admin.site.register(Posting)
admin.site.register(Member)
admin.site.register(Tag)
admin.site.register(Contract)
admin.site.register(Application)
