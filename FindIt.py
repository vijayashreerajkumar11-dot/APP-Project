
import tkinter as tk
from tkinter import ttk, messagebox

items = []
shown_items = []

# Add a new lost or found item
def add_item():
    name = name_entry.get().strip()
    category = category_box.get()
    location = location_entry.get().strip()
    status = status_var.get()

    if not name or not category or not location:
        messagebox.showwarning("Warning", "Fill all details")
        return

    items.append([name, category, location, status])
    show_all()
    name_entry.delete(0, tk.END)
    category_box.set("")
    location_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Item added!")

# Display the selected list of items
def display(data):
    global shown_items
    shown_items = data[:]
    item_list.delete(*item_list.get_children())
    for item in shown_items:
        item_list.insert("", tk.END, values=item)

# Show every reported item
def show_all():
    display(items)

# Search using any item detail
def search_item():
    word = search_entry.get().strip().lower()
    result = [item for item in items if any(word in part.lower() for part in item)]
    display(result)

# Delete the selected report
def delete_item():
    selected = item_list.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select an item")
        return
    item = shown_items[item_list.index(selected[0])]
    if messagebox.askyesno("Confirm", "Delete " + item[0] + "?"):
        items.remove(item)
        show_all()
        messagebox.showinfo("Success", "Item deleted")

# Main window
root = tk.Tk()
root.title("FindIt - Campus Lost and Found")
root.geometry("600x850")
root.minsize(550, 700)
root.resizable(True, True)
root.configure(bg="#F0F5F9")

# Header
header = tk.Frame(root, bg="#12304A")
header.pack(fill="x")
tk.Label(header, text="🔎 FindIt", font=("Arial", 26, "bold"),
         bg="#12304A", fg="white").pack(pady=8)
tk.Label(header, text="🎒  🔑  📚  🎧", font=("Arial", 20),
         bg="#12304A", fg="white").pack()
tk.Label(header, text="CAMPUS LOST & FOUND SYSTEM",
         bg="#12304A", fg="#DCEAF4").pack(pady=8)

# Item entry form
form = tk.Frame(root, bg="#FFFFFF", padx=20, pady=8)
form.pack(padx=25, pady=8, fill="x")
tk.Label(form, text="Report an Item", font=("Arial", 16, "bold"),
         bg="#FFFFFF", fg="#12304A").pack(pady=4)

# Item name
tk.Label(form, text="Item Name", bg="#FFFFFF", fg="#12304A").pack()
name_entry = tk.Entry(form, width=38)
name_entry.pack(pady=2)

# Category dropdown
tk.Label(form, text="Category", bg="#FFFFFF", fg="#12304A").pack()
category_box = ttk.Combobox(form, state="readonly", width=35,
    values=["Electronics", "Books & Notes", "Bags & Wallets",
            "ID Cards", "Keys", "Clothing", "Accessories",
            "Water Bottles", "Documents", "Other"])
category_box.pack(pady=2)

# Campus location
tk.Label(form, text="Campus Location", bg="#FFFFFF", fg="#12304A").pack()
location_entry = tk.Entry(form, width=38)
location_entry.pack(pady=2)

# Lost or found option
tk.Label(form, text="Item Status", bg="#FFFFFF", fg="#12304A").pack(pady=2)
status_var = tk.StringVar(value="Lost")
tk.Radiobutton(form, text="Lost", variable=status_var, value="Lost",
               bg="#FFFFFF", fg="#12304A", selectcolor="#DCEAF4").pack()
tk.Radiobutton(form, text="Found", variable=status_var, value="Found",
               bg="#FFFFFF", fg="#12304A", selectcolor="#DCEAF4").pack()

# Add item button
tk.Button(form, text="＋ Add Item", command=add_item, bg="#1E5A7A",
          fg="white", width=22, relief="flat").pack(pady=5)

# Search items
tk.Label(root, text="Search Items", font=("Arial", 13, "bold"),
         bg="#F0F5F9", fg="#12304A").pack()
search_entry = tk.Entry(root, width=35)
search_entry.pack(pady=3)
tk.Button(root, text="Search", command=search_item, bg="#DCEAF4",
          fg="#12304A", width=16, relief="flat").pack(pady=3)

# Item history table
tk.Label(root, text="Item History", font=("Arial", 13, "bold"),
         bg="#F0F5F9", fg="#12304A").pack(pady=3)

item_list = ttk.Treeview(root, columns=("Name", "Category", "Location", "Status"),
                         show="headings", height=4)
item_list.heading("Name", text="Name")
item_list.heading("Category", text="Category")
item_list.heading("Location", text="Location")
item_list.heading("Status", text="Status")
item_list.column("Name", width=90)
item_list.column("Category", width=100)
item_list.column("Location", width=90)
item_list.column("Status", width=65)
item_list.pack(padx=5, pady=3)

# Show all and delete buttons
tk.Button(root, text="Show All Items", command=show_all,
          bg="#1E5A7A", fg="white", width=22).pack(pady=3)
tk.Button(root, text="Delete Selected Item", command=delete_item,
          bg="#DCEAF4", fg="#12304A", width=22).pack(pady=3)

# Footer
tk.Label(root, text="Helping lost belongings find their way home 💙",
         bg="#F0F5F9", fg="#12304A").pack(pady=5)

# Run application
root.mainloop()
