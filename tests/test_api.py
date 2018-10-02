from calls import get_posts, get_comments

HTTP_OK = 200


class TestAPI:
    """
    This tests some API calls
    """
    @staticmethod
    def _assert_equal(a, b):
        """
        Method to compare two status codes
        :param a: actual status code
        :param b: expected status code
        """
        if a != b:
            raise AssertionError("Getting {} status code instead {} as response".format(a, b))

    def test_get_posts(self):
        """
        Testing posts
        """
        response = get_posts()

        self._assert_equal(response.status_code, HTTP_OK)

    def test_get_post(self):
        """
        Testing post
        """
        response = get_posts(6)  # range 1 - 100

        self._assert_equal(response.status_code, HTTP_OK)

    def test_get_comments(self):
        """
        Testing comments
        """
        response = get_comments()

        self._assert_equal(response.status_code, HTTP_OK)

    def test_get_comment(self):
        """
        Testing comment
        """
        response = get_comments(120)  # range 1 - 500

        self._assert_equal(response.status_code, HTTP_OK)
