from socketIO_client import SocketIO

# Conectando al socket del Servidor
print("Conectando al Servidor...")
socketIO = SocketIO('201.174.122.202',5001)
print("Conectado al Servidor.")

def rutina(*args):
	print(args[0])

socketIO.on('arduino', rutina)
socketIO.wait()