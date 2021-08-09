from sound_frequencies.web.models import Event


class EventTestUtils:
    def create_event(self, **kwargs):
        return Event.objects.create(**kwargs)


