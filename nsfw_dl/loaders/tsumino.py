"""
Read the license at:
https://github.com/IzunaDevs/nsfw_dl/blob/master/LICENSE
"""
from nsfw_dl import *


class TsuminoRandom:
    """
    Gets a random image from tsumino.
    """
    reqtype = "get"
    data_format = "url"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://www.tsumino.com/Browse/Random", {}, {}

    @staticmethod
    def get_image(data):
        """
        gets an image.
        """
        image = data.find(id="highres").get("href")
        if image is None:
            image = data.find(id="image").get("src")
        return image
