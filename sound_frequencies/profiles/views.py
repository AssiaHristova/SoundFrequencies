from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, FormView, UpdateView, ListView, DeleteView

from sound_frequencies.profiles.forms import SignUpForm, LogInForm, ProfileForm
from sound_frequencies.profiles.models import Profile
from sound_frequencies.web.models import Event, Article, Photo

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'profiles/sign_up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        registered_user = super().form_valid(form)
        login(self.request, self.object)
        return registered_user


class LogInView(LoginView):
    authentication_form = LogInForm
    template_name = 'profiles/log_in.html'
    success_url = reverse_lazy('home page')


def log_out(request):
    logout(request)
    return redirect('home page')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_details.html'
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=self.request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=self.request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.age = form.cleaned_data['age']
        self.object.gender = form.cleaned_data['gender']
        if form.is_valid():
            self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object
        return context


class ProfileUploadsView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_uploads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(user_id=self.request.user.id)
        events = Event.objects.filter(user_id=self.request.user.id)
        photos = Photo.objects.filter(user_id=self.request.user.id)
        context = {
            'articles': articles,
            'events': events,
            'photos': photos
        }
        return context


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profiles/profile_delete.html'
    success_url = reverse_lazy('profile details')


