import threading
import requests

def fetch_html(url):
    try:
        response = requests.get(url)
        print(f"HTML content of {url}:\n{response.text}\n")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

def main():
    urls = [
        "https://www.example.com",
        "https://www.google.com"
    ]
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_html, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
main()