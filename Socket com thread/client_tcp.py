# Cliente TCP
import socket
# Endereco IP do Servidor
SERVER = '172.16.13.5'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print('Para sair use /sair')
print('Digite seu nome: ')
msg = input()

while msg != '/sair':
    if msg != '/sair':
        tcp.sendto(msg.encode(), dest)
        msg = input()
tcp.close()
