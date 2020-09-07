# %%
import requests
from bs4 import BeautifulSoup
from IPython.display import Image

URL = 'https://www.pagina12.com.ar/'
p12= requests.get(URL)

p12.status_code

s = BeautifulSoup(p12.text,'lxml')
 
secciones = s.find('ul',attrs={'class': 'hot-sections'}).find_all('li')
seccion = secciones[0]
#print(seccion.a.get_text())

seccion.a.get('href')
# %%
links_secciones = [seccion.a.get('href') for seccion in secciones]
print(links_secciones)

sec = requests.get(links_secciones[0])
# print(type(sec))
#print(sec.text)

s_seccion = BeautifulSoup(sec.text, 'lxml')

article_list = s_seccion.find('ul',attrs={'class', 'article-list'})
#print(article_list)

def news_section(soup):
    """Función que recibe un objeto soup de una categoría determinada, 	 
     y devuelve los links de todas las noticias pertenecientes a ella"""

    lista_notas =[]
    # Get featured article link
    featured_article = soup.find('div', attrs={'class': 'featured-article__container'})
    if featured_article:
        lista_notas.append(featured_article.a.get('href'))
    
    # Get articles links in the list
    articles = soup.find('ul', attrs={'class': 'article-list'})
    for article in articles.find_all('li'):
        if article.a:
            lista_notas.append(article.a.get('href'))
       
    return lista_notas
# %%
lista_notas=news_section(s_seccion)
newline = ('\n') 
# url_nota = lista_notas[0]
# url_nota = 'https://www.pagina12.com.ar/288931-canje-de-deuda-alberto-fernandez-hizo-la-gran-nestor'
# print(f'Link de la noticia: {newline} {url_nota}')

def get_content(url_nota):
    """Función que recibe una url y devuelve el contenido de todas la nota"""
    try: 
        nota = requests.get(url_nota)
        if nota.status_code == 200:
            s_nota = BeautifulSoup(nota.text,'lxml')
            #Get title
            titulo = s_nota.find('h1', attrs={'class':'article-title'}).text
            # print(f'Titulo:{newline} {titulo.text}')
            #Get Date
            fecha = s_nota.find('span',attrs={'pubdate':'pubdate'}).get('datetime')
            # print(f'Fecha: {date_note}{newline}')
            #Copete
            try:
                copete = s_nota.find('div', attrs={'class': 'article-summary'}).text
                # print(f'Copete :{copete.text}{newline}')          
            except:
                copete = None
            
            #Volanta
            try:
                volanta = s_nota.find('h2',attrs={'class':'article-prefix'}).text
            # print(f'Volanta: {volanta.text}{newline}')
            except:
                volanta= None
            #Cuerpo
            cuerpo = s_nota.find('div', attrs={'class':'article-text'}).find_all('p')
            articulo_texto = ''
            for parrafo in cuerpo:
                articulo_texto += parrafo.text
            
            # print(f'Cuerpo: {articulo_texto} ')
            #Autor
            try:
                autor = s_nota.find('div', attrs={'class':'article-author'}).a.text
                # print(f'Author : {autor.text}{newline}')
            except:
                autor = None
           
    except Exception as e:
        print('Error')
        print(e)
        print('/n')
    
    content ={'title': titulo,'fecha': fecha,'copete': copete,'volanta': volanta,'cuerpo': articulo_texto,'autor': autor}

    return content

def get_image(url_nota):
    """Función que recibe una url y devuelve la imagen de la nota"""
    nota = requests.get(url_nota)
    s_nota = BeautifulSoup(nota.text,'lxml')
    try:
        media = s_nota.find('div', attrs={'class','article-main-media-image'})
        imagenes = media.find_all('img')
        print(imagenes[-1].get('data-src'))
        if len(imagenes) > 0:
            img_src = imagenes[-1].get('data-src')
            img_req = requests.get(img_src)
            img_content = img_req.content
        # print(f'Link de la imagen: {img_src}')
        # display(Image(img_req.content))
    except:
        print('No se encontró media')
        img_content = None
    return img_content
# %%
lista_notas=news_section(s_seccion)
url_nota = lista_notas[0]
# url_nota = 'https://www.pagina12.com.ar/288931-canje-de-deuda-alberto-fernandez-hizo-la-gran-nestor'
contenido = get_content(url_nota)
imagen = get_image(url_nota)
# display(Image(imagen))
# %%
links_secciones
# %%
notas =[]
for link in links_secciones:
    try:
        r = requests.get(link)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text,'lxml')
            notas.extend(news_section(soup))
        else:
            print('No se pudo obtener la seccion',link)
    except:
        print('No se pudo obtener la seccion',link)

# %%
notas
# %%
data = []
for i,nota in enumerate(notas):
    print(f'Scrapeando nota {i+1}/{len(notas)}')
    data.append(get_content(nota))

# %%
import pandas as pd
df = pd.DataFrame(data)
df.head()
# %%
df.to_csv('NotasPagina12.csv')
# %%
