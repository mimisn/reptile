from multiprocessing import Process, Queue
from reptileProcess import GetUrlProcess,ReptileProcess

proxies = {
  "http": "http://203.202.248.35:8080",
  "http": "http://109.172.51.162:35783",
}

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
}


if __name__ == '__main__':
    queue = Queue(100)
    getProcess = GetUrlProcess(queue)
    reptileProcess = ReptileProcess(queue=queue, headers=headers, proxies=proxies, verify=False)
    reptileProcess1 = ReptileProcess(queue=queue, headers=headers, proxies=proxies, verify=False)
    reptileProcess2 = ReptileProcess(queue=queue, headers=headers, proxies=proxies, verify=False)
    reptileProcess3 = ReptileProcess(queue=queue, headers=headers, proxies=proxies, verify=False)
    reptileProcess4 = ReptileProcess(queue=queue, headers=headers, proxies=proxies, verify=False)
    getProcess.start()
    reptileProcess.start()
    reptileProcess1.start()
    reptileProcess2.start()
    reptileProcess3.start()
    reptileProcess4.start()
    while True:
        getProcess.is_alive()
        reptileProcess.is_alive()
        reptileProcess1.is_alive()
        reptileProcess2.is_alive()
        reptileProcess3.is_alive()
        reptileProcess4.is_alive()