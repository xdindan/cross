import requests
from bs4 import BeautifulSoup
import time
import random

url = "https://app.viralsweep.com/vrlswp/widget/d8dc16-168142"
params = {
    "rndid": "168142_949404",
    "framed": "1",
    "vs_eid_hash": "",
    "ref": "https://www.cros.world/",
    "source_url": "",
    "hsh": "",
    "hash": ""
}

response = requests.get(url, params=params)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('a', attrs={'data-aid': True})
    
    with open("email.txt", "r") as email_file:
        emails = email_file.readlines()

    for email in emails:
        email = email.strip()

        for link in links:
            data_aid = link['data-aid']
            print("Mengirim permintaan POST dengan data-aid:", data_aid)

            post_url = "https://app.viralsweep.com/promo/bonus"
            headers_post = {
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": url,
                "Cookie": f"vs_dem_168142=a%3A1%3A%7Bs%3A5%3A%22email%22%3Bs%3A{len(email)}%3A%22{email}%22%3B%7D;"
            }

            data_post = {
                "aid": data_aid,
                "type": "website",
                "pid": "168142",
                "extra": "",
                "eid_hash": ""
            }

            response_post = requests.post(post_url, headers=headers_post, data=data_post, allow_redirects=False)

            if response_post.status_code == 200:
                print("Sukses")
            else:
                print("Gagal")

else:
    print("Gagal mengambil halaman. Status Kode:", response.status_code)
