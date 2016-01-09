import requests

p = requests.get('https://pic4.zhimg.com/953bf0a87f045858dd8c9cb9cef0883b_b.jpg')
with open('/home/jason/python/pic.jpg', 'wb') as f:
    f.write(p.content)
