from multiprocessing import Process
import DB.MySqlHelper as mysql

class GetUrlProcess(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.queue = queue
        self.daemon = True

    def run(self):
        test = mysql.Mysql()
        is_run = True
        while is_run:
            re = test.getAll('select * from reptileUrl where getstatus=%s limit 100', [0])
            for i in re:
                with self.queue.put(i.url):
                    sql = f"update reptileUrl set getstatus=1 where id={i.id}"
                    test.update(sql)
        test.dispose()
        print(re)