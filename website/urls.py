from django.conf.urls import url
from .views import OrganizationView

urlpatterns = [
    url(r'^', OrganizationView.as_view(), name="organization-view"),
]