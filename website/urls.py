from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^organization/signout/$', OrganizationSignOutView.as_view(), name="organization-signout-view"),
    url(r'^employee/clock/report/$',  EmployeeXlsxReportView.as_view(), name="employee-clock-report"),
    url(r'^employee/clocks/$',  EmployeeClockSearchView.as_view(), name="clock-search"),
    url(r'^employee/signout/$', EmployeeSignOutView.as_view(), name="employee-signout-view"),
    url(r'^employee/clock/$', EmployeeClockView.as_view(), name="employee-clock-view"),
    url(r'^employee/$', EmployeeView.as_view(), name="employee-view"),
    url(r'^$', OrganizationView.as_view(), name="organization-view"),
]