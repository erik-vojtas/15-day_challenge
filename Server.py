import socket
import random

random_num = random.randint(1,10)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object

server_socket.bind(("localhost", 8000)) # wait for a client, port 2800

server_socket.listen(1) # wait for one client
print ( "Waiting for client to connect")

client_socket, address = server_socket.accept()
client_socket.sendall("Hi, lets' play a game! Guess a number from 1 to 10.".encode("utf-8"))
print ( "Received connection from ", address)
lives = 5
while lives != 0:
    message_from_client = client_socket.recv(1024)
    if int(message_from_client.decode("utf-8")) < int(random_num):
        lives -= 1
        client_socket.sendall(f"Your guess was lower than lucky number. You have {lives} life/lives left.".encode("utf-8"))

    elif int(message_from_client.decode("utf-8")) > int(random_num):
        lives -= 1
        client_socket.sendall(f"Your guess was higher than lucky number. You have {lives} life/lives left".encode("utf-8"))

    else:
        client_socket.sendall(f"You won!".encode("utf-8"))


client_socket.close()