from tgblogparser.objects.basic_objects import ApiGetRequestMixin, ApiPostRequestMixin


class ApiGetOrPostMixin(ApiGetRequestMixin, ApiPostRequestMixin):
    pass
