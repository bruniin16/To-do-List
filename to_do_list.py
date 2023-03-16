from tkinter import *
import json

corbg = "#242323"

def add_item():
    item = item_entry.get()
    if item:
        item_list.insert(END, " - " + item)
        item_entry.delete(0, END)

def remove_item():
    selec = item_list.curselection()
    item_list.delete(selec[0])

def completed():
    selec = item_list.curselection()
    if selec:
        completed_list["state"] = "normal"
        completed_list.insert(END, item_list.get(selec))
        item_list.delete(selec[0])
        completed_list["state"] = "disabled"



main = Tk()
main.title("to-do list")
main.geometry("665x550+700+300")
main.config(bg = corbg)
main.resizable(width = False, height = False)

#campo para adicionar um item
item_entry = Entry(main, bg=corbg, fg="white", width=30, font="calibri 12", relief="solid")
item_entry.place(x=30, y=30)

#botão para adicionar o item
add_button = Button(main, text="Add Task", command=add_item, bg=corbg, fg="white", relief="solid", font="arial 10 bold")
add_button.place(x=30, y=60)

#lista de itens a fazer
item_list = Listbox(main, height=15, width=35, bg=corbg, fg="white", relief="solid", highlightthickness=2, font="calibri")
item_list.configure(highlightbackground="purple")
item_list.place(x=30, y=160)

#botão para remover itens
remove_button = Button(main, text="Remove Task", command=remove_item, bg=corbg, fg="white", relief="solid", font="arial 10 bold")
remove_button.place(x=30, y=475)

#botão para completar tarefas
completed_button = Button(main, text="Completed", command=completed, bg=corbg, fg="white", relief="solid", font="arial 10 bold")
completed_button.place(x=235, y=475)

#lista de tarefas completadas
completed_list = Listbox(main, height=15, width=35, bg=corbg, fg="white", relief="solid", highlightthickness=2, font="calibri")
completed_list.configure(highlightbackground="purple")
completed_list.place(x=350, y=160)

#Labels
todo_label = Label(main, text="To Do", bg=corbg, fg="white", font="courier 15 bold")
todo_label.place(x=30, y=120)
completed_label = Label(main, text="Completed", bg=corbg, fg="white", font="courier 15 bold")
completed_label.place(x=350, y=120)

main.mainloop()