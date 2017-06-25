from django.conf.urls import url
from django.views.generic import TemplateView
from .views import IndexView, NotFoundView

app_name = 'personal'
urlpatterns = [
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'',
        NotFoundView.as_view(),
        name='notfound'
    )
]
