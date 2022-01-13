from django.urls import path
from . import views
urlpatterns = [
    path('', views.myfunc),
    path('get-info/', views.myapiview.as_view()),
]
