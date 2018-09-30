import requests


URL = 'http://jsonplaceholder.typicode.com'
POSTS_URL = '{}/posts'.format(URL)
COMMENTS_URL = '{}/comments'.format(URL)


def get_resource(url):
    """
    Common function to make and get result
    :param url: url for request
    :return: response object or None
    """
    response = requests.get(url)

    if response.ok:
        return response
    return None


def fetch_url(url, number):
    """
    Function to fetch url
    :param url: url for request
    :param number: number for request
    :return: url string (e.g. http://your.com/resource_name/number)
    """
    return '{}/{}'.format(url, number)


def get_posts(number=None):
    """
    Function to get posts or post
    :param number: number of post
    """
    if number:
        return get_resource(fetch_url(POSTS_URL, number))
    return get_resource(POSTS_URL)


def get_comments(number=None):
    """
    Function to get comments or comment
    :param number: number of comment
    """
    if number:
        return get_resource(fetch_url(COMMENTS_URL, number))
    return get_resource(COMMENTS_URL)
