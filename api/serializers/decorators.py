from functools import wraps

from ..models import ProfileModel


def profile_analyser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        profile = ProfileModel.objects.filter(user_id=args[1].user.id).first()
        kwargs["profile"] = profile
        return func(*args, **kwargs)

    return wrapper
