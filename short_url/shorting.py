from _md5 import md5


def create_short_url(url):
    url_hash = md5(url.encode()).hexdigest()[:10]
    return url_hash
