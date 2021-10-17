from datetime import datetime
from django.views.generic import ListView

from sound_frequencies.web.models import Event, Merchandise, Photo, Artist, Release, Article, Video


class HomePageView(ListView):
    model = Merchandise
    template_name = 'web/list_templates/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = Video.objects.last()
        event = Event.objects.filter(date__gt=datetime.today()).first()
        merch_list = Merchandise.objects.order_by('date')[:3]
        context = {'video': video,
                   'event': event,
                   'merch_list': merch_list
                   }
        return context


class EventListView(ListView):
    model = Event
    template_name = 'web/list_templates/events_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        upcoming_events = Event.objects.filter(date__gt=datetime.today())
        past_events = Event.objects.filter(date__lt=datetime.today()).exclude(id=3)
        user_events = Event.objects.filter(user_id=self.request.user.id)
        context = {
            'upcoming_events': upcoming_events,
            'past_events': past_events,
            'user_events': user_events,
        }
        return context


class ArtistListView(ListView):
    model = Artist
    template_name = 'web/list_templates/artists_list.html'


class ReleaseListView(ListView):
    model = Release
    template_name = 'web/list_templates/releases_list.html'


class PhotoListView(ListView):
    model = Photo
    template_name = 'web/list_templates/photos_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = Photo.objects.all()
        user_photos = Photo.objects.filter(user_id=self.request.user.id)
        photos_ordered_by_event = Photo.objects.order_by('event')
        events_with_photos = set([photo.event for photo in photos])
        context = {
            'user_photos': user_photos,
            'events_with_photos': events_with_photos,
            'photos_ordered_by_event': photos_ordered_by_event,
        }
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'web/list_templates/articles_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_articles = Article.objects.filter(user_id=self.request.user.id)
        articles = Article.objects.all()
        context = {
            'articles': articles,
            'user_articles': user_articles
        }
        return context


class MerchandiseListView(ListView):
    model = Merchandise
    template_name = 'web/list_templates/merchandise_list.html'


class VideoListView(ListView):
    model = Video
    template_name = 'web/list_templates/videos_list.html'


