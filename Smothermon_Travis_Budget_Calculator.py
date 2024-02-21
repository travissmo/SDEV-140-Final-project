import tkinter as tk
from tkinter import messagebox
#This function will calculate a basic budget based on monthly income
def calculate_budget():
    try:
        income = float(income_entry.get())
    except ValueError:  #Added a value error if user enters a non float
        messagebox.showerror("Error", "Please enter a valid income.")
        return
#Opens the spending window
def open_spending_window():
    spending_window = tk.Toplevel(root)
    spending_window.title("Recommended Spending Calculator")

    spending_label = tk.Label(spending_window, text= "Enter your monthly spending for reccomendations")
    spending_label.pack(pady = 10)
   
    spending_entry = tk.Entry(spending_window)
    spending_entry.pack(pady=10)

    spending_calculation_button = tk.Button(spending_window, text= "Calculate your spending recommendation")
    spending_calculation_button.pack(pady= 10)

# Main window
root = tk.Tk()
root.title("Budget Calculator")

# Label and Entry for Monthly Income, Housing Costs, Utilities, Food, and Savings entered by user
income_label = tk.Label(root, text="Enter Monthly Income:")
income_label.pack(pady=10)

income_entry = tk.Entry(root)
income_entry.pack(pady=10)

housing_label = tk.Label(root, text="Monthly Housing Costs:")
housing_label.pack(pady=5)

housing_entry = tk.Entry(root)
housing_entry.pack(pady=5)

food_label = tk.Label(root, text="Monthly Food Expenses:")
food_label.pack(pady=5)

food_entry = tk.Entry(root)
food_entry.pack(pady=5)

utilities_label = tk.Label(root, text="Monthly Utilities Expenses:")
utilities_label.pack(pady=5)

utilities_entry = tk.Entry(root)
utilities_entry.pack(pady=5)

savings_label = tk.Label(root, text="Monthly Savings:")
savings_label.pack(pady=5)

savings_entry = tk.Entry(root)
savings_entry.pack(pady=5)

# Button to calculate budget
calculate_button = tk.Button(root, text="Calculate Budget", command=calculate_budget)
calculate_button.pack(pady=10)

# Button to open the spending window
spending_button = tk.Button(root, text="Open Spending Window", command=open_spending_window)
spending_button.pack(pady=10)

root.mainloop()