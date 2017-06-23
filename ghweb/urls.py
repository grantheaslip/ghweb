from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

app_name = 'ghweb'
urlpatterns = [
    url(r'^', include('personal.urls'))
]
