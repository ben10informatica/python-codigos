import requests
from bs4 import BeautifulSoup

# URL do site que você quer fazer o scraping
url = 'https://www.bbc.com/news'

# Enviar uma requisição GET para a URL
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos os títulos de artigos
    titles = soup.find_all('h2', class_='title')

    # Imprimir os títulos
    for title in titles:
        print(title.get_text())
else:
    print(f'Falha ao acessar a página. Status code: {response.status_code}')
