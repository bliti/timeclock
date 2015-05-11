from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect, render
from organizations.forms import OrganizationLoginForm
from organizations.models import Organization
from employees.forms import EmployeeLoginForm
from employees.models import Employee


class OrganizationView(FormView):
    template_name = "organization.html"
    form_class = OrganizationLoginForm
    success_url = reverse_lazy('employee-view')


    def form_valid(self, form):
        """
        Checks to see if the organization credentials
        being posted are correct.
        """
        try:
            organization = Organization.objects.get(name=form.cleaned_data['name'], password=form.cleaned_data['password'])
            self.request.session['organization_name'] = organization.name
            return super(OrganizationView, self).form_valid(form)
        
        except ObjectDoesNotExist:
            messages.add_message(self.request, messages.WARNING, 'Incorrect Organization Credentials')
            return redirect(reverse_lazy('organization-view'))
        
        except MultipleObjectsReturned:
            messages.add_message(self.request, messages.WARNING, 'There was an error in your request. Please try again.')
            return redirect(reverse_lazy('organization-view'))
        
        messages.add_message(self.request, messages.WARNING, 'Something went wrong. Please try again.')
        return redirect(reverse_lazy('organization-view'))


class EmployeeView(FormView):
    template_name = "employee.html"
    form_class = EmployeeLoginForm
    success_url = reverse_lazy('employee-clock-view')
    
    
    def form_valid(self, form):
        """
        Checks to see if the employee username
        being posted is correct.
        """
        try:
            employee = Employee.objects.get(username=form.cleaned_data['username'])
            self.request.session['username'] = employee.username
            return super(EmployeeView, self).form_valid(form)
        
        except ObjectDoesNotExist:
            messages.add_message(self.request, messages.WARNING, 'Incorrect Employee')
            return redirect(reverse_lazy('employee-view'))
        
        except MultipleObjectsReturned:
            messages.add_message(self.request, messages.WARNING, 'There was an error in your request. Please try again.')
            return redirect(reverse_lazy('employee-view'))
        
        messages.add_message(self.request, messages.WARNING, 'Something went wrong. Please try again.')
        return redirect(reverse_lazy('employee-view'))
    

class EmployeeClockView(TemplateView):
    template_name = "employee-clock.html"                