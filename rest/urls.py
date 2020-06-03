
from django.conf.urls import url,include
from django.contrib import admin
from frame import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'^datatest',views.DataList)
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^data/(?P<id>\d+)/$', views.DataDetails.as_view()),
    #url(r'^datatest/',views.DataList.as_view()),
    url('',include(router.urls)),
    url(r'admin/',admin.site.urls),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
