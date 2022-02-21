from django.urls import path
from . import views

urlpatterns = [
    path('api/children', views.ChildrenList.as_view(), name='children_list'),
    path('api/children/<int:pk>', views.ChildrenDetails.as_view(), name='children_detail'),
]