from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('product/', views.home, name='home'),  # This could be another view if needed
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),  # Product detail
    path('addrase/', views.addrase, name='addrase'),  # Address form
    path('order/', views.order, name='order'),  # Order confirmation
    path('payment/', views.payment, name='payment'),  # Payment processing
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

