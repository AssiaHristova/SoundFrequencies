from django.contrib import admin

from sound_frequencies.web.models import Article, Artist, Release, Photo, Event, Merchandise


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    def show_links(self, obj):
        return '<a href="%s">%s</a>' % (obj.links, obj.links)

    show_links.allow_tags = True


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


class PhotoInline(admin.StackedInline):
    model = Photo


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    pass

