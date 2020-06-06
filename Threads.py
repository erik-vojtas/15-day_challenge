import time
import threading
from bs4 import BeautifulSoup, SoupStrainer
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

# start = time.perf_counter()  #start time counter
#
# def do_something(seconds):
#     print(f"Sleeping {seconds} second(s)...")
#     time.sleep(seconds)
#     return f"Done Sleeping...{seconds}"
#
# threads = []
# for _ in range(10): # _ thrownaway variable
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
# # t1 = threading.Thread(target=do_something)
# # t2 = threading.Thread(target=do_something)
# #
# # t1.start()
# # t2.start()
# #
# # t1.join()
# # t2.join()
#
#
# finish = time.perf_counter()  #finish time
#
# print(f'Finished in {round(finish-start, 2)} second(s)')
#
# print("-----------------------------")


# • Write a Python Class that runs as a separate thread and returns the number of URLS referenced by a given website. (Hint: Use Beautifulsoup to parse the HTML)
# • Run n threads concurrently to get the number of links in n different sites.
# • The main program sums up the results from all the threads and displays the total number of links in the given sites.

# sites = [“http://orf.at”, “http://google.com”, ... more)
# start n threads that process all the sites
# sum up the results of the threads that are finished
# print the total number when all the threads have finished execution



list_of_urls = ["http://stackoverflow.com/", "http://orf.at", "http://google.com", "http://bbc.co.uk", "https://www.channelnewsasia.com/news/international", "https://www.bbc.com"]
sum = 0
def getURLs(url):
    global sum
    urlsOfPage = []
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for link in soup.find_all('a'):
        urlsOfPage.append(link.get('href'))
    print(f"URL: {url} has access to {len(urlsOfPage)} URLs")
    sum += len(urlsOfPage)
    return len(urlsOfPage)

start = time()

# processes = []
# with ThreadPoolExecutor(max_workers=10) as executor:
#     for url in list_of_urls:
#         processes.append(executor.submit(getURLs, url))
#
# for task in as_completed(processes):
#     print(task.result())


# threads = []
# counter = 1
# for url in list_of_urls:
#     t = threading.Thread(target=getURLs, args=(url,))
#     t.start()
#     print(f"Thread number {counter} has started.")
#     threads.append(t)
#     counter += 1
#
# c = 1
# for thread in threads:
#     thread.join()
#     print(f"Thread number {c} has finished.")
#     c+=1

for i, url in enumerate(list_of_urls):
    n = i+1
    t = threading.Thread(target=getURLs, args=(url,))
    t.start()
    print(f"Thread {n} has started")
    t.join()
    print(f"Thread {n} has finished")



print(f"Total number of URLs: {sum}.")
print(f'Time taken: {time() - start}')
print("-----------------------------")
