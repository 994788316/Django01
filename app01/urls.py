# from django.conf.urls import include, url

from django.conf.urls import include, url
from django.contrib import admin

from app01 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^show_deps$', views.show_deps),
    url(r'^show_dep/(\d+)$', views.show_dep),
    url(r'^add_dep$', views.add_dep),
    url(r'^del_dep/(\d+)$', views.del_dep),

]

























# from app01 import views
#
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^show_deps$', views.show_deps),
#     url(r'^show_dep/(\d+)$', views.show_dep)

# ]





















