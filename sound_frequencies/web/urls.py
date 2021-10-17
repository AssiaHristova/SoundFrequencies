from django.urls import path

from sound_frequencies.web.views.crud_views.view import EventCreateView, EventUpdateView, EventDeleteView, \
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView
from sound_frequencies.web.views.general.views import about_page, contacts_page
from sound_frequencies.web.views.list_views.views import HomePageView, EventListView, ArtistListView, ReleaseListView, \
    PhotoListView, ArticleListView, MerchandiseListView, VideoListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home page'),
    path('events/', EventListView.as_view(), name='events list'),
    path('artists/', ArtistListView.as_view(), name='artists list'),
    path('photos/', PhotoListView.as_view(), name='photos list'),
    path('releases/', ReleaseListView.as_view(), name='releases list'),
    path('articles/', ArticleListView.as_view(), name='articles list'),
    path('merches/', MerchandiseListView.as_view(), name='merches list'),
    path('videos/', VideoListView.as_view(), name='videos list'),
    path('events/create/', EventCreateView.as_view(), name="event create"),
    path('events/update/<int:pk>', EventUpdateView.as_view(), name="event update"),
    path('events/delete/<int:pk>', EventDeleteView.as_view(), name="event delete"),
    path('articles/create/', ArticleCreateView.as_view(), name="article create"),
    path('articles/update/<int:pk>', ArticleUpdateView.as_view(), name="article update"),
    path('articles/delete/<int:pk>', ArticleDeleteView.as_view(), name="article delete"),
    path('photos/create/', PhotoCreateView.as_view(), name="photo create"),
    path('photos/update/<int:pk>', PhotoUpdateView.as_view(), name="photo update"),
    path('photos/delete/<int:pk>', PhotoDeleteView.as_view(), name="photo delete"),
    path('about/', about_page, name='about us'),
    path('contacts/', contacts_page, name='contact us'),
]
