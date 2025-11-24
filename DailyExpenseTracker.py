import tkinter as tk
from tkinter import messagebox

#list for storing all expenses
expenses=[]

#function for adding expense
def add_exp():
 item=ent_item.get()
 amt=ent_amt.get()

 #save and show message when expense is added by user
 expenses.append((item,amt))
 messagebox.showinfo("Added",f"Added={item} ₹{amt}")
 ent_item.delete(0,tk.END)
 ent_amt.delete(0, tk.END)

#storing all expense data
def show_exp():
 txt.delete("1.0",tk.END)
 if not expenses:
  txt.insert(tk.END,"No expenses yet.\n")
  return
 total=0
 txt.insert(tk.END,"Your Expenses=\n\n")
 for item,amt in expenses:
  txt.insert(tk.END,f"{item} ₹{amt}\n")
  total+=amt
 txt.insert(tk.END,f"\nTotal=₹{total}")

#main screen and buttons
main=tk.Tk()
main.title("Daily Expense Tracker")
main.geometry("350x450")

ltitle=tk.Label(main,text="Daily Expense Tracker",font=("Arial",12,"bold"))
ltitle.pack()

litem=tk.Label(main,text="Expense Item=")
litem.pack()
ent_item=tk.Entry(main,width=30)
ent_item.pack()

lamt=tk.Label(main,text="Amount(₹)=")
lamt.pack()
ent_amt=tk.Entry(main,width=30)
ent_amt.pack()

btn_add=tk.Button(main,text="Add Expense",command=add_exp,width=20,bg="#87CEEB")
btn_add.pack()

btn_show=tk.Button(main,text="Show All Expenses",command=show_exp,width=20,bg="#F085DE")
btn_show.pack()

txt=tk.Text(main,width=35,height=12)
txt.pack()

main.mainloop()
