import requests
import time
import concurrent.futures
import threading

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local,"session"):
        thread_local.session = requests.Session()

    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 50) as executor:
        executor.map(download_site,sites)

if __name__ == "__main__":

    sites = [
        "https://realpython.com/python-concurrency/",
        "https://google.com",
    ]*10

    startTime = time.time()
    download_all_sites(sites)
    duration = time.time()-startTime
    print(f"Downloaded {len(sites)} in {duration} seconds")