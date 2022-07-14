from socketIO_client import SocketIO

# Conectando al socket del Servidor
print("Conectando al Servidor...")
socketIO = SocketIO('ip.del.ser.vidor',5001)
print("Conectado al Servidor.")

def rutina(*args):
	print(args[0])

socketIO.on('arduino', rutina)
socketIO.wait()
