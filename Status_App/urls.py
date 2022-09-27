from django.urls import path, include
from .views import *

urlpatterns = [
    path('list', StatusListCreateApiView.as_view()),
    path('retrieve/<id>/', StatusRetriveUpdateDestroyApiView.as_view())

]