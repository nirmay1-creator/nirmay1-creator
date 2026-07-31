import urllib.request
import urllib.parse
import json
import re

url = "https://duckduckgo.com/?q=pixel+art+cat+city+gif+github&t=h_&iar=images&iax=images&ia=images"
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
)

try:
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    vqd_match = re.search(r'vqd=([\d-]+)', html)
    
    if vqd_match:
        vqd = vqd_match.group(1)
        search_url = f"https://duckduckgo.com/i.js?q=pixel+art+cat+city+gif+github&o=json&vqd={vqd}"
        search_req = urllib.request.Request(
            search_url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Accept': 'application/json'
            }
        )
        search_response = urllib.request.urlopen(search_req)
        data = json.loads(search_response.read().decode('utf-8'))
        
        for item in data.get('results', []):
            img_url = item.get('image', '')
            if img_url.endswith('.gif'):
                print(f"Found GIF: {img_url}")
                
                # Download it
                try:
                    gif_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                    gif_res = urllib.request.urlopen(gif_req, timeout=5)
                    with open('assets/pixel-cat-real.gif', 'wb') as f:
                        f.write(gif_res.read())
                    print("Downloaded successfully!")
                    break
                except Exception as e:
                    print(f"Failed to download {img_url}: {e}")
    else:
        print("Could not find vqd.")
except Exception as e:
    print(f"Error: {e}")
