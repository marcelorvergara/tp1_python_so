import threading
import time
from tabulate import tabulate
import psutil


def criar_titulo():
    titulo = ["PID", "# threads", "Criação", "T. Usu.", "T. Sis.", "Mem. (%)", "RSS", "VMS", "Executável"]
    return titulo


class ProcessTable(threading.Thread):

    def __init__(self, p):
        super().__init__()
        self.tabela = []
        try:
            txt = []
            p = psutil.Process(p)
            txt.append(p)
            txt.append(p.num_threads())
            txt.append(time.ctime(p.create_time()))
            txt.append(p.cpu_times().user)
            txt.append(round(p.cpu_times().system, 2))
            txt.append(round(p.memory_percent(), 2))
            rss = round((p.memory_info().rss / (2 ** 20)), 2)
            txt.append(rss)
            vms = round((p.memory_info().vms / (2 ** 20)), 2)
            txt.append(vms)
            txt.append(p.exe())
            self.tabela.append(criar_titulo())
            self.tabela.append(txt)
            print(tabulate(self.tabela))
        except:
            pass
