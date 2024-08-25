from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]

def create_admin_user(username, password):
    user = user.objects.create_user(username=username, password=password)
    user_profile = user_profile.objects.create(user=user, role='Admin')
    user_profile.can_view_admin_panel = True
    user_profile.save()
from django.urls import path
from . import views

urlpatterns = [
    # Other paths...
    path('books/', views.BookListView.as_view(), name='books'),
]

