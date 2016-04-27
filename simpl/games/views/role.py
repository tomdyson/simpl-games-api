from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from ..forms import RoleForm
from ..models import Role


class RoleCreateView(SuccessMessageMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'simpl/roles/role_create.html'
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        return reverse('simpl:role_detail', args=(self.object.pk,))


class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'simpl/roles/role_delete.html'
    context_object_name = 'role'
    success_message = 'Role was deleted successfully'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('simpl:role_list')


class RoleDetailView(DetailView):
    model = Role
    template_name = 'simpl/roles/role_detail.html'
    context_object_name = 'role'


class RoleListView(ListView):
    model = Role
    template_name = 'simpl/roles/role_list.html'
    paginate_by = 20
    context_object_name = 'role_list'
    allow_empty = True


class RoleUpdateView(UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'simpl/roles/role_update.html'
    context_object_name = 'role'
    success_message = '%(name)s was updated successfully'

    def get_success_url(self):
        return reverse('simpl:role_detail', args=(self.object.pk,))