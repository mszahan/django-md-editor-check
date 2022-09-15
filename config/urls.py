from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')), 
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('cfroala.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)