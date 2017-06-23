from django.conf.urls import url
from .views import IndexView, NotFoundView

app_name = 'personal'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='personal.index'),
    url(r'', NotFoundView.as_view(), name='personal.notfound')
]
