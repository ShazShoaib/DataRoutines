import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading
import os.path

import EmailManager
import Encryption
import RecipientManager

checked_recipients = []
checkboxes = []
check_labels = []
recipient_list = RecipientManager.get_emails()


def get_checked_recipients():
    recipient_list = RecipientManager.get_emails()
    checked_recipients.clear()
    for i in range(len(checkboxes)):
        if checkboxes[i].instate(['selected']):
            checked_recipients.append(recipient_list[i])
    return checked_recipients


def update_sender():  # update the email and password of sender
    pass_coded = ""
    for n in range(len(updated_password.get())):
        pass_coded = pass_coded + "*"
    print("Updated Email")
    print("Email: ", updated_email.get())
    print(" Password: ", pass_coded)
    Encryption.save_sender_credentials(updated_email.get(), updated_password.get())
    email_window.withdraw()


def send_emails():  # to send emails to selected recipients
    EmailManager.subject = get_subject()
    print("Subject: ", get_subject())
    EmailManager.message = get_text()
    print("Message: ", get_text())
    print(get_checked_recipients())
    sender = threading.Thread(target=EmailManager.Send_Emails, args=(get_checked_recipients(),), daemon=True)
    sender.start()


def add_recipient():  # to add a new recipient to the list
    print('P', new_recipient.get())
    RecipientManager.add_recipient(new_recipient.get())
    items = RecipientManager.get_emails()
    destroy_check_list()
    check_list(items)
    add_window.withdraw()


def remove_recipients():  # to remove all selected recipients from the list
    print("Removing")
    checked_recipients = get_checked_recipients()
    for recipient in checked_recipients:
        RecipientManager.remove_recipient(recipient)
    items = RecipientManager.get_emails()
    destroy_check_list()
    check_list(items)
    print(checked_recipients)


def get_text():
    text = text_box.get("1.0", "end-1c")
    return text


def get_subject():
    subject = subject_box.get("1.0", "end-1c")
    return subject


image_path = ""
def select_image():
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Images", "*.jpg *.bmp *.jpeg *.png *.raw"), ("all files", "*.*")))
    EmailManager.image_path = image_path
    img_path_label.configure(text=os.path.basename(image_path))
    print("Selected Image:", image_path)


file_path = ""
def select_file():
    file_path = filedialog.askopenfilename(title="Select attachment")
    EmailManager.file_path = file_path
    file_path_label.configure(text=os.path.basename(file_path))
    print("Selected File:", file_path)


def init_change_email_window():
    email_window.title("Change email")
    email_window.geometry("300x170")
    label = tk.Label(email_window, text="Enter Sender Credentials")
    email_label = tk.Label(email_window, text="Email:", anchor="e")
    password_label = tk.Label(email_window, text="Password:", anchor="e")
    email_field = tk.Entry(email_window, textvariable=updated_email)
    password_field = tk.Entry(email_window, show="*", textvariable=updated_password)
    label.place(x=50, y=10, height=25, width=200)
    email_label.place(x=10, y=40, height=25, width=55)
    email_field.place(x=65, y=40, height=25, width=200)
    password_label.place(x=10, y=80, height=25, width=55)
    password_field.place(x=65, y=80, height=25, width=200)
    Update_button = tk.Button(email_window, text="Update", command=update_sender)
    Update_button.place(x=100, y=120, height=30, width=100)


def change_email_window():
    email_window.deiconify()


def init_add_recipient_window():
    add_window.title("Add New Recipient")
    add_window.geometry("300x120")
    label = tk.Label(add_window, text="Enter Recipient Email")
    email_label = tk.Label(add_window, text="Email:", anchor="e")
    email_field = tk.Entry(add_window, textvariable=new_recipient)
    Add_button = tk.Button(add_window, text="Add", command=add_recipient)
    label.pack()
    email_label.place(x=10, y=40, height=25, width=55)
    email_field.place(x=65, y=40, height=25, width=200)
    Add_button.place(x=110, y=80, height=30, width=80)


def add_recipient_window():
    add_window.deiconify()


def destroy_check_list():
    for checkbox in checkboxes:
        checkbox.destroy()
    for check_label in check_labels:
        check_label.destroy()


def check_list(items):
    checkboxes.clear()
    check_labels.clear()

    for i in range(len(items)):
        item = items[i]
        checkbox = ttk.Checkbutton(root, text="")
        checkbox.invoke()
        checkbox.invoke()
        check_label = tk.Label(root, text=item, anchor="w")
        check_label.place(x=275, y=10 + i * 20, height=20, width=250)
        checkbox.place(x=260, y=10 + i * 20, width=25, height=20)
        checkboxes.append(checkbox)
        check_labels.append(check_label)


def select_all():
    count = len(checkboxes)
    for checkbox in checkboxes:
        if checkbox.instate(['selected']):
            checkbox.invoke()
            count = count - 1
    if not count == 0:
        for checkbox in checkboxes:
            checkbox.invoke()


def main_window():
    root.title("Email Manager")

    root.geometry("500x500")

    curr_email = tk.Label(root, text=Encryption.read_sender_credentials()[0], anchor="w")
    curr_email.place(x=15, y=10, height=40, width=170)
    email_button = tk.Button(root, text="Change email", command=change_email_window)
    email_button.place(x=15, y=50, height=30, width=170)

    send_button = tk.Button(root, text="Send", command=send_emails)
    send_button.place(x=440, y=450, height=40, width=50)

    file_img = tk.PhotoImage(file='Icons/file.png')
    file_button = tk.Button(root, command=select_file, image=file_img)
    file_button.place(x=10, y=405, height=40, width=40)
    file_path_label.place(x=55, y=415, height=20, width=400)

    img_img = tk.PhotoImage(file="Icons/img.png")
    image_button = tk.Button(root, command=select_image, image=img_img)
    image_button.place(x=10, y=450, height=40, width=40)
    img_path_label.place(x=55, y=460, height=20, width=400)

    add_recipient_button = tk.Button(root, text="Add Recipient", command=add_recipient_window)
    add_recipient_button.place(x=400, y=405, height=40, width=90)

    remove_recipients_button = tk.Button(root, text="Remove Selected", command=remove_recipients)
    remove_recipients_button.place(x=295, y=405, height=40, width=100)

    select_all_button = tk.Button(root, text="Select\nAll", command=select_all)
    select_all_button.place(x=245, y=405, width=45, height=40)

    subject_label = tk.Label(root, text="Subject:", anchor="w")
    subject_label.place(x=15, y=85, height=20, width=50)

    message_label = tk.Label(root, text="Message:", anchor="w")
    message_label.place(x=15, y=140, height=20, width=55)

    font_tuple = ("Calibri", 11, "")
    subject_box.configure(font=font_tuple)
    text_box.configure(font=font_tuple)
    subject_box.place(x=15, y=105, height=30, width=225)
    text_box.place(x=15, y=160, height=200, width=225)

    items = RecipientManager.get_emails()
    check_list(items)
    root.mainloop()


root = tk.Tk()
add_window = tk.Toplevel(root)
email_window = tk.Toplevel(root)
photo = tk.PhotoImage(file="Icons/icon.png")
root.iconphoto(False, photo)
new_recipient = tk.StringVar()
updated_email = tk.StringVar()
updated_password = tk.StringVar()

init_add_recipient_window()
init_change_email_window()
add_window.withdraw()
email_window.withdraw()
text_box = tk.Text(root)
img_path_label = tk.Label(root, text=image_path, anchor="w")
file_path_label = tk.Label(root, text=file_path, anchor="w")
subject_box = tk.Text(root)
subject_box.focus()

main_window()
