from django.urls import path
from .import views

urlpatterns = [
    # ('<urlpattern>',views.<ClassBased View>.as_view(),name= '<path_reference_name>')
    path('', views.homeView, name = 'homepage'),
    path('about', views.aboutView, name = 'aboutpage'),
    path('contact', views.contactView, name= 'contactpage'),
    path('products/<int:pk>', views.ProductDetails.as_view(), name = 'prod_details')
]
