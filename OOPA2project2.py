# PROJECT 2 - PIZZA ORDER MANAGEMENT SYSTEM
# ==========================================

from hmac import new
from textwrap import fill
import tkinter as tk
from tkinter import Toplevel, Entry, Label, Button, ttk, messagebox
from turtle import left, width

# ========== Pizza databases and storing ==========
order_items_basket = []
order_items_price_basket = []
customer_database = []
order_details = []

# ========== PARENT CLASSES ==========
class Pizza:
    #properties
    def __init__(self, pizza_name, pizza_description, pizza_price, pizza_image):
        self.pizza_name = pizza_name
        self.pizza_description = pizza_description
        self.pizza_price = pizza_price
        self.pizza_image = pizza_image

    #storing pizza information
    def store_pizza_details(self):
        return [
            self.pizza_name,
            self.pizza_description,
            self.pizza_price,
            self.pizza_image
        ]

class Customer:
    #properties
    def __init__(self, customer_name, customer_email, customer_phone_num, customer_postcode, customer_payment):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_phone_num = customer_phone_num
        self.customer_postcode = customer_postcode
        self.customer_payment = customer_payment

    #storing customer information
    def store_customer_details(self):
        return [
            self.customer_name,
            self.customer_email,
            self.customer_phone_num,
            self.customer_postcode,
            self.customer_payment
        ]

class Order:
    #properties
    def __init__(self, order_id, order_items, order_items_prices):
        self.order_id = order_id
        self.order_items = order_items
        self.order_items_prices = order_items_prices
        self.total = sum(self.order_items_prices)

    #storing order information
    def store_order_details(self):
        return [
            self.order_id,
            self.order_items,
            self.total #calculating total sum of all order
        ]

class Error:
    def __init__(self, error_title, error_description):
        self.error_title = error_title
        self.error_description = error_description

# ========== CHILDREN CLASSES ==========
class Payment_Type(Error):
    error_title = "Error message"
    error_description = "\n\nThe wrong type of payment is entered.\nAccepted values: Cash, Card, ApplePay. \n\nTry again\n\n"
    def __init__(self):
        super().__init__(Payment_Type.error_title, Payment_Type.error_description)

# ========== MAIN ==========
#screen 1
screen_1 = tk.Tk()
screen_1.title('Pizza Shop')
screen_1.geometry("1920x1080")
screen_1.configure(bg="#FFF1D7")

screen1_label = tk.Label(screen_1, text=f"\nOur pizzas", font=("Verdana", 36, "bold"), bg="#FFF1D7")
screen1_label.pack()
screen1_section1 = tk.Frame(screen_1, bg="#FFF1D7")
screen1_section1.pack(padx=100, pady=12)

#creating pizza objects
pizza1 = Pizza("Margherita", "Pizza as the heartier cousin of Caprese salad, with a crisp, chewy crust supporting the delicious trio of tomatoes, basil, and fresh mozzarella.", 20.99, "D:/desktop/codding/oop/code - project 2/program 2/card1.png")
pizza2 = Pizza("Pepperoni", "Pepperoni is an American variety of salami, made from cured pork and beef seasoned with paprika or other chili pepper.", 30.99, "D:/desktop/codding/oop/code - project 2/program 2/card1.png")
pizza3 = Pizza("Vegetables", "Piled with flavourful veggies like peppers and artichokes, this vegetarian pizza will be a hit at your next pizza night! Fresh basil takes it over the top.", 40.99, "D:/desktop/codding/oop/code - project 2/program 2/card1.png")

#adding choosing items to the basket
def add_item_button(option):
    if option == "1":
        item_name = pizza1.pizza_name
        item_price = pizza1.pizza_price
    elif option == "2":
        item_name = pizza2.pizza_name
        item_price = pizza2.pizza_price
    else:
        item_name = pizza3.pizza_name
        item_price = pizza3.pizza_price
    order_items_basket.append(item_name)
    order_items_price_basket.append(item_price)

def pizza_card(root, pizza_image, pizza_name, pizza_description, option):
    #creating and adding background and actual card
    card = tk.Frame(root, bg="#BB3E00", padx=40, pady=10)
    card.pack(side="left", padx=5, pady=5, fill="y")
    #creating and adding image
    image = tk.PhotoImage(file=pizza_image)
    image_label = tk.Label(card, image=image, bg="#BB3E00", height=350, width=400)
    image_label.image = image
    image_label.pack()
    #creating and adding name
    pizza_name_label = tk.Label(card, text=pizza_name, font=("Verdana", 15, "bold"), bg="#BB3E00", fg="#FFF1D7")
    pizza_name_label.pack()
    #creating and adding description
    pizza_description_label = tk.Label(card, text=pizza_description, font=("Verdana", 13, "italic"), bg="#BB3E00", fg="#FFF1D7", wraplength=350)
    pizza_description_label.pack()
    #refer to add function
    def recursive_func(o=option.strip()):
        add_item_button(o)

    #creating and adding a button
    add_button = tk.Button(card, text="Add", command=recursive_func, font=("Verdana", 15, "bold"), bg="#F7AD45", fg="#FFF1D7", width=10)
    add_button.pack()

#adding card
pizza_card(screen1_section1, "D:/desktop/codding/oop/code - project 2/program 2/card1.png", "Margherita", f"\nPizza as the heartier cousin of Caprese salad, with a crisp, chewy crust supporting the delicious trio of tomatoes, basil, and fresh mozzarella.\n", "1")
pizza_card(screen1_section1, "D:/desktop/codding/oop/code - project 2/program 2/card2.png", "Pepperoni", f"\nPepperoni is an American variety of salami, made from cured pork and beef seasoned with paprika or other chili pepper.\n", "2")
pizza_card(screen1_section1, "D:/desktop/codding/oop/code - project 2/program 2/card3.png", "Vegetables", f"\nPiled with flavourful veggies like peppers and artichokes, this vegetarian pizza will be a hit at your next pizza night! Fresh basil takes it over the top.\n", "3")

def open_customer_details_screen():
    screen_2 = tk.Toplevel(screen_1)
    screen_2.title('Customer details')
    screen_2.geometry("1600x700")
    screen_2.configure(bg="#7B6F19")
    screen2_label = tk.Label(screen_2, text=f"\nCustomer details", font=("Verdana", 26, "bold"), fg="#FFF1D7", bg="#7B6F19")
    screen2_label.pack()
    form_section = tk.Frame(screen_2, bg="#F7AD45", padx=40, pady=10)
    form_section.pack(fill="both", padx=540, pady=14)

    #adding and creating form (labels + inputs)
    order_id_lable = Label(form_section, text="Order ID:", height=3, bg="#F7AD45", fg="#BB3E00", font=("Verdana", 12, "bold"))
    order_id = Entry(form_section, width=45, bg="#FFF1D7", fg="black", font=("Verdana", 12), justify="left")
    order_id_lable.pack()
    order_id.pack()
    customer_name_lable = Label(form_section, text="Customer name:", height=3, bg="#F7AD45", fg="#BB3E00", font=("Verdana", 12, "bold"))
    customer_name = Entry(form_section, width=45, bg="#FFF1D7", fg="black", font=("Verdana", 12), justify="left")
    customer_name_lable.pack()
    customer_name.pack()
    customer_email_lable = Label(form_section, text="Customer email:", height=3, bg="#F7AD45", fg="#BB3E00", font=("Verdana", 12, "bold"))
    customer_email = Entry(form_section, width=45, bg="#FFF1D7", fg="black", font=("Verdana", 12), justify="left")
    customer_email_lable.pack()
    customer_email.pack()
    customer_phone_num_lable = Label(form_section, text="Customer phone number:", height=3, bg="#F7AD45", fg="#BB3E00", font=("Verdana", 12, "bold"))
    customer_phone_num = Entry(form_section, width=45, bg="#FFF1D7", fg="black", font=("Verdana", 12), justify="left")
    customer_phone_num_lable.pack()
    customer_phone_num.pack()
    customer_postcode_lable = Label(form_section, text="Customer postcode:", height=3, bg="#F7AD45", fg="#BB3E00", font=("Verdana", 12, "bold"))
    customer_postcode = Entry(form_section, width=45, bg="#FFF1D7", fg="black", font=("Verdana", 12), justify="left")
    customer_postcode_lable.pack()
    customer_postcode.pack()
    customer_payment_lable = Label(form_section, text="Payment method (Cash/Card/ApplePay):", height=3, bg="#F7AD45", fg="#BB3E00", font=("Verdana", 12, "bold"))
    customer_payment = Entry(form_section, width=45, bg="#FFF1D7", fg="black", font=("Verdana", 12), justify="left")
    customer_payment_lable.pack()
    customer_payment.pack()

    def add_customer_details():
        #validation of data types
        try:
            id_checking = int(order_id.get().strip())
        except ValueError:
            messagebox.showerror("Invalid ID data type", "Please enter a valid integers for order ID.")
            return
        try:
            phone_checking = int(customer_phone_num.get().strip())
        except ValueError:
            messagebox.showerror("Invalid phone number data type", "Please enter a valid integers for phone number. The format for phone number must be: 07xxxxxxxxx")
            return
        #validation of the length of phone nymber
        if len(customer_phone_num.get().strip()) != 11:
            messagebox.showerror("Invalid phone number length", f"Please enter a phone number that is exactly\n10 integers after 0 trunk prefix. \nThe format for phone number must be: 07xxxxxxxxx")
            return
        #validation of payment type
        if customer_payment.get().strip() not in ["Cash", "Card", "ApplePay"]:
            error = Payment_Type()
            screen_error = tk.Toplevel(screen_2)
            screen_error.title("Error: Type of payment")
            screen_error.geometry("400x250")
            screen_error.configure(bg="#BB3E00")
            error_title_lable = Label(screen_error, text=error.error_title, height=3, bg="#BB3E00", fg="#FFF1D7", font=("Verdana", 15, "bold"))
            error_description_lable = Label(screen_error, text=error.error_description, height=5, bg="#BB3E00", fg="#FFF1D7", font=("Verdana", 12))
            try_again_button = tk.Button(screen_error, text='OK', width=15, bg='#F7AD45', fg="white", font=("Verdana", 12, "bold"), command=screen_error.destroy)
            error_title_lable.pack()
            error_description_lable.pack()
            try_again_button.pack()
            return

        global new_customer
        new_customer = Customer(customer_name.get(), customer_email.get(), customer_phone_num.get(), customer_postcode.get(), customer_payment.get())
        global new_order
        new_order = Order(order_id.get(), order_items_basket, order_items_price_basket)
        customer_database.append(new_customer)
        order_details.append(new_order)

        order_details_button["state"] = "normal"
        screen_2.destroy()

    submit_details_button = tk.Button(form_section, text="Submit", font=("Verdana", 14, "bold"), bg="#BB3E00", fg="#FFF1D7", width=15, command=add_customer_details)
    submit_details_button.pack(pady=14)

#creating and adding a button
customer_details_button = tk.Button(screen_1, command=open_customer_details_screen, text="Customer details", font=("Verdana", 17, "bold"), bg="#7B6F19", fg="#FFF1D7", width=15)
customer_details_button.pack()

def open_order_details_screen():
    screen_3 = tk.Toplevel(screen_1)
    screen_3.title('Customer details')
    screen_3.geometry("1600x700")
    screen_3.configure(bg="#F7AD45")
    screen3_label = tk.Label(screen_3, text=f"\nOrder details", font=("Verdana", 26, "bold"), fg="#BB3E00", bg="#F7AD45")
    screen3_label.pack()
    items_section = tk.Frame(screen_3, bg="#BB3E00", padx=40, pady=10)
    items_section.pack(fill="both", padx=540)
    total_section = tk.Frame(screen_3, bg="#7B6F19", padx=40, pady=10)
    total_section.pack(fill="both", padx=540)
    customer_section = tk.Frame(screen_3, bg="#7B6F19", padx=40, pady=10)
    customer_section.pack(fill="both", padx=540)
    
    #displaying items
    for i in range(len(order_items_basket)):
        item = order_items_basket[i]
        price = order_items_price_basket[i]
        basket_item_label = tk.Label(items_section, text=f"{item} --------------------- {price}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#7B6F19")
        basket_item_label.pack()

    #displaying total
    total_label = tk.Label(total_section, text=f"Total: {sum(order_items_price_basket)}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#BB3E00")
    total_label.pack()
    
    #displaying customer details
    final_id_label = tk.Label(customer_section, text=f"Order ID: {new_order.order_id}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#7B6F19")
    final_id_label.pack()
    final_name_label = tk.Label(customer_section, text=f"Customer name: {new_customer.customer_name}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#7B6F19")
    final_name_label.pack()
    final_email_label = tk.Label(customer_section, text=f"Customer email: {new_customer.customer_email}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#7B6F19")
    final_email_label.pack()
    final_phone_label = tk.Label(customer_section, text=f"Customer phone number: {new_customer.customer_phone_num}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#7B6F19")
    final_phone_label.pack()
    final_postcode_label = tk.Label(customer_section, text=f"Customer postcode: {new_customer.customer_postcode}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#7B6F19")
    final_postcode_label.pack()
    final_payment_label = tk.Label(customer_section, text=f"Payment method: {new_customer.customer_payment}", font=("Verdana", 13, "bold"), width=30, fg="#FFF1D7", bg="#7B6F19")
    final_payment_label.pack()
    
    image = tk.PhotoImage(file="D:/desktop/codding/oop/code - project 2/program 2/logo.png")
    image_label = tk.Label(customer_section, image=image, bg="#7B6F19", height=100, width=100)
    image_label.image = image
    image_label.pack()

#creating and adding a button
order_details_button = tk.Button(screen_1, state="disable", text="Order details", command=open_order_details_screen, font=("Verdana", 17, "bold"), bg="#F7AD45", fg="#FFF1D7", width=15)
order_details_button.pack(pady=15)

screen_1.mainloop()
