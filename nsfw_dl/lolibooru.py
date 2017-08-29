# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2016-2017 AraHaan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from bs4 import BeautifulSoup

from .errors import *
from .tags import *


__all__ = ['lolibooru_random', 'lolibooru_search']


async def lolibooru_random(session):
    """Returns a random image from lolibooru."""
    try:
        query = "https://lolibooru.moe/post/random/"
        page = await session.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="image").get("src")
        image = image.replace(' ', '%20')
        return image
    except Exception as e:
        str(e)
        return None


async def lolibooru_search(searchtags, session):
    """Returns a specific image from lolibooru."""
    if isinstance(searchtags, str):
        try:
            query = "https://lolibooru.moe/post/index.json?tags=" + searchtags
            page = await session.get(query)
            json = await page.json()
            if not json == []:
                return json
            else:
                raise NoResultsFound('No images found.')
        except Exception as e:
            str(e)
            return None
    else:
        return -1
