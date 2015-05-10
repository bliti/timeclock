from django.conf.urls import url
from .views import OrganizationView, EmployeeView, EmployeeClockView

urlpatterns = [
    url(r'^employee/clock/$', EmployeeClockView.as_view(), name="employee-clock-view"),
    url(r'^employee/$', EmployeeView.as_view(), name="employee-view"),
    url(r'^$', OrganizationView.as_view(), name="organization-view"),
]