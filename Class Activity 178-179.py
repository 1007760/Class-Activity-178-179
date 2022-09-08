from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("500x500")
root.title("Class Activity 178-179")

label_heading = Label(root, text = "Juice Center", bg = "orange2", font = ("Sylfaen", 18, "bold", "italic"))
label_heading.place(relx = 0.05, rely = 0.1, anchor = W)


#Heading
label_heading = Label(root, text="Juice Center",bg="orange2", font=("Sylfaen",18,"bold","italic"))
label_heading.place(relx=0.05,rely=0.1, anchor= W)

#Logo image
juice = ImageTk.PhotoImage(Image.open ("logo"))
juice_image=Label(root, image=juice, bg="orange2")
juice_image.place(relx=0.2, rely=0.4,anchor=CENTER)

#Load Images
apple = ImageTk.PhotoImage(Image.open ("apple"))
mango = ImageTk.PhotoImage(Image.open ("mango"))
orange = ImageTk.PhotoImage(Image.open ("orange.jpg"))


#Fruit Images
fruit_image=Label(root, bg="orange2")
fruit_image.place(relx=0.8, rely=0.8,anchor=CENTER)


#Label Select Fruit
label_name = Label(root, text="Select fruit ",bg="orange2", font=("Bahnschrift Light",15))
label_name.place(relx=0.96,rely=0.2, anchor= E)


#Dropdown
fruit_list = ["Apple","Mango","Orange"]
fruit_dropdown = ttk.Combobox(root,state = "readonly", values=fruit_list, justify="right") 
fruit_dropdown.place(relx=0.95, rely=0.25, anchor= E)


#Label Enter Quantity
label_quantity = Label(root, text="Enter Quantity ",bg="orange2", font=("Bahnschrift Light",15))
label_quantity.place(relx=0.96,rely=0.35, anchor= E)


#Entry Element
input_quantity = Entry(root)
input_quantity.place(relx=0.95,rely=0.4, anchor= E)


#Total Cost Label
label_show_amount = Label(root ,bg="orange2", font=("Bahnschrift Light",12))
label_show_amount.place(relx=0.95,rely=0.7, anchor= E)

#Quantity Label
label_show_quantity = Label(root ,bg="orange2", font=("Bahnschrift Light",12))
label_show_quantity.place(relx=0.95,rely=0.8, anchor= E)

class Juice :
    def __init__(fruit_name, quantity, self) :
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 2.50
        
    def calculate_cost(self) :
        total_cost = self.quantity*self.__cost
        label_show_amount['text'] = "YOu have to pay : " + str(total_cost) + " USD"
        
        if (self.fruit == "apple") :
            calorie = self.quantity * 52
            fruit_image['image'] = apple
            
        elif (self.fruit == "mango") : 
            calorie = self.quantity * 60
            fruit_image['image'] = mango
            
        elif (self.fruit == "orange") :
            calorie = self.quantity * 47
            fruit_image['image'] = orange
            
        label_show_quantity['text'] = "x" + str(self.quantity) + " = " + str(calorie)
        
    def getCost(self) :
        self.__calculateCost()
        
def orderJuice() :
    fruit = fruit_dropdown.get()
    quantity = input_quantity.get()
    obj1 = Juice(fruit, quantity)
    obj1.getCost()
    
btn1 = Button(root, text = "Total Amount Due : ", command = orderJuice)
btn1.place(relx = 0.95, rely = 0.5, anchor = E)
root.mainloop()