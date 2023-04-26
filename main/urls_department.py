from django.urls import path
from . import views 

urlpatterns = [
   path('crear-departamento/',views.create_department,name='create_department'),
   path('departmentos/',views.show_department,name='show_departments'),
   path('borrar-departamento/<int:id>',views.delete_department,name='delete_department')
]