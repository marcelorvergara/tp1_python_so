import os
import pwd
import subprocess
import psutil

from Files import Files
from ProcessTable import ProcessTable


def get_username():
    return pwd.getpwuid(os.getuid())[0]


# Quetão 1
print(get_username())

# Questão 2
# 2.1 Varáveis de ambiente são usadas pelo sistema operacional para armazenar valores que serão
# usados pelos processos e programas
# 2.2 Como obter
# 2.3 Diretório do python
print(os.environ)
for o in os.environ:
    print('variável de ambiente:', o)
    if o == 'PYTHONPATH':
        print('Caminho do diretório python:', os.environ[o])

# 3 PID e GID
print(os.getpid())
print(os.stat(path='/'))

# 4 Caminho absoluto
print(os.path.abspath('main.py'))

# 5 Checar se o arquivo existe
print(os.path.exists('main.py'))
if os.path.isfile('main.py'):
    print('É um arquivo')

# 6 Extensão de um arquivo
arq, arq_ext = os.path.splitext('main.py')
print('A extensão do arquivo:', arq, ' é:', arq_ext)

# 7 Caminho absoluto de um arquivo sem o nome do arquivo
dir, arq = os.getcwd(), 'main.py'
print('O caminho do arquivo é', dir)

# 8 e 9 Quantidade de bytes dos arquivos em um diretório e datas de criação/alteração
files = Files('.')
files.start()

# 10 os.exec* e os.spawn* - diferença
# O comando os.exec* altera o fluxo de um processo que já está em execução. Já o os.spawn* cria um novo processo.

# 11 Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo,
# usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo.
# Feito em linux, por isso não tem notepad
usr_file = os.path.abspath('text_file.txt')
subprocess.call(['gedit', usr_file], stdin=None, stdout=None, stderr=None, shell=False)

# 12 Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o
# módulo ‘subprocess’ de Python. Dê um exemplo de cada.


# 13 Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.
usr_file = os.path.abspath('text_file.txt')
p = subprocess.Popen(['gedit', usr_file]).pid
print("O pid do processo é:", p)

# 14 Explique a principal semelhança e a principal diferença entre os comandos psutil.pids e psutil.process_iter.
# Conforme exemplo abaixo, psutil.pids() só traz os números dos processos que estão rodando.
# Já psutil.process_ites traz uma tulip com outras informações de todos os processo que estão rodando, além
# do seu pid
proid = psutil.pids()
print(proid)
proid2 = psutil.process_iter()
for proc in proid2:
    print(proc)

# 15 Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário,
# o tempo de criação e o uso de memória em KB.
p = ProcessTable(p)
txt = p.start()

# 16 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.
print("Número de núcleos físicos:", psutil.cpu_count(logical=False))
print("Frequência do processador:", round(psutil.cpu_freq().current / 1024, 2), "Ghz")
cpus_proc = psutil.cpu_percent(percpu=True, interval=0.1)
print('--------------')
for p in cpus_proc:
    print(p)

# 17 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o percentual do uso de CPU do computador.
for i in range(20):
    print(psutil.cpu_percent(percpu=False, interval=1))
    print('-------------------------')

# 18 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e quanto de memória de paginação (swap) existem no computador.
virt_mem = psutil.virtual_memory()
total = round(virt_mem.total / pow(2, 30), 1)
print("Total de memória: " + str(total) + " GB")
disponivel = round(virt_mem.available / pow(2, 30), 1)
print("Memória disponível: " + str(disponivel) + "GB")
print("Memória swap: " + str(round(psutil.swap_memory().total / pow(2, 30), 1)) + "GB")

# 19 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível há na partição do sistema (onde o sistema está instalado).
# é linux
disco = psutil.disk_usage("/")
print("Total de disco: " + str(round(disco.total / pow(2, 30), 2)) + " GB")
print("Total de disco em uso: " + str(round(disco.used / pow(2, 30), 2)) + " GB")
print("Total de disco livre: " + str(round(disco.free / pow(2, 30), 2)) + " GB")
print("Percentual de disco em uso: " + str(disco.percent) + " %")

# 20 Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
# o nome do dispositivo,
# o tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
# o total de armazenamento em GB e
# o armazenamento disponível em GB.
partitions = psutil.disk_partitions()
for p in partitions:
    if p.fstype:
        print("O label do disco é:", p.device)
        print("O sistema de arquivos é:", p.fstype)
        print("Total de disco: " + str(round(psutil.disk_usage(p.mountpoint).total / pow(2, 30), 2)) + " GB")
        print("Total de disco livre: " + str(round(psutil.disk_usage(p.mountpoint).free / pow(2, 30), 2)) + " GB")
