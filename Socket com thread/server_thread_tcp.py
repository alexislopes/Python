# Servidor TCP
import socket
from threading import Thread


def conexao(con, cli):
    c = 0
    while True:
        try:
            msg = con.recv(1024)
            if c == 0:
                nomao = str(msg)
                c+=1
            else:
                if not msg: break
                msg =str(msg)
                nomera = nomao.partition("'")
                msgera = msg.partition("'")
            print("{}{}".format(nomao, msg))
        except OSError as err:
            break
    print('Finalizando conexao com {}'.format(nomao))


# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print("Concetado por ", cliente)
    t = Thread(target=conexao, args=(con, cliente,))
    t.start()
