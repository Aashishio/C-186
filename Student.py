from tkinter import *
from firebase import firebase
from simplecrypt import encrypt, decrypt

login_window = Tk()
login_window.geometry("400x400")
login_window.config(bg='#AB92BF')

firebase = firebase.FirebaseApplication('https://encryption-91696-default-rtdb.firebaseio.com/', None)
username = ''
yourcode = ''
friendscode = ''
message_text = ''
message_entry = ''
last_value = ''

def sendData():
    global username
    global message_entry
    global yourcode
    message = usrname+':'+message_entry.get()
    cipherCode = encrypt('AIM', message)
    hex_string = cipherCode.hex()
    data = firebase.put('/', yourcode, hex_string)
    print(data)
    getdata()

def getdata():
    global message_text
    global yourcode
    global friendscode
    global last_value
    
    getdata = firebase.get('/', yourcode)
    print(getdata)
    byte_str = bytes.fromhex(getdata)
    original = decrypt('AIM', byte_str)
    print(original)
    
    readable = original.decode('utf-8')
    print(readable)
    message_text.insert(END, readable+'\n')
    
    get_friends_message = firebase.get('/', friendscode)
    if get_friends_message != None:
        byte_str = bytes.fromhex(get_friends_message)
        original = decrypt('AIM', byte_str)
        final_message = original.decode('utf-8')
        if final_message not in last_value:
            message_text.insert(END, final_message+'\n')
            last_value = final_message

def enterRoom():
    global username
    global message_entry
    global yourcode
    global friendscode
    global message_text
    
    username = usrname_entry.get()
    yourcode = your_code_entry.get()
    friendscode = friends_code_entry.get()
    
    message_window = Tk()
    message_window.config(bg='#AFC1D6')
    message_window.geometry("600x500")
    
    message_text = Text(message_window, height=20, width=72)
    message_text.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    message_label = Label(message_window, text="Message " , font = 'arial 13', bg='#AFC1D6', fg="white")
    message_label.place(relx=0.3,rely=0.8, anchor=CENTER)
    
    message_entry = Entry(message_window, font = 'arial 15')
    message_entry.place(relx=0.6,rely=0.8, anchor=CENTER)
    
    btn_send = Button(message_window, text="Send", font = 'arial 13', bg="#D6CA98", fg="black", padx=10, relief=FLAT, command=sendData)
    btn_send.place(relx=0.5,rely=0.9, anchor=CENTER)
    
    message_window.mainloop()
    

username_label = Label(login_window, text="Username : " , font = 'arial 13', bg ='#AB92BF', fg="white")
username_label.place(relx=0.3,rely=0.3, anchor=CENTER)

username_entry = Entry(login_window)
username_entry.place(relx=0.6,rely=0.3, anchor=CENTER)

your_code_label = Label(login_window, text="Your code :  " , font = 'arial 13', bg ='#AB92BF', fg="white")
your_code_label.place(relx=0.3,rely=0.4, anchor=CENTER)

your_code_entry = Entry(login_window)
your_code_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

friends_code_label = Label(login_window, text="Your Friends code :  " , font = 'arial 13', bg ='#AB92BF', fg="white")
friends_code_label.place(relx=0.22,rely=0.5, anchor=CENTER)

friends_code_entry = Entry(login_window)
friends_code_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_start = Button(login_window, text="Start" , font = 'arial 13' , bg="#CEF9F2", fg="black", command=enterRoom, relief=FLAT, padx=10)
btn_start.place(relx=0.5,rely=0.65, anchor=CENTER)

login_window.mainloop()

#https://encryption-91696-default-rtdb.firebaseio.com/