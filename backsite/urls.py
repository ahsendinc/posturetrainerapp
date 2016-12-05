"""backsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from postureapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'documents', views.DocumentViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'recommendations', views.RecommendationViewSet)
router.register(r'pickleobjects', views.PickleObjectViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^postureapp/', include('postureapp.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^$', RedirectView.as_view(url='/postureapp/index/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
