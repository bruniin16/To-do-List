from tkinter import *
import json

corbg = "#242323"

def add_item():
    item = item_entry.get()
    if item:
        item_list.insert(END, " - " + item)
        item_entry.delete(0, END)
        save()

def remove_item():
    selec = item_list.curselection()
    item_list.delete(selec[0])
    save()

def remove_completed():
    selec = completed_list.curselection()
    completed_list.delete(selec[0])
    save()

def completed():
    selec = item_list.curselection()
    if selec:
        completed_list.insert(END, item_list.get(selec))
        item_list.delete(selec[0])
        save()

def save():
    items = item_list.get(0, END)
    with open("items.json", "w") as f:
        json.dump(items, f)
    
    complete = completed_list.get(0, END)
    with open("completed.json", "w") as f:
        json.dump(complete, f)

def load():
    try:
        with open("items.json", "r") as f:
            items = json.load(f)
        for item in items:
            item_list.insert(END, item)
    except FileNotFoundError:
        pass

    try:
        with open("completed.json", "r") as f:
            complete = json.load(f)
        for item in complete:
            completed_list.insert(END, item)
    except FileNotFoundError:
        pass

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

removecomp_button = Button(main, text="Clear Completed Task", command=remove_completed, bg=corbg, fg="white", relief="solid", font="arial 10 bold")
removecomp_button.place(x=350, y=475)

#botão para completar tarefas
completed_button = Button(main, text="Completed", command=completed, bg=corbg, fg="white", relief="solid", font="arial 10 bold")
completed_button.place(x=235, y=475)

#lista de tarefas completadas
completed_list = Listbox(main, height=15, width=35, bg=corbg, fg="grey", relief="solid", highlightthickness=2, font="calibri")
completed_list.configure(highlightbackground="purple")
completed_list.place(x=350, y=160)

#Labels
todo_label = Label(main, text="To Do", bg=corbg, fg="white", font="courier 15 bold")
todo_label.place(x=30, y=120)
completed_label = Label(main, text="Completed", bg=corbg, fg="white", font="courier 15 bold")
completed_label.place(x=350, y=120)

load()
main.mainloop()