from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()


router.register('customerapi',views.CustomerModelViewset,basename='customer')
router.register('productapi',views.ProductModelViewset,basename='product')





urlpatterns=[
    path('api/',include(router.urls)),
    path('list/',views.Listview.as_view())

]