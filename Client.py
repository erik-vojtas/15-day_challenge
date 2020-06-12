import socket

# Connecting to a local server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8000))
# msg = b"Hi Server"
# print ("Client:", msg)
# s.send(msg)
message_from_server = client_socket.recv(1024)
print("Server:", message_from_server)

end_of_the_game = False
while end_of_the_game != True: #repeat it until the end of the game equals to True
    user_input = input("Let's try: ")
    client_socket.send(str.encode(user_input))
    print("Client:", user_input)
    response = client_socket.recv(1024) #receive response
    print(response.decode('utf-8')) #print receiving message from server
    if len(response.decode('utf-8')) > 10:
        end_of_the_game = False
    else:
        end_of_the_game = True
client_socket.close()