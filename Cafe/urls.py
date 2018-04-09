from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Cafe import views as del_views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', del_views.IndexView),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login_user/$', del_views.login_user,name = 'login_user1'),
    url(r'^login_restaurant/$', del_views.login_restaurant,name = 'login_user2'),
    url(r'^authenticate_user/$', del_views.authenticate_user),
    url(r'^authenticate_res/$', del_views.authenticate_res),
    url(r'^home/$', del_views.home),
    url(r'^rest_home/$', del_views.rest_home),
    url(r'^cus_reg/$', del_views.customer_register),
    url(r'^res_reg/$', del_views.restaurant_register),
    url(r'^get/(?P<rest_id>\d+)/$',del_views.rest_display),
    url(r'^query/(?P<check_id>\d+)/$', del_views.query),
    url(r'^additem/$', del_views.additem),
    url(r'^deleteitem/$', del_views.deleteitem),
    url(r'^setstatus/$', del_views.setstatus),
    url(r'^cart/$', del_views.cart),
    url(r'^place_order/$', del_views.place_order),
    url(r'^checkout/$', del_views.checkout),
    # url(r'^showorders/$', del_views.showstatus),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
