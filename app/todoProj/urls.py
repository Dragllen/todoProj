from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from todos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)