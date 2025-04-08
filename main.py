from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import webbrowser
import threading

app = Flask(__name__, template_folder='apt')

def add_protocol(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return f'https://{url}'
    return url

def extract_links(url):
    url = add_protocol(url)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        link_list = []
        for link in links:
            href = link.get('href')
            full_url = urljoin(url, href)
            if full_url.startswith('http') or full_url.startswith('ftp') or full_url.startswith('www'):
                link_list.append(full_url)
        return link_list
    else:
        return []

@app.route('/', methods=['GET', 'POST'])
def home():
    links = []
    if request.method == 'POST':
        url = request.form['url']
        links = extract_links(url)
    return render_template('index.html', links=links)

def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
