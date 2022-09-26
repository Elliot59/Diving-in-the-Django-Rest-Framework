from django.urls import path, include
from .views import *

urlpatterns = [
    path('', StatusListCreateApiView.as_view()),
    path('<id>/', StatusRetriveUpdateDestroyApiView.as_view())

]