from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Church, Contribution, Request, Donation
from .forms import ContributionForm, RequestForm, DonationForm, ChurchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .models import User,Church
from .forms import CustomUserCreationForm  # Create a custom form for registration



def register(request):
    churches = Church.objects.all()  # Fetch all churches to populate the dropdown
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'churches': churches})




class CustomLoginView(LoginView):
    template_name = 'login.html'  # Specify your login template path
    success_url = reverse_lazy('church_list')  # Where to redirect after login

class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        return render(request)
        pass

class ChurchListView(ListView):
   model = Church
   template_name = 'church_list.html'
   context_object_name = 'churches'



class ChurchDetailView(DetailView):
    model = Church
    template_name = 'church_detail.html'
    context_object_name = 'church'


class ChurchCreateView( CreateView):
   model = Church
   form_class = ChurchForm
   template_name = 'church_form.html'
   success_url = reverse_lazy('church_list')

#edit church
class EditChurchView( UpdateView):  # Use View class for class-based views
    def get(self, request, pk):
        church = get_object_or_404(Church, pk=pk)
        form = ChurchForm(instance=church)
        return render(request, 'church_form.html', {'form': form})

    def post(self, request, pk):
        church = get_object_or_404(Church, pk=pk)
        form = ChurchForm(request.POST, instance=church)
        if form.is_valid():
            form.save()
            return redirect('church_list')  # Redirect to the church list after updating
        return render(request, 'church_form.html', {'form': form})


#class ChurchUpdateView(LoginRequiredMixin, UpdateView):
  #  model = Church
  #  form_class = ChurchForm
   # template_name = 'church_form.html'
   # success_url = reverse_lazy('church_list')

#class ChurchDeleteView(LoginRequiredMixin, DeleteView):
  #  model = Church
    #template_name = 'church_confirm_delete.html'
    #success_url = reverse_lazy('church_list')

class ContributionListView(ListView):
    model = Contribution
    template_name = 'contribution_list.html'
    context_object_name = 'contributions'

    def get_queryset(self):
        return Contribution.objects.filter(church_id=self.kwargs['church_id'])


class ContributionCreateView(LoginRequiredMixin, CreateView):
    model = Contribution
    form_class = ContributionForm
    template_name = 'contribution_form.html'

    def form_valid(self, form):
        form.instance.church_id = self.kwargs['church_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contribution_list', kwargs={'church_id': self.kwargs['church_id']})



class ContributionUpdateView(LoginRequiredMixin, UpdateView):
    model = Contribution
    form_class = ContributionForm
    template_name = 'contribution_form.html'

    def get_success_url(self):
        return reverse_lazy('contribution_list', kwargs={'church_id': self.object.church.id})



class ContributionDeleteView(LoginRequiredMixin, DeleteView):
    model = Contribution
    template_name = 'contribution_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('contribution_list', kwargs={'church_id': self.object.church.id})

class RequestListView(ListView):
    model = Request
    template_name = 'request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return Request.objects.filter(church_id=self.kwargs['church_id'])

class RequestCreateView(LoginRequiredMixin, CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'request_form.html'

    def form_valid(self, form):
        form.instance.church_id = self.kwargs['church_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('request_list', kwargs={'church_id': self.kwargs['church_id']})

class RequestUpdateView(LoginRequiredMixin, UpdateView):
    model = Request
    form_class = RequestForm
    template_name = 'request_form.html'

    def get_success_url(self):
        return reverse_lazy('request_list', kwargs={'church_id': self.object.church.id})


class RequestDeleteView(LoginRequiredMixin, DeleteView):
    model = Request
    template_name = 'request_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('request_list', kwargs={'church_id': self.object.church.id})



class DonationListView(ListView):
    model = Donation
    template_name = 'donation_list.html'
    context_object_name = 'donations'

    def get_queryset(self):
        return Donation.objects.filter(request_id=self.kwargs['request_id'])



class DonationCreateView(LoginRequiredMixin, CreateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donation_form.html'

    def form_valid(self, form):
        form.instance.request_id = self.kwargs['request_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('donation_list', kwargs={'request_id': self.kwargs['request_id']})


class DonationUpdateView(LoginRequiredMixin, UpdateView):
    model = Donation
    form_class = DonationForm
    template_name = 'donation_form.html'

    def get_success_url(self):
        return reverse_lazy('donation_list', kwargs={'request_id': self.object.request.id})

class DonationDeleteView(LoginRequiredMixin, DeleteView):
    model = Donation
    template_name = 'donation_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('donation_list', kwargs={'request_id': self.object.request.id})





def delete_church(request, pk):
    # Retrieve the church by its primary key (pk)
    church = get_object_or_404(Church, pk=pk)

    # Delete the church
    church.delete()

    # Add a success message
    messages.success(request, 'Church deleted successfully.')

    # Redirect to the list of churches (update 'church_list' as needed)
    return redirect('church_list')




def edit_church(request, pk):
    # Get the church object or return 404 if not found
    church = get_object_or_404(Church, pk=pk)

    if request.method == 'POST':
        # If the form has been submitted, populate it with the submitted data
        form = ChurchForm(request.POST, instance=church)
        if form.is_valid():
            form.save()  # Save the changes
            # Redirect after saving (update the URL as needed)
            return redirect('church_list')
    else:
        # If the request is GET, display the form with the current church data
        form = ChurchForm(instance=church)

    # Render the form template with the form context
    return render(request, 'church_form.html', {'form': form})




