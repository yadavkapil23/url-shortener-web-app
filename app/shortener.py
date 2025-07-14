import requests
import hashlib

def shorten_url(long_url: str) -> str:
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    return requests.get(api_url).text

def generate_code(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:6]
