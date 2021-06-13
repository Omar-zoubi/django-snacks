from django.urls import path
from .views import firstView, secondView

# from .views import HomePageView, AboutView
urlpatterns=[
    path('', firstView.as_view(), name='home'),
    path('about', secondView.as_view(), name='about'),

]