import threading
import requests

def fetch_html(url, results):
    try:
        response = requests.get(url)
        results[url] = response.text
    
    except requests.RequestException as e:
        results[url] = f"Error fetching {url}: {e}"

def search_text(url, html_content, keyword):
    if keyword.lower() in html_content.lower():
        print(f'Keyword "{keyword}" found in {url}')
    else:
        print(f'Keyword "{keyword}" NOT found in {url}')

def main():
    urls = [
        "https://www.example.com",
        "https://www.google.com"
    ]
    
    threads = []
    results = {}
    
    for url in urls:
        thread = threading.Thread(target=fetch_html, args=(url, results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    for url, html_content in results.items():
        print()
        keyword = input(f"Enter Keyword you Want to Search in {url}: ")
        search_text(url, html_content, keyword)
main()