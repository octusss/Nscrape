import threading
import requests
from urllib.parse import urlparse
import time

# Global list to store all proxies
all_proxies = []

def download_proxies(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            print(f"Failed to download proxies from {url}. Status code: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Error downloading proxies from {url}: {e}")
        return []

def remove_duplicates(proxies):
    return list(set(proxies))

def save_proxies_to_file(filename):
    unique_proxies = remove_duplicates(all_proxies)
    with open(filename, 'w') as file:
        for proxy in unique_proxies:
            file.write(proxy + '\n')
    print("Removing duplicate proxies...")
    time.sleep(1)
    print(f"All unique proxies saved to {filename}")

def download_and_save(url):
    proxies = download_proxies(url)
    all_proxies.extend(proxies)

def main():
    print("Nscrape")
    proxy_type = input("Enter the type of proxies you want to download (socks5/socks4/http): ").lower()
    
    if proxy_type == "socks5":
        urls = [
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
            "https://api.openproxylist.xyz/socks5.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://openproxylist.xyz/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks5",
            "https://www.my-proxy.com/free-socks-5-proxy.html"
            # Add more URLs here
        ]
    elif proxy_type == "socks4":
        urls = [
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
            "https://api.openproxylist.xyz/socks4.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&simplified=true",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://openproxylist.xyz/socks4.txt",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://www.my-proxy.com/free-socks-4-proxy.html"
            # Add more URLs here
        ]
    elif proxy_type == "http":
        urls = [
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&simplified=true",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://openproxylist.xyz/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
]
    else:
        print("Invalid proxy type. Please enter 'socks5' or 'socks4' or 'http'.")
        return

    threads = []
    for url in urls:
        thread = threading.Thread(target=download_and_save, args=(url,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Save all proxies to a single file
    save_proxies_to_file(f"{proxy_type}.txt")

if __name__ == "__main__":
    main()
