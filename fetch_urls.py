import urllib.request
import json
import re

url = "https://duckduckgo.com/?q=cat+looking+at+city+pixel+art+gif+imgur&t=h_&iar=images&iax=images&ia=images"
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
)

try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    vqd_match = re.search(r'vqd=([\d-]+)', html)
    
    if vqd_match:
        vqd = vqd_match.group(1)
        search_url = f"https://duckduckgo.com/i.js?q=cat+looking+at+city+pixel+art+gif+imgur&o=json&vqd={vqd}"
        search_req = urllib.request.Request(
            search_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        search_response = urllib.request.urlopen(search_req)
        data = json.loads(search_response.read().decode('utf-8'))
        
        for item in data.get('results', [])[:10]:
            print(item.get('image', ''))
except Exception as e:
    print(f"Error: {e}")
