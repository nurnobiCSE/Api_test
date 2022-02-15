
from django.urls import path
from .import views
urlpatterns = [
    path('api/',views.main),
    path('api-views/',views.mainhit.as_view()),
]
