import requests
from bs4 import BeautifulSoup


def pegar_dolar():
    url = "https://www.google.com/search?q=dolar+hoje"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Finge ser um navegador

    print("Acessando o Google...")
    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.content, 'html.parser')
        # O Google costuma colocar o valor numa classe específica,
        # mas ela muda. Vamos tentar pegar de um jeito genérico para teste:
        print("Busca realizada! Tentando encontrar valor...")

        # Esse código tenta achar o texto grande do valor
        # Nota: O Google muda isso constatemente, isso é só um teste educacional
        texto = soup.text
        if "Brasileiro" in texto:
            print("Consegui ler a página do Google!")
            print("Agora o desafio é filtrar o número exato no meio de tanto código.")
        else:
            print("A página carregou, mas veio diferente do esperado.")
    else:
        print("Bloqueado pelo Google!")


pegar_dolar()
