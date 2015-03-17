from django.contrib import admin
from user import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
	fields = ['firstname', 'lastname', 'mail', 'password']

admin.site.register(User, UserAdmin)
