from django.contrib import admin
from user import User, Profil


# Register your models here.
class UserAdmin(admin.ModelAdmin):
	fields = ['firstname', 'lastname', 'mail', 'password']


admin.site.register(User, UserAdmin)
admin.site.register(Profil)
