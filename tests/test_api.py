from calls import get_posts, get_comments

HTTP_OK = 200


class TestAPI:
    """
    This tests some API calls
    """
    @staticmethod
    def _assert_equal(a: int, b: int) -> None:
        """ Method to compare two status codes

        Args:
            a (int): actual status code
            b (int): expected status code

        Returns:
            None

        Rises:
            AssertionError
        """
        if a != b:
            raise AssertionError(f'Getting {a} status code instead {b} as response')

    def test_get_posts(self) -> None:
        """
        Testing posts
        """
        response = get_posts()

        self._assert_equal(response.status_code, HTTP_OK)

    def test_get_post(self) -> None:
        """
        Testing post
        """
        response = get_posts(6)  # range 1 - 100

        self._assert_equal(response.status_code, HTTP_OK)

    def test_get_comments(self) -> None:
        """
        Testing comments
        """
        response = get_comments()

        self._assert_equal(response.status_code, HTTP_OK)

    def test_get_comment(self) -> None:
        """
        Testing comment
        """
        response = get_comments(120)  # range 1 - 500

        self._assert_equal(response.status_code, HTTP_OK)
