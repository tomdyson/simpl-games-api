from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import PeriodForm
from ..models import Period


class PeriodCreateView(SuccessMessageMixin, CreateView):
    model = Period
    form_class = PeriodForm
    template_name = 'simpl/periods/period_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:period_detail', args=(self.object.pk,))


class PeriodDeleteView(DeleteView):
    model = Period
    template_name = 'simpl/periods/period_delete.html'
    context_object_name = 'period'
    success_message = 'Period was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:period_list')


class PeriodDetailView(DetailView):
    model = Period
    template_name = 'simpl/periods/period_detail.html'
    context_object_name = 'period'


class PeriodListView(ListView):
    model = Period
    template_name = 'simpl/periods/period_list.html'
    paginate_by = 20
    context_object_name = 'period_list'
    allow_empty = True


class PeriodUpdateView(UpdateView):
    model = Period
    form_class = PeriodForm
    template_name = 'simpl/periods/period_update.html'
    context_object_name = 'period'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:period_detail', args=(self.object.pk,))