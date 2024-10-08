from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("products",views.products,name="products"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)