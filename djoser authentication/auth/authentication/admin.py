from django.contrib import admin
from authentication.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id','email','name','is_active','is_admin')




    
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials',{'fields':('email','password')}),
        ('Personal Info',{'fields':('name',)}),
        ('Permissions',{'fields':('is_admin','is_active')}),

    )

    add_fieldsets = (
        (None,{'classes':('wide',),
               'fields':('email','name','password1','password2')}),
    )

    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()

admin.site.register(User,UserModelAdmin)

