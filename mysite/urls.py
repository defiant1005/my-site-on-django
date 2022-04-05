from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from news.views import NewsView

router = SimpleRouter()

router.register('api/news', NewsView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls
