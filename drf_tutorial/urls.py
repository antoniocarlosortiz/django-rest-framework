from django.conf.urls import url, include
from snippets import views


urlpatterns = [
    url(r'^', include('snippets.urls')),
]
