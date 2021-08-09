from django.core.exceptions import PermissionDenied


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class AnyGroupRequiredMixin:
    required_groups = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if not request.user.is_authenticated:
            raise PermissionDenied

        user_group_names = [g.name for g in request.user.groups.all()]
        result = set(user_group_names).intersection(self.required_groups)
        if self.required_groups and not result:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
