from tkinter import *

root = Tk()

root.title("Driving License")
root.geometry("300x400")


root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="purple")
canvas.create_rectangle(0, 345, 300, 400, fill="purple")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Driving License")
label_id_tag = canvas.create_text(20, 150, font=('Times', '16', 'bold'), text="ID :")
label_name_tag = canvas.create_text(33, 180, font=('Times', '16', 'bold'), text="Name :")
label_date_of_birth_tag = canvas.create_text(50, 210, font=('Times', '12', 'bold'), text="Date of Birth :")
label_pin_tag = canvas.create_text(40, 240, font=('Times', '16', 'bold'), text="Pin no. :")
label_address_tag = canvas.create_text(42, 280, font=('Times', '16', 'bold'), text="Address :")
label_auth_tag = canvas.create_text(105, 310, font=('Times', '10', 'bold'), text="Auth. to drive the following vehicles :")

label_id = Label(root)
label_name = Label(root)
label_date_of_birth = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_auth = Label(root)

def myCardDetails():
    ID = "18390486730"
    print(type(id))
    name = "Krish Kataruka"
    print(type(name))
    date_of_birth = " 23rd March, 2009"
    print(type(date_of_birth))
    pin = "Kolkata - 700071"
    print(type(pin))
    address = "10 Lord Sinha Road, 6D Ankur Building"
    print(type(address))
    auth = "Two Four"
    print(type(auth))
    
    label_id["text"] = ID
    label_name["text"] = name
    label_date_of_birth["text"]= date_of_birth
    label_pin["text"]= pin
    label_address["text"]= address
    label_auth["text"]= auth
    
button1 = Button(root, text="Show my Driving License", command=myCardDetails)

button1.configure(width=20, activebackground="yellow", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(90, 150, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(110, 180, anchor=CENTER, window=label_name)
label_date_of_birth_window = canvas.create_window(155, 210, anchor=CENTER, window=label_date_of_birth)
label_pin_window = canvas.create_window(125, 240, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(190, 280, anchor=CENTER, window=label_address)
label_auth_window = canvas.create_window(235, 310, anchor=CENTER, window=label_auth)
canvas.pack()

root.mainloop()

