"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl import *


class YandereRandom:
    """
    Gets a random image from yandere.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "https://yande.re/post/random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        image = data.find(id="highres").get("href")
        if image is None:
            image = data.find(id="image").get("src")
        return image


class YandereSearch:
    """
    Gets a random image with a specific tag from yandere.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://yande.re/post.json?tags={args}", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        if data:
            return random.choice(data)['file_url']
        raise NoResultsFound
