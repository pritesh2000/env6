from .views import CategoryCreateView, ServiceCreateView, ServiceDeleteView, ServiceDetailView, ServiceListView, ServiceUpdateView, SubcategoryCreateView, index
from django.urls import path

app_name = 'garage'

urlpatterns = [
    path('', index, name='index'),         

    path('addcategory/', CategoryCreateView.as_view(), name='addcategory'),


    path('addsubcategory', SubcategoryCreateView.as_view(), name='addsubcategory'),


    # --------------SERVICE CRUD URL------------
    path('addservice/', ServiceCreateView.as_view(), name='addservice'),
    path('listservice/', ServiceListView.as_view(), name='listservice'),
    path('<int:pk>/deleteservice/', ServiceDeleteView.as_view(), name='deleteservice'),
    path('<int:pk>/updateservice/', ServiceUpdateView.as_view(), name='updateservice'),
    path('<int:pk>/detailservice/', ServiceDetailView.as_view(), name='detailservice'),
]