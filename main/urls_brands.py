from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('crear-marca/',views.create_brand,name='create_brand'),
    path('borrar-marca/<int:id>',views.delete_brand,name='delete_brand'),
    path('marcas/',views.show_brands,name='show_brands'),
]