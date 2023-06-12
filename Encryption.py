from cryptography.fernet import Fernet
import getpass

# Generate a secret key
def generate_sender_key():
    key = Fernet.generate_key()
    with open('Security/key.key', 'wb') as key_file:
        key_file.write(key)

def generate_database_key():
    key = Fernet.generate_key()
    with open('Security/DBkey.key', 'wb') as key_file:
        key_file.write(key)

# Encrypt and save the credentials to a file
def save_sender_credentials():
    email = input("Enter Senders email address:")
    password = getpass.getpass("Enter Senders password: ")

    with open('Security/key.key', 'rb') as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)
    encrypted_email = cipher_suite.encrypt(email.encode())
    encrypted_password = cipher_suite.encrypt(password.encode())

    with open('Emails/credentials.txt', 'wb') as file:
        file.write(encrypted_email + b'\n')
        file.write(encrypted_password)

def save_sender_credentials(email,password):
    with open('Security/key.key', 'rb') as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)
    encrypted_email = cipher_suite.encrypt(email.encode())
    encrypted_password = cipher_suite.encrypt(password.encode())

    with open('Emails/credentials.txt', 'wb') as file:
        file.write(encrypted_email + b'\n')
        file.write(encrypted_password)


def save_database_credentials():
    username = input("Enter database username:")
    password = getpass.getpass("Enter Senders password: ")
    host = input("Enter database host ip:")
    database = input("Enter database name:")

    with open('Security/DBkey.key', 'rb') as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)
    encrypted_email = cipher_suite.encrypt(username.encode())
    encrypted_password = cipher_suite.encrypt(password.encode())
    encrypted_host = cipher_suite.encrypt(host.encode())
    encrypted_database = cipher_suite.encrypt(database.encode())


    with open('Emails/DBcredentials.txt', 'wb') as file:
        file.write(encrypted_email + b'\n')
        file.write(encrypted_password + b'\n')
        file.write(encrypted_host + b'\n')
        file.write(encrypted_database)

# Decrypt and read the credentials from the file
def read_sender_credentials():
    with open('Security/key.key', 'rb') as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)

    with open('Emails/credentials.txt', 'rb') as file:
        encrypted_email = file.readline().strip()
        encrypted_password = file.readline().strip()

    email = cipher_suite.decrypt(encrypted_email).decode()
    password = cipher_suite.decrypt(encrypted_password).decode()

    return email, password


def read_database_credentials():
    with open('Security/DBkey.key', 'rb') as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)

    with open('Emails/DBcredentials.txt', 'rb') as file:
        encrypted_email = file.readline().strip()
        encrypted_password = file.readline().strip()
        encrypted_hostname = file.readline().strip()
        encrypted_database = file.readline().strip()
    email = cipher_suite.decrypt(encrypted_email).decode()
    password = cipher_suite.decrypt(encrypted_password).decode()
    hostname = cipher_suite.decrypt(encrypted_hostname).decode()
    database = cipher_suite.decrypt(encrypted_database).decode()
    return email, password, hostname, database

#generate_database_key()
#save_database_credentials()
#print(read_database_credentials())