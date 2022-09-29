from django.contrib import admin

from . models import travelmodel
from . models import travelpost

# Register your models here.
admin.site.register(travelmodel)
admin.site.register(travelpost)