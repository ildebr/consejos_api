from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
# Register your models here.
 
# class UserAdminConfig(UserAdmin):
# 	model = NewUser
# 	search_fields = ('email', 'user_name', 'first_name',)
# 	list_filter = ('email', 'user_name', 'first_name','is_active', 'is_staff',)
# 	ordering = ('-start_date',)
# 	list_display = ('email', 'id', 'user_name', 'first_name','is_active', 'is_staff',)
# 	fieldsets = (
# 	(None, {'fields' : ('email', 'user_name', 'first_name',)}),
# 	('Permissions', {'fields': ('is_staff', 'is_active',)}),
# 	('Personal', {'fields': ('about',)}),
# 	)

# admin.site.register(NewUser, UserAdminConfig)

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
	search_fields = ('email ', 'user_name', 'first_name',)
	ordering = ('-start_date',)
	list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
	fieldsets = (
		(None, {'fields' : ('email', 'user_name', 'first_name', 'last_name' ,'CI','phone',)}),
		('Permissions', {'fields': ('is_staff', 'is_active')}),
		('Personal', {'fields': ('about',)}),
		)
	add_fieldsets = (
		(None,{
			'classes': ('wide',),
			'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
			}),
		)

admin.site.register(NewUser, UserAdminConfig)