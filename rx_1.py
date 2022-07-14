from socketIO_client import SocketIO

IP_SERVER = 'ip.del.ser.vidor'
# Conectando al socket del Servidor
print("Conectando al Servidor...")
socketIO = SocketIO(IP_SERVER,5001)
print("Conectado al Servidor.")

def rutina(*args):
	print(args[0])

socketIO.on('arduino', rutina)
socketIO.wait()
