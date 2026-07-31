import urllib.request
import os

req1 = urllib.request.Request(
    'https://media.tenor.com/FwB36O167UoAAAAC/cyberpunk-pixel-art.gif',
    headers={'User-Agent': 'Mozilla/5.0'}
)
with urllib.request.urlopen(req1) as response, open('assets/banner-top.gif', 'wb') as out_file:
    out_file.write(response.read())

req2 = urllib.request.Request(
    'https://media.tenor.com/T0b_i8k4qKcAAAAC/pixel-city.gif',
    headers={'User-Agent': 'Mozilla/5.0'}
)
with urllib.request.urlopen(req2) as response, open('assets/banner-bottom.gif', 'wb') as out_file:
    out_file.write(response.read())

print("Downloaded both GIFs successfully!")
