import tkinter as tk

# Function to handle button clicks
def on_click(button_value):
    if button_value == "=":  # Calculate the result
        try:
            result = eval(entry.get())  # Evaluate the expression
            entry.delete(0, tk.END)  # Clear the entry
            entry.insert(0, str(result))  # Display the result
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")  # Display error for invalid input
    elif button_value == "C":  # Clear the entry
        entry.delete(0, tk.END)
    else:  # Add the button value to the entry
        entry.insert(tk.END, button_value)

# Create the main window
root = tk.Tk()
root.title("Indian Flag Themed Calculator")
root.geometry("400x500")
root.config(bg="#ffffff")  # White background for the flag's center

# Add a border effect with saffron and green at the top and bottom
top_stripe = tk.Frame(root, height=10, bg="#ff9933")
top_stripe.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Entry widget to display the expression/result
entry = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.FLAT,
    bg="#ffffff",  # White
    fg="#00008b"  # Navy blue for text
)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=20)

# Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Button colors based on the Indian flag
button_colors = {
    "numbers": "#138808",  # Green
    "operations": "#ff9933",  # Saffron
    "clear": "#ff4500",  # Bright saffron/red for emphasis
    "equals": "#00008b",  # Navy blue
}

# Add buttons to the grid
row = 2
col = 0
for button in buttons:
    if button.isdigit() or button == "0":  # Number buttons
        color = button_colors["numbers"]
    elif button in ["+", "-", "*", "/"]:  # Operation buttons
        color = button_colors["operations"]
    elif button == "C":  # Clear button
        color = button_colors["clear"]
    elif button == "=":  # Equals button
        color = button_colors["equals"]

    tk.Button(
        root,
        text=button,
        font=("Arial", 18),
        width=5,
        height=2,
        bg=color,
        fg="white",
        bd=0,
        activebackground="#37474f",  # Darker shade for button press
        activeforeground="white",
        command=lambda b=button: on_click(b),
    ).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Bottom stripe for the flag
bottom_stripe = tk.Frame(root, height=10, bg="#138808")
bottom_stripe.grid(row=row + 1, column=0, columnspan=4, sticky="nsew")

# Run the application
root.mainloop()
