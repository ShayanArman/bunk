from django.contrib import admin
from .models import Bunk, UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', "get_image"]

	def get_image(self, obj):
		url = "/" + obj.photo.url
		return '<img src="%s" height="123" width="123"/>' % url
	get_image.short_description = "Image"
	get_image.allow_tags = True	

class BunkAdmin(admin.ModelAdmin):
	list_display = ['from_user', 'to_user', 'bunk_time']

admin.site.register(Bunk, BunkAdmin)
admin.site.register(UserProfile, UserProfileAdmin)