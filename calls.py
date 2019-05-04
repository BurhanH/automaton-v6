import requests


URL = 'http://jsonplaceholder.typicode.com'
POSTS_URL = '{}/posts'.format(URL)
COMMENTS_URL = '{}/comments'.format(URL)


def get_resource(url: str):
    """ Common function to make and get result

    Args:
        url (str): url for request

    Returns:
        response object or None
    """
    response = requests.get(url)

    if response.ok:
        return response
    return None


def fetch_url(url: str, number: int) -> str:
    """ Function to fetch url

    Args:
        url (str): url for request
        number (str): number for request

    Returns:
         url (str): e.g. http://your.com/resource_name/number
    """
    return f'{url}/{number}'


def get_posts(number: int = None):
    """ Function to get posts or post

    Args:
        number (str): number of post

    Returns:
        response object or None
    """
    if number:
        return get_resource(fetch_url(POSTS_URL, number))
    return get_resource(POSTS_URL)


def get_comments(number: int = None):
    """ Function to get comments or comment

    Args:
        number (str): number of comment

    Returns:
        response object or None
    """
    if number:
        return get_resource(fetch_url(COMMENTS_URL, number))
    return get_resource(COMMENTS_URL)
