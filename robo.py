import requests
from bs4 import BeautifulSoup

# URL alvo
url = "https://pt.wikipedia.org/wiki/Python"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("🤖 Robô (disfarçado) indo até a Wikipedia...")

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    print("✅ Acesso permitido! O disfarce funcionou.")
    soup = BeautifulSoup(resposta.content, 'html.parser')

    titulo = soup.find('h1').text

    print("-" * 30)
    print(f"TÍTULO DA PÁGINA: {titulo}")
    print("-" * 30)
else:
    print(f"❌ Ainda bloqueado. Código de erro: {resposta.status_code}")
