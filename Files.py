import threading, os, time


def busca_arquivos(dir_var):
    soma = 0
    total_arq = 0
    total_dir = 0
    lista_dir = [dir_var]
    while lista_dir:
        dir_atual = lista_dir[0]
        time.sleep(0.1)
        l = []
        try:
            l = os.listdir(dir_atual)
        except:
            pass
        for i in l:
            arq = os.path.join(dir_atual, i)
            if os.path.isfile(arq):
                print('O arquivo:', arq, ' possui o tamanho de:', os.stat(arq).st_size, ' bytes')
                print('O arquivo:', arq, ' possui a data de criação de:', time.ctime(os.path.getmtime(arq)), ' bytes')
                print('O arquivo:', arq, ' possui a data de modificação de:', time.ctime(os.path.getctime(arq)), ' bytes')
                soma += os.stat(arq).st_size
                total_arq += 1
        lista_dir.remove(dir_atual)
    return soma, total_arq, total_dir


class Files(threading.Thread):
    global entry

    def get_text(self,dir1):
        soma, total_arq, total_dir = busca_arquivos(dir1)
        print('Total de bytes: ' + str(soma))
        print('Total de MB: ' + str(round(soma / 2 ** 20, 2)))
        print('Total de arquivos: ' + str(total_arq))
        print('Total de dir: ' + str(total_dir))

    def __init__(self, directory):
        super().__init__()
        self.get_text(directory)


