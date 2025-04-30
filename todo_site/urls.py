from django.urls import path
from todo import views
from django.contrib import admin

urlpatterns = [
    # Home page
    path('', views.index, name="todo"),

    # Delete a todo item by ID
    path('del/<str:item_id>/', views.remove, name="del"),

    # Admin panel
    path('admin/', admin.site.urls),
]
