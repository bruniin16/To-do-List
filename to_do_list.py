from tkinter import *
import json

corbg = "#242323"

def add_item():
    item = item_entry.get()
    if item:
        item_list.insert(END, item)
        item_entry.delete(0, END)

def remove_item():
    selec = item_list.curselection()
    item_list.delete(selec[0])

def completed():
    selec = item_list.curselection()
    if selec:
        completed_list.insert(END, item_list.get(selec))
        item_list.delete(selec[0])



main = Tk()
main.title("to-do list")
main.geometry("800x500+700+300")
main.config(bg = "#242323")
#main.resizable(width = False, height = False)

#campo para adicionar um item
item_entry = Entry(main, bg=corbg, fg="white")
item_entry.pack()

#botão para adicionar o item
add_button = Button(main, text="Add Task", command=add_item, bg=corbg, fg="white", relief="solid")
add_button.pack()


#lista de itens a fazer
item_list = Listbox(main, height=20, width=40, bg=corbg, fg="white", relief="solid", highlightthickness=2)
item_list.configure(highlightbackground="purple")
item_list.pack()

#botão para remover itens
remove_button = Button(main, text="Remove Task", command=remove_item, bg=corbg, fg="white", relief="solid")
remove_button.pack()

#botão para completar tarefas
completed_button = Button(main, text="Completed", command=completed, bg=corbg, fg="white", relief="solid")
completed_button.pack()

#lista de tarefas completadas
completed_list = Listbox(main, height=20, width=40, bg=corbg, fg="white", relief="solid", highlightthickness=2)
completed_list.configure(highlightbackground="purple")
completed_list.pack()

main.mainloop()