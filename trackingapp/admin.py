from django.contrib import admin

# Register your models here.

from trackingapp.models import Bugtrack,DevProfile
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     pass

@admin.register(DevProfile)
class DevProfileAdmin(admin.ModelAdmin):
    list_disaply=['key_skills','experience']




@admin.register(Bugtrack)
class BugtrackAdmin(admin.ModelAdmin):
    list_display = ['assigned_to','title','created_on','priority','current_status','final_status','points','img']
    list_filter = ( 'priority','created_on',)

    def img(self,obj):
        return format_html('<img src="{}" width=50,height=40 alt="*"/>'.format(obj.upload_image.url))
    img.allow_tags = True

    def get_queryset(self, request):
        qs = super(BugtrackAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(assigned_to=request.user)

    def get_actions(self, request):
        actions = super(BugtrackAdmin, self).get_actions(request)
        if request.user.is_superuser:
            return actions
        else:
            del actions['delete_selected']

    def get_readonly_fields(self, request, obj=None):
        # readonly_fields = ('admission', 'courses',)
        if request.user.is_superuser:
            return self.readonly_fields

        # readonly_fields = ('title','description','assigned_to','created_on','priority','upload_image','reference','final_status','points',)

        return self.readonly_fields + ('title','description','assigned_to','created_on','priority','upload_image','reference','final_status','points',)
