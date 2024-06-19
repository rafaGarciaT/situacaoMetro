import requests
from bs4 import BeautifulSoup

url = "https://www.diretodostrens.com.br/?codigo=2"
headers = {
    "User-Agent": "situacaoMetro/1.0 (+https://github.com/rafaelGarcia1oACienciaDaComputacao/situacaoMetro)"
}

vq_home_request = requests.get('https://www.diretodostrens.com.br/?codigo=2')
vq_home_request.raise_for_status()

vq_home_content = vq_home_request.text

soup = BeautifulSoup(vq_home_content, 'html.parser')
print(soup.title)

table = soup.find("table", class_="table table-hover")
tbody = table.find("tbody")

print(tbody)
