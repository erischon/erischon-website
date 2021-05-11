from django.urls import path
from . import views


urlpatterns = [
    path('', views.portfolio_homepage, name='portfolio-hp'),
    path('project/<int:id>', views.project, name='project-detail'),
]
