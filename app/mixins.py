from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SetUserMixin(LoginRequiredMixin):

    def form_valid(self, form):
        setattr(form.instance, 'user', self.request.user)
        return super().form_valid(form)


class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class CreateUpdateView(SingleObjectTemplateResponseMixin, ModelFormMixin,
                       ProcessFormView
                       ):
    def get_object(self, queryset=None):
        try:
            return super(CreateUpdateView, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).post(request, *args, **kwargs)
