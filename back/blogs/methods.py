from .models import Blog
from ..users.models import User


def is_user_blog(user: User, blog: Blog) -> bool:
    if blog.user == user:
        return True
    return False
