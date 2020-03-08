
from django.conf.urls import url, include
from django.contrib import admin
from faceRecog import views as app_views
admin.autodiscover()
urlpatterns = [
    url(r'^$', app_views.index),
    url(r'^error_image$', app_views.errorImg),
    url(r'^create_dataset$', app_views.create_dataset),
    url(r'^trainer$', app_views.trainer),
    url(r'^eigen_train$', app_views.eigenTrain),
    url(r'^detect$', app_views.detect),
    url(r'^detect_image$', app_views.detectImage),
    url(r'^admin/', admin.site.urls),
    url(r'^records/', include('records.urls')),
]