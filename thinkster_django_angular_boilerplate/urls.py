from django.conf.urls import patterns, url, include

from thinkster_django_angular_boilerplate.views import IndexView
from rest_framework_nested import routers

from authentication.views import UsuarioViewSet

router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)
