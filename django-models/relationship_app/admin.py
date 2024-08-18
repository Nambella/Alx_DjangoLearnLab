from django.contrib import admin
from django.shortcuts import render

# Register your models here.
from django.contrib.auth.decorators import user_passes_test

def has_admin_permissions(user):
    return user.userprofile.role == 'Admin' and user.userprofile.can_view_admin_panel

@user_passes_test(has_admin_permissions)
def admin_view(request):
    # Your admin view logic here
    return render(request, 'admin_view.html')

def create_admin_user(username, password):
    user = user.objects.create_user(username=username, password=password)
    user_profile = user_profile.objects.create(user=user, role='Admin')
    user_profile.can_view_admin_panel = True
    user_profile.save()
