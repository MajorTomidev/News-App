from django.urls import path
from .views import api_list_page, Api_list_page, api_detail_page, Api_detail_page, api_create_page, api_update_page

urlpatterns = [
    path('home/', api_list_page, name='api-home' ),
    path('class/home/', Api_list_page.as_view(), name='api-list'),
    path('detail/<slug:slug>/', api_detail_page, name='api-detail'),
    path('class/detail/<slug:slug>/', Api_detail_page.as_view(), name='api-detail-list'),
    path('create/', api_create_page, name='api-create'),  
    path('update/<slug:slug>/',api_update_page, name='api-update'),                                                        
]