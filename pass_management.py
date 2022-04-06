from cryptography.fernet  import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:     #wb = write in bytes
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key) 


def View():
    m_pass = input("Enter the master password: ")
    if m_pass=="master":
        with open('data.txt','r') as f:            #a = append mode
            for i in f.readlines():
                data = i.rstrip()
                v_name,v_pass = data.split(" | ")
                print("Name:",v_name," | Password:",fer.decrypt(v_pass.encode()).decode())
    else:
        print("Invalid master password!")
        with open('data.txt','r') as f:            #a = append mode
            for i in f.readlines():
                data = i.rstrip()
                v_name,v_pass = data.split(" | ")
                n=len(fer.decrypt(v_pass.encode()).decode())
                n_pass=""
                for j in range(0,n):
                    n_pass+="*"    
                print("Name:",v_name," | Password:",n_pass)

def Add():
    u_name = input("Enter name: ")
    u_pass = input("Enter password: ")

    with open('data.txt','a') as f:            #a = append mode
        f.write(u_name + " | " + fer.encrypt(u_pass.encode()).decode() + "\n")


while True:
    mode = input("1.)Add a password\n2.)View the passwords\n3.)EXIT\nEnter choice: ")
    
    if mode == "1":
        Add()
    
    elif mode == "2":
        View()
    
    elif mode == "3":
        break
    
    else:
        print("INVALID INPUT!")
        continue




