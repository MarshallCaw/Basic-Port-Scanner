# %%
import socket

for port in range(5000, 5005): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("127.0.0.1", port))
    if result == 0:
         print("Port " + str(port) + " is open")
    else:
         print ("Port " + str(port) + " is closed")
    sock.close()



