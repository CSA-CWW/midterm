import tkinter
from tkinter import *
from tkinter import ttk
root = Tk()
file_send = False
def drink():
    global error, drinkbal
    drinklist = ['Soda','Tea','Bottled Water','Milk','Juice']
    if drinkvar.get() == 'Soda' or drinkvar.get() == 'Tea' or drinkvar.get() == 'Bottled Water':
        drinkbal = 1
    if drinkvar.get() == 'Milk':
        drinkbal = .75
    if drinkvar.get() == 'Juice':
        drinkbal = 1.25
    if drinkvar.get() not in drinklist:
        drinkbal = '.'
        error = True
    if drinkvar.get() in drinklist:
        error = False
        
def calc():
    global drinkbal, error, file_send, final_list, final_bal
    final_list = [] ; final_bal = '.'
    entreebal = '.'
    ################DRINK######################################
    drink()
    ################ENTREE#####################################
    if entree.get(ACTIVE) == 'Sandwich':
        entreebal = 3
    if entree.get(ACTIVE) == 'Pizza':
        entreebal = 4
    if entree.get(ACTIVE) == 'Chicken Nuggets':
        entreebal = 3.75
    if entree.get(ACTIVE) == 'Chicken':
        entreebal = 4
    if entree.get(ACTIVE) == 'Tofu':
        entreebal = 15
    if entree.get(ACTIVE) == 'Clam Chowder':
        entreebal = 20
    if entree.get(ACTIVE) not in entree_list:
        error = True
    if entree.get(ACTIVE) in entree_list and error != True:
        error = False
    ################FINAL APEND#################################
    if error == False:
        final_list.append(employee.get())
        final_list.append(day.get())
        final_list.append(optvar.get())
        final_list.append(drinkvar.get())
        final_list.append(entree.get(ACTIVE))

        final_bal = (round(((drinkbal + entreebal) + ((drinkbal + entreebal) * .0825)),2))
        final_list.append(final_bal)
        price_label.configure(text='Price: $' +str(final_bal)+ '')
        file_send = True
    else:
        price_label.configure(text='Price: NOT ALL AREAS FILLED OUT')
        file_send = False

def check():
    global final_list, file_send
    if file_send == True:
        file = open('document.txt','a')
        file.write('Employee: ' +str(final_list[0])+ '\n')
        file.write('Day: ' +str(final_list[1])+ '\n')
        file.write('Payment option: ' +str(final_list[2])+ '\n')
        file.write('Drink: ' +str(final_list[3])+ '\n')
        file.write('Food: ' +str(final_list[4])+ '\n')
        file.write('Price: ' +str(final_list[5])+ '\n')
        file.write('\n\n')
        file.close()
        root.destroy()
                

drinkvar = StringVar()
drink_label = Label(root, text="Drinks")

soda = ttk.Radiobutton(root, text="Soda", variable=drinkvar, value='Soda', command=drink)
tea = ttk.Radiobutton(root, text="Tea", variable=drinkvar, value='Tea', command=drink)
milk = ttk.Radiobutton(root, text="Milk", variable=drinkvar, value='Milk', command=drink)
juice = ttk.Radiobutton(root, text="Juice", variable=drinkvar, value='Juice', command=drink)
water = ttk.Radiobutton(root, text="Bottled Water", variable=drinkvar, value='Bottled Water', command=drink)


price_label = Label(root, text="Price:")

entree_label = Label(root, text="Entrees")
entree = Listbox(root, height=10)
entree_list = ['Sandwich','Pizza','Chicken Nuggets','Chicken','Tofu','Clam Chowder']
for x in entree_list:
    entree.insert(END, x)


optvar = StringVar()
option = ttk.Combobox(root,text='', textvariable = optvar, width=15)
option['values'] = ['Credit','Check','Cash']


empvar = StringVar()
employee = Entry(root,textvariable=empvar)
employee_label = Label(root, text="Employee ID:")


calculate = Button(root,text='Calculate',command=calc)
checkout = Button(root,text='Checkout',command=check)

day = Spinbox(values=('Monday','Tuesday','Wednesday','Thursday','Friday'))

drink_label.grid(column=1,row=1, sticky='W') ; entree_label.grid(column=2,row=1, sticky='W')
employee_label.grid(column=2, row=7, sticky='W')
employee.grid(column=2, row=8, sticky='W')
day.grid(column=1, row=7, sticky='NSEW')
soda.grid(column=1, row=2, sticky='NSEW')
tea.grid(column=1, row=3, sticky='NSEW')
milk.grid(column=1, row=4, sticky='NSEW')
juice.grid(column=1, row=5, sticky='NSEW')
water.grid(column=1, row=6, sticky='NSEW')

entree.grid(column=2, row=2, sticky='NSEW',rowspan=5)
option.grid(column=1, row=8, sticky='NSEW')
calculate.grid(column=1, row=9, sticky='NSEW')
checkout.grid(column=2, row=9, sticky='NSEW')
price_label.grid(column=1, row=0, columnspan=2)
