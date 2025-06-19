

from django.views.static import serve

from django.urls import path,re_path

from django.conf import settings
from django.conf.urls.static import static
from .views import image_detail,contact,home,success,subscribe,about,services,custom_404,gallery,products

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
  
    path('', home, name='homepage'),
    path('image-detail/<int:image_id>/', image_detail, name='image_detail'),
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe,  name='subscribe'),
    path('success/', success,  name='success_page'),
    path('about/', about,  name='about'),
    path('services/', services,  name='services'),
     path('products/', products,  name='products'),
    path('gallery/', gallery,  name='gallery')
]
# Add the catch-all pattern for 404
urlpatterns += [re_path(r'^.*/$', custom_404)]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)