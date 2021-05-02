from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    # Blog
    path('blog/', include('blog.urls', namespace='blog'))
]
