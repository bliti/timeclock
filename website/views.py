from django.views.generic import TemplateView


class EmployeeView(TemplateView):
    template_name = "employee.html"


class EmployeeClockView(TemplateView):
    template_name = "employee-clock.html"


class OrganizationView(TemplateView):
    template_name = "company.html"