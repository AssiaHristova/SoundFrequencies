from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView

from sound_frequencies.web.models import Event, Article, Photo
from sound_frequencies.web.forms import EventForm, ArticleForm, PhotoForm


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'web/crud_templates/event_create.html'
    form_class = EventForm
    success_url = reverse_lazy('events list')

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        event.save()
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'web/crud_templates/event_update.html'
    model = Event
    context_object_name = 'event'
    form_class = EventForm
    success_url = reverse_lazy('events list')


class EventDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'web/crud_templates/event_delete.html'
    model = Event
    success_url = reverse_lazy('events list')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'web/crud_templates/article_create.html'
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('articles list')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.user = self.request.user
        article.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'web/crud_templates/article_update.html'
    model = Article
    context_object_name = 'article'
    form_class = ArticleForm
    success_url = reverse_lazy('articles list')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'web/crud_templates/article_delete.html'
    model = Article
    success_url = reverse_lazy('articles list')


class PhotoCreateView(LoginRequiredMixin, FormView):
    template_name = 'web/crud_templates/photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('photos list')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.image = self.request.FILES['image']
        photo.user = self.request.user
        photo.save()
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'web/crud_templates/photo_update.html'
    model = Photo
    context_object_name = 'photo'
    form_class = PhotoForm
    success_url = reverse_lazy('photos list')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'web/crud_templates/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('photos list')
