from socketIO_client import SocketIO
import serial
import time

print("Comenzando...")
socketIO = SocketIO('201.174.122.202', 5001)
print("Conectado al servidor.")

print("Conectando al Arduino...")
arduino=serial.Serial('COM6',9600, timeout = 3.0)
arduino.isOpen()
print("Conectado al Arduino.")
while True:
    arduino.write("r".encode())
    sig = arduino.readline().strip()
    if not sig:
        continue
    #sig = int(sig)
    sig = float(sig)
    #print(sig)
    socketIO.emit("arduino",sig)
    time.sleep(0.15)

arduino.close()
