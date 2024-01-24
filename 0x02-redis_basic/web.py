import requests
import redis
from typing import Callable

redis_client = redis.Redis()


def cache_decorator(func: Callable) -> Callable:
    """
    Decorator to cache the result of a function
    with a specified expiration time.
    """
    def wrapper(*args, **kwargs):
        """
        Generate a cache key based on the function name and arguments
        """
        cache_key = f"cache:{func.__name__}:{args}"

        cached_result = redis_client.get(cache_key)
        if cached_result:
            return cached_result.decode('utf-8')

        result = func(*args, **kwargs)

        redis_client.setex(cache_key, 10, result)

        return result

    return wrapper


@cache_decorator
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL
    and cache the result with an expiration time of 10 seconds.
    """
    access_count_key = f"count:{url}"
    redis_client.incr(access_count_key)

    response = requests.get(url)
    html_content = response.text

    return html_content
