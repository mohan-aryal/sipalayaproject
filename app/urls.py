from django.urls import path
from .views import show, Myview, Child, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('show/', show, name="show"),
    path('view/', Myview.as_view()),
    path('child/', Child.as_view()),
   
]
