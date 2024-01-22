from django.contrib import admin
from teretana.models import *

# Register your models here.

model_list = [Oznaka, Plan, Korisnik, Pretplatnik, Trener, Pretplata]
admin.site.register(model_list)