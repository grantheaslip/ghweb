from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

app_name = 'ghweb'
urlpatterns = [
    # Todo: Set permanent=True once this is tested
    url(r'^(?P<canonical_path>.*)index\.html$', RedirectView.as_view(url='/%(canonical_path)s')),
    url(r'^', include('personal.urls'))
]
