"""
CloudBotsBiz
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def MyRoot(app):
    
    def send_message(self):
        print('\nSending..')
        nickname_text = text2.value
        message_text = text4.value
        client.send(f"{nickname_text}:{message_text}".encode('utf-8'))
        print("\nSent!")
    
    def connect_to_server(self):
        print('\nConnecting')
        if text2.value != "":
            client.connect((text1.value, 9999))
            message = client.recv(1024).decode('utf-8')
            if message == "NICK":
                client.send(text2.value.encode('utf-8'))

                # thread = threading.Thread(target=receive)
                # thread.start()

    def receive():
        stop = False
        chat_text = text3.value
        while not stop:
            try:
                print("\nUser connecting..")
                message = client.recv(1024).decode('utf-8')
                chat_text += message + "\n"
                print("\nUser Connected!")
                # main_box.remove(btton)
                # box1.remove(lab1)
            except:
                print("ERROR: Something went wrong")
                client.close()
                stop = True

    main_box = toga.Box(id='connection_grid')
    box1 = toga.Box()
    box2 = toga.Box()
    box3 = toga.Box()
    box4 = toga.Box()
    box5 = toga.Box()
    box6 = toga.Box()

    #box1
    lab1 = toga.Label("Server iP")
    lab1.style.update(flex = 0)
    text1 = toga.TextInput(id = 'ip_text', placeholder = "192.168.1.1")
    text1.style.update(flex = 0, width = 100, padding_top = 5, padding_bottom = 5,padding_right = 1)
    box1.add(lab1, text1)
    box1.style.update(direction = COLUMN)
    #box2 
    lab2 = toga.Label("Nickname")
    lab2.style.update(flex = 0)
    text2 = toga.TextInput(id = 'nickname_text', placeholder = "Deja")
    text2.style.update(flex = 1, padding_top = 5, padding_bottom = 5, padding_left = 1)
    box2.add(lab2, text2)
    box2.style.update(direction = COLUMN)
    
    #box3 b1+b2
    box3.add(box1)
    box3.add(box2)
    box3.style.update(flex = 0, width = 1, height = 50, direction = ROW)
    main_box.add(box3)

    #button
    btton = toga.Button("Connect", id = 'connect_btn', on_press = connect_to_server)
    btton.style.update(width=100, padding_bottom = 25)
    main_box.add(btton)

    #box4
    lab3 = toga.Label("Chat History")
    lab3.style.update(flex = 0)
    text3 = toga.MultilineTextInput(id = 'chat_text', placeholder = "")
    text3.style.update(flex = 1, height = 250, padding_top = 5, padding_bottom = 10,padding_right = 5)
    box4.add(lab3, text3)
    box4.style.update(direction = COLUMN)
    #box5 
    lab4 = toga.Label("Your Message")
    lab4.style.update(flex = 0)
    text4 = toga.TextInput(id = 'message_text', placeholder = "Start typing..")
    text4.style.update(flex = 1, padding_top = 5, padding_bottom = 10, padding_left = 5)
    box5.add(lab4, text4)
    box5.style.update(direction = COLUMN)
    
    #box6 b4+b5
    box6.add(box4)
    box6.add(box5)
    box6.style.update(flex = 1, direction = COLUMN)
    main_box.add(box6)

    #button2
    btton2 = toga.Button("Send", id = 'send_btn', on_press = send_message)
    main_box.add(btton2)

    main_box.style.update(width = 400, direction = COLUMN)

    ip_text = text1.value
    nickname_text = text2.value
    connect_btn = btton
    chat_text = text3.value
    message_text = text4.value
    send_btn = btton2
    connection_grid = main_box

    return main_box

def main():
    return toga.App(startup=MyRoot)

if __name__ == '__main__':
    main().main_loop()
