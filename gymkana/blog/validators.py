from django.core.exceptions import ValidationError


class FileLimitSize:
    limit_value = 0

    def __init__(self, limit_value):
        self.limit_value = limit_value

    def __call__(self, limit_value):
        if limit_value.size > (self.limit_value * 1024 * 1024):
            raise ValidationError("Image file too large ( maximum 10mb )")
