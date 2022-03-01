
from django.urls import path
from .import views
urlpatterns = [
    path('',views.main),
    path('api-views/',views.mainhit.as_view()),
    path('skill-api/',views.skilApi.as_view(),name="skill"),
    path('project-api/',views.projectModelApi.as_view(), name="project"),
]
