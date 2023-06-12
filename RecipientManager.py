def debug_get_recipients():
    with open('Emails/Recipients.txt', 'r') as file:
        emails = file.readlines()
    return emails

def get_emails():
    with open('Emails/Recipients.txt', 'r') as file:
        emails = [line.strip() for line in file.readlines()]
    return emails

def add_recipient(insertion_email):
    with open('Emails/Recipients.txt', 'r') as file:
        emails = file.readlines()

    exists = False
    for index in range(len(emails)):
        if(emails[index].strip().__eq__(insertion_email)):
            exists = True

    if(not exists):
        with open('Emails/Recipients.txt', 'a') as file:
            file.write(insertion_email+'\n')
        print("Successfully added "+ insertion_email + " to recipient list")
    else:
        print("email already exists")


def remove_recipient(removal_email):
    with open('Emails/Recipients.txt', 'r') as file:
        emails = file.readlines()

    removed = False
    for index in range(len(emails)):
        if(emails[index].strip().__eq__(removal_email)):
            del emails[index]
            removed = True
            with open('Emails/Recipients.txt', 'w') as file:
                file.writelines(emails)
            break
    if(removed):
        print("Successfully removed " + removal_email + " from the Recipient list")
    else:
        print(removal_email + " does not exist in Recipient list")
