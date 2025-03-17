
import os
from cryptography.fernet import Fernet
#Cryptography is the practice of using codes to protect information so that only intended recipients can read it. 


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 

def load_key():
    if  not os.path.exists("key.key"):
        print("Key file not found! Generating a new one")
        write_key()
    with open("key.key", "rb") as file: 
        return file.read()

key = load_key() 
fer=Fernet(key)

def view():
    if not os.path. exits("passwords.txt"):
        print("No passwords saved yet.")
        return 
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if "|" in data and data.count("|") == 1:
                user, passw = data.split("|")
                try:
                    decrypted_password = fer.decrypt(passw.encode()).decode()
                    print("User:", user, "| Password:", decrypted_password)
                except: 
                    print(f"Could not decrypt password for {user}. Data might be corrupted.")
            else: 
                print("Invalid data")
    
def add():
    name = input('Account Name: ').strip()
    pwd = input('Password: ').strip()

    if not name or not pwd: 
        print("Account name and password cannot be empty.")
        return

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    print("Password saved successfully!!")

#remode(r)-> you can't do anything in remode or just read  the file. 
#write(w)-> over write the file, if the file already exited.
#append(a)-> allow to add something to an exiting file and create a new file, if that file doesn't exit. 

while True: 
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
    continue
