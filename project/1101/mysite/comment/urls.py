from django.urls import path
from . import views

urlpatterns = [
    path('update_comment',views.upadte_comment,name='update_comment')
]