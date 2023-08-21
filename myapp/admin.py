from django.contrib import admin
from .models import Emp,Role,Department
# Register your models here.

admin.site.register(Emp)
admin.site.register(Role)
admin.site.register(Department)