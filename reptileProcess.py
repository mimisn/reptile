from multiprocessing import Process

import requests
import re
import time
import DB.MySqlHelper as mysql
from logs.logTest import LogsHandler

logger = LogsHandler().getLogger()
class GetUrlProcess(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.queue = queue
        self.daemon = True

    def run(self):
        is_run = True
        conn = None
        while is_run:
            try:
                conn = mysql.Mysql()
                res = conn.getAll('select * from reptileUrl where  reptilestatus=0 limit 100')
                if res is not False:
                    for i in res:

                            #print("whiat1..........................")
                            self.queue.put(i["url"])
                            #print("whiat............................")
                            sql = f"update reptileUrl set getstatus=1 where id={i['id']}"
                            count = conn.update(sql)
                            logger.info("push:"+i["url"])
                            if count:
                                logger.info("update:"+sql+"   count:"+str(count))
            except Exception as e:
                logger.error(e)
            finally:
                conn.dispose()
                time.sleep(10)

class ReptileProcess(Process):
    def __init__(self, queue, headers=None, proxies=None, verify=False):
        Process.__init__(self)
        self.queue = queue
        self.daemon = True
        self.headers = headers
        self.proxies = proxies
        self.verify = verify

    def run(self):
        conn = None
        is_run = True
        suffix = ['png', 'ico', 'svg', 'jpg', 'css', 'js']
        mail_suffix = ['com', 'cn', 'net', 'de', 'fr', 'jp', 'lk', 'in', 'nz', 'ru', 'hk', 'tw', 'sg', 'il', 'fm', 'ar', 'mk', 'gn', 'zm', 'mn', 'zw']
        is_suffix = False
        while is_run:
            #print("get====whiat1..........................")
            res = self.queue.get()
            #print("get======whiat1..........................")
            try:
                conn = mysql.Mysql()
                logger.info("reptile:"+res)
                r = requests.get(res, timeout=2, headers=self.headers, proxies=self.verify,
                             verify=self.verify)
                r.encoding = "utf-8"
                if r.status_code == requests.codes.ok:
                    urlPattern = re.compile(r'href="([a-zA-z]+://[^\s]*)"')
                    url = re.findall(urlPattern, r.text)
                    mailPattern = re.compile(r'[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?')
                    mail = mailPattern.findall(r.text)
                    #print("mail", mail)
                    for u in url:
                        reptlieSuffix = u.split('.')
                        if reptlieSuffix:
                            if reptlieSuffix[-1] in suffix:
                                is_suffix = True
                            else:
                                is_suffix = False
                        if len(u) <= 255 and is_suffix is False:
                            qq = conn.getAll("SELECT * FROM reptileUrl where url=%s", [u])
                            if qq is False:
                                conn.insertOne("INSERT INTO reptileUrl ( url) VALUES (%s)", [u])
                                logger.info("INSERT INTO:"+u)
                            else:
                                #logger.info("repeat url:" + u)
                                pass
                    for m in mail:
                        zhPattern = re.compile(u'[^\x00-\xff]+')
                        match = zhPattern.split(m)
                        if match:
                            for tex in match:
                                if '@' in tex:
                                    mailSuffix = tex.split('.')
                                    if mailSuffix[-1] in mail_suffix:
                                        repeatMail = conn.getAll("SELECT * FROM mail where mail=%s", [tex])
                                        if repeatMail is False:
                                            conn.insertOne("INSERT INTO mail ( mail) VALUES (%s)", [tex])   #[match[0]])
                                            logger.info("INSERT INTO:"+ tex)
                        else:
                            conn.insertOne("INSERT INTO mail ( mail) VALUES (%s)", [m])
                            logger.info("INSERT INTO:" + m)
            except Exception as e:
                logger.error(e)
            finally:
                conn.update("update reptileUrl set reptilestatus=1 where url=%s", res)
                logger.info("UPDATE REPTILEURL:" + res)
                conn.dispose()