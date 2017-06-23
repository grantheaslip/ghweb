from django.conf.urls import url
from django.views.generic import TemplateView
from .views import IndexView, NotFoundView

app_name = 'personal'
urlpatterns = [
    url(
        r'^$',
        IndexView.as_view(),
        name='personal.index'
    ),
    url(
        r'^static/personal/favicons/manifest.json$',
        TemplateView.as_view(
            template_name='personal/manifest.json',
            content_type='application/json'
        ),
        name='personal.manifestjson',
    ),
    url(
        r'',
        NotFoundView.as_view(),
        name='personal.notfound'
    )
]
