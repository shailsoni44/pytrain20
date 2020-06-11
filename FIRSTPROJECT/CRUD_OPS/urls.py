from CRUD_OPS import views
from django.urls import path

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('success', views.success, name='success'),
    # path('delete/<int:id>', views.destroy),
    # path('edit/<int:id>', views.success),
    path('show', views.show, name='show'),
    path('home', views.home, name='home'),
]
