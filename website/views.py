from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView
from organizations.forms import OrganizationForm


class EmployeeView(TemplateView):
    template_name = "employee.html"


class EmployeeClockView(TemplateView):
    template_name = "employee-clock.html"


class OrganizationView(FormView):
    template_name = "company.html"
    form_class = OrganizationForm
    success_url = reverse_lazy('employee-view')
    
    
    def form_valid(self, form):
        #process the form here!
        #pasuign for mother's day. :D
        return super(OrganizationView, self).form_valid(form)