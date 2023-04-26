from django.urls import path
from . import views 

urlpatterns = [
    path('crear-producto/',views.create_product,name='create_product'),
    path('actualizar-producto/<int:id>',views.update_product,name='update_product'),
    path('borrar-producto/<int:id>',views.delete_product,name='delete_product'),
]