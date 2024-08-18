from django.contrib import admin

# Register your models here.
def create_admin_user(username, password):
    user = user.objects.create_user(username=username, password=password)
    user_profile = user_profile.objects.create(user=user, role='Admin')
    user_profile.can_view_admin_panel = True
    user_profile.can_manage_users = True
    user_profile.save()
