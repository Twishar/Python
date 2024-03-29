from Lutts.Processes.sockets.socket_preview import server, client
import sys, os
from threading import Thread

mode = int(sys.argv[1])
if mode == 1:                       #запустить сервер в этом процессе
    server()

elif mode == 2:                     #запустить клиента в этом процессе
    client('client:process = %s' % os.getpid())

else:
    for i in range(5):
        Thread(target=client, args=('client:thread=%s' % i)).start()