from django.urls import path
from .views import IndexView, CreateForm, UpdateForm, DeleteForm

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateForm.as_view(), name='create'),
    path('update/<int:pk>', UpdateForm.as_view(), name='update'),
    path('delete/<int:pk>', DeleteForm.as_view(), name='delete')
]
