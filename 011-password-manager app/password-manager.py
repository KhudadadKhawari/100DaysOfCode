from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#---------------------------Password Generator----------------------#
def generate_random_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []

    for _ in range(random.randint(8,10)):
        password.append(random.choice(letters))
    for _ in range(random.randint(2,4)):
        password.append(random.choice(symbols))
    for _ in range(random.randint(2,4)):
        password.append(random.choice(numbers))

    random.shuffle(password)
    generated_password = "".join(password)
    

    password_entry.delete(0,END)
    password_entry.insert(0,str(generated_password))
    pyperclip.copy(generated_password)

#---------------------------Save Password---------------------------#

def add_password():
    if not website.get() or not email_username.get() or not password_entry.get():
        messagebox.showerror(title="empty fillds", message="Website/Email/Passowrd fields can't be empty")
    else:
        password_info = f"{website.get()} | {email_username.get()} | {password_entry.get()} \n"
        user_confirm = messagebox.askokcancel(title=website.get(), message=f"Entered details:\nEmail: {email_username.get()}"
        f"\nPassword: {password_entry.get()} \nClick OK to Save" )

        if user_confirm:

            with open('passwords.txt', 'a') as file:
                file.write(password_info)
                website.delete(0,END)
                email_username.delete(0,END)
                password_entry.delete(0,END)


#---------------------------UI Setup--------------------------------#

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canva = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Practice/day-29/logo.png")
canva.create_image(100,100, image = logo_img)
canva.grid(row=0, column=1)

website_lb = Label(text="Website:")
website_lb.grid(row = 1, column = 0)
website = Entry(width=40)
website.grid(row=1, column=1, columnspan=2)
website.focus()

email_username_lb = Label(text="Email/Username:")
email_username_lb.grid(row = 2, column = 0)
email_username = Entry(width=40)
email_username.grid(row=2, column=1, columnspan=2)

password_lb = Label(text="Password:")
password_lb.grid(row = 3, column = 0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
generate_password_btn = Button(text="Generate Password", width=15, command=generate_random_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=38, command=add_password)
add_btn.grid(row=4, column=1, columnspan=2)




window.mainloop()