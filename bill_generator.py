import tkinter as tk
from tkinter import messagebox

class BillManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Management")
        self.root.geometry("700x500")
        self.root.config(bg="black")
        
        # Item Details (Menu)
        self.menu = {
            "Dosa": 60,
            "Cookies": 30,
            "Tea": 7,
            "Coffee": 100,
            "Juice": 20,
            "Pancakes": 15,
            "Eggs": 7
        }
        
        # Variables to store quantities
        self.quantities = {item: tk.IntVar() for item in self.menu}
        self.total = tk.DoubleVar()

        # Title
        tk.Label(self.root, text="BILL MANAGEMENT", font=("Arial", 16, "bold"), bg="black", fg="white").pack(side=tk.TOP, fill=tk.X)

        # Left Frame: Menu
        left_frame = tk.Frame(self.root, bg="lightgreen", bd=2, relief=tk.RIDGE)
        left_frame.place(x=10, y=50, width=200, height=300)
        tk.Label(left_frame, text="Menu", font=("Arial", 14, "bold"), bg="lightgreen").pack()
        for item, price in self.menu.items():
            tk.Label(left_frame, text=f"{item}......Rs.{price}/unit", font=("Arial", 12), bg="lightgreen").pack(anchor="w")

        # Center Frame: Quantity Inputs
        center_frame = tk.Frame(self.root, bg="pink", bd=2, relief=tk.RIDGE)
        center_frame.place(x=220, y=50, width=250, height=300)
        tk.Label(center_frame, text="Quantity", font=("Arial", 14, "bold"), bg="pink").pack()
        for item in self.menu:
            tk.Label(center_frame, text=item, font=("Arial", 12), bg="pink").pack(anchor="w")
            tk.Entry(center_frame, textvariable=self.quantities[item], font=("Arial", 12), width=5).pack()

        # Right Frame: Bill Display
        right_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.RIDGE)
        right_frame.place(x=440, y=50, width=250, height=300)
        tk.Label(right_frame, text="Bill", font=("Arial", 14, "bold"), bg="white").pack()
        tk.Label(right_frame, text="Total", font=("Arial", 12, "bold"), bg="white").pack()
        self.total_label = tk.Label(right_frame, text="Rs. 0.00", font=("Arial", 12, "bold"), bg="lightgreen", fg="black")
        self.total_label.pack(pady=10)

        # Buttons
        tk.Button(self.root, text="Reset", command=self.reset, font=("Arial", 12), bg="gray", fg="white").place(x=220, y=360, width=100, height=30)
        tk.Button(self.root, text="Total", command=self.calculate_total, font=("Arial", 12), bg="#008000", fg="white").place(x=350, y=360, width=100, height=30)
        btn_generate = tk.Button(root, text="Generate Bill", command=self.generate_bill, bg="blue", fg="white", font=("Arial", 14))
        btn_generate.place(x=20, y=450, width=200, height=40)
        
        btn_save = tk.Button(root, text="Save Bill", command=self.save_bill, bg="orange", fg="white", font=("Arial", 14))
        btn_save.place(x=250, y=450, width=200, height=40)
        
        btn_exit = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", font=("Arial", 14))
        btn_exit.place(x=480, y=450, width=200, height=40)
    def calculate_total(self):
        """Calculate the total bill."""
        total_cost = 0
        for item, price in self.menu.items():
            quantity = self.quantities[item].get()
            if quantity < 0:
                messagebox.showerror("Error", "Quantity cannot be negative!")
                return
            total_cost += price * quantity
        self.total.set(total_cost)
        self.total_label.config(text=f"Rs. {total_cost:.2f}")

    def reset(self):
        """Reset all quantities and total."""
        for item in self.quantities:
            self.quantities[item].set(0)
        self.total.set(0.0)
        self.total_label.config(text="Rs. 0.00")
    def generate_bill(self):
        if not self.items:
            messagebox.showerror("Error", "No items to generate a bill!")
            return
        
        self.txt_bill.delete(1.0, tk.END)
        bill_content = f"Bill Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        bill_content += "="*40 + "\n"
        bill_content += f"{'Item':<15}{'Price':<10}{'Qty':<5}{'Total':<10}\n"
        bill_content += "="*40 + "\n"
        
        for item in self.items:
            bill_content += f"{item[0]:<15}{item[1]:<10.2f}{item[2]:<5}{item[3]:<10.2f}\n"
        
        bill_content += "="*40 + "\n"
        bill_content += f"{'Total Amount':<30}{self.total_amount:.2f}\n"
        bill_content += "="*40
        self.txt_bill.insert(tk.END, bill_content)
    
    def save_bill(self):
        if not self.items:
            messagebox.showerror("Error", "No bill to save!")
            return
        
        filename = f"Bill_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(self.txt_bill.get(1.0, tk.END))
        messagebox.showinfo("Saved", f"Bill saved as {filename}")    

# Run the application
root = tk.Tk()
app = BillManagement(root)
root.mainloop()
