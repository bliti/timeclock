from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import View, TemplateView, FormView, WeekArchiveView
from django.shortcuts import redirect, render
from django.utils import timezone
from organizations.forms import OrganizationLoginForm
from organizations.models import Organization
from employees.forms import EmployeeLoginForm
from employees.models import Employee
from clocks.models import EmployeeClock
from datetime import datetime


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
            messages.add_message(self.request, messages.ERROR, 'Incorrect Organization Credentials')
            return redirect(reverse_lazy('organization-view'))
        
        except MultipleObjectsReturned:
            messages.add_message(self.request, messages.ERROR, 'There was an error in your request. Please try again.')
            return redirect(reverse_lazy('organization-view'))
        
        messages.add_message(self.request, messages.ERROR, 'Something went wrong. Please try again.')
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
            messages.add_message(self.request, messages.ERROR, 'Incorrect Employee')
            return redirect(reverse_lazy('employee-view'))
        
        except MultipleObjectsReturned:
            messages.add_message(self.request, messages.ERROR, 'There was an error in your request. Please try again.')
            return redirect(reverse_lazy('employee-view'))
        
        messages.add_message(self.request, messages.ERROR, 'Something went wrong. Please try again.')
        return redirect(reverse_lazy('employee-view'))


class EmployeeClockView(TemplateView):
    template_name = "employee-clock.html"


    def post(self, request, *args, **kwargs):
        """
        Handles the clock button being clicked.
        """
        #make sure the employee is logged in. Double check
        try:
            username = request.session['username']
        except KeyError:
            messages.add_message(self.request, messages.ERROR, 'Sign in to continue')
            return redirect(reverse_lazy('employee-view'))
        
        #get the employee object before we construct the clock object
        try:
            employee = Employee.objects.get(username=username)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            messages.add_message(self.request, messages.ERROR, 'There was an error in your request. Please try again.')
            return redirect(reverse_lazy('employee-view'))
        
        #clock the employee
        clock = EmployeeClock.objects.create(
            timestamp=timezone.now(),
            employee=employee
            )
        
        time_format = '%I:%M %p'
        time = datetime.strftime(clock.timestamp, time_format)
        messages.add_message(
            self.request,
            messages.SUCCESS, 
            '{user} was successfully clocked at {time}'.format(
                user=employee.name,time=time
            )
        )
        
        #log the employee out automatically after a clock
        return redirect(reverse_lazy('employee-signout-view'))


    def get_context_data(self, **kwargs):
        """
        Adding the last 10 clocks
        from this specific employee.
        """        
        #this is so ugly.
        context = super(EmployeeClockView, self).get_context_data(**kwargs)
        
        try:
            employee = Employee.objects.get(username=self.request.session['username'])
            context = super(EmployeeClockView, self).get_context_data(**kwargs)
            #django ORM, you so ugly.
            #get the latest 10 clocks query.
            context['recent_clocks'] = EmployeeClock.objects.filter(employee=employee).order_by('-pk')[:10]
        
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return context

        return context
        

class OrganizationSignOutView(View):
    """
    Signs out an organization to
    prevent employees from clocking.
    """ 
    
    
    def get(self, request, *args, **kwargs):
        """
        Deletes the organization session
        """ 
        try:
            del request.session['organization_name']
        except KeyError:
            pass
            #reason for pass is that if the key does not exist
            #it means that the organization will be signed out anyways.
            #No need to handle the exception with any special instruction.
        messages.add_message(self.request, messages.SUCCESS, 'You were successfully signed out of the organization.')  
        return redirect(reverse_lazy('organization-view'))
    
    
    def post(self, request, *args, **kwargs):
        return redirect('organization-view')


class EmployeeSignOutView(View):
    """
    Signs out an employee
    """ 
    
    
    def get(self, request, *args, **kwargs):
        """
        Deletes the organization session
        """ 
        try:
            del request.session['username']
        except KeyError:
            pass
            #reason for pass is that if the key does not exist
            #it means that the organization will be signed out anyways.
            #No need to handle the exception with any special instruction.    
        return redirect(reverse_lazy('employee-view'))
    
    
    def post(self, request, *args, **kwargs):
        return redirect('employee-view')


#reports
class WeeklyClockReportView(WeekArchiveView):
    """
    Displays all clocks that fall whithin a given week.
    To allow employees to see their past clocks.
    """
    template_name = 'employeeclock_archive_week.html'
    queryset = EmployeeClock.objects.all()
    date_field = "timestamp"
    week_format = "%W"
    allow_future = True
    alow_empty = True