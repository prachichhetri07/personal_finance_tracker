import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create main window
root = tk.Tk()
root.title("Finance Tracker")
root.geometry("500x400")

# Initialize data
finance_data = {'Month': [], 'Income': [], 'Expenses': [], 'Savings': []}

# Function to add finance data
def add_data():
    try:
        month = month_entry.get()
        income = float(income_entry.get())
        expenses = float(expenses_entry.get())
        savings = income - expenses
        
        finance_data['Month'].append(month)
        finance_data['Income'].append(income)
        finance_data['Expenses'].append(expenses)
        finance_data['Savings'].append(savings)
        
        messagebox.showinfo("Success", "Data added!")
        month_entry.delete(0, tk.END)
        income_entry.delete(0, tk.END)
        expenses_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

# Function to visualize the finance data
def visualize_data():
    if not finance_data['Month']:
        messagebox.showwarning("No Data", "No data to show!")
        return
    
    df = pd.DataFrame(finance_data)
    plt.figure(figsize=(4, 6))

    # Plot Income with customized style
    plt.plot(df['Month'], df['Income'], 
             label='Income', 
             marker='o', 
             color='#2ca02c',   # Green shade
             linestyle='--',    # Dashed line
             linewidth=2,       # Line width
             markersize=8)      # Marker size

    # Plot Expenses with customized style
    plt.plot(df['Month'], df['Expenses'], 
             label='Expenses', 
             marker='D',        # Diamond marker
             color='#d62728',   # Red shade
             linestyle='-.',    # Dash-dot line
             linewidth=2, 
             markersize=8)

    # Plot Savings as a scatter with different color and transparency
    plt.scatter(df['Month'], df['Savings'], 
                color='#1f77b4',   # Blue shade
                alpha=0.7,         # Transparency
                s=100,             # Marker size (scatter uses size instead of markersize)
                label='Savings')

    # Annotate each point with the exact values for income, expenses, and savings
    for i in range(len(df)):
        # Income annotation (slightly above the point)
        plt.annotate(f'{df["Income"][i]:.2f}', (df['Month'][i], df['Income'][i]), 
                     textcoords="offset points", xytext=(10,10), ha='center', fontsize=9)
        
        # Expenses annotation (slightly below the point)
        plt.annotate(f'{df["Expenses"][i]:.2f}', (df['Month'][i], df['Expenses'][i]), 
                     textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
        
        # Savings annotation (a bit further below the point)
        plt.annotate(f'{df["Savings"][i]:.2f}', (df['Month'][i], df['Savings'][i]), 
                     textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

    # Add titles, labels, and grid for better appearance
    plt.title('Personal Finance Tracker (Monthly)', fontsize=20, color="#333")
    plt.xlabel('Month', fontsize=20)
    plt.ylabel('Amount in Rs', fontsize=12)
    plt.legend(loc='upper left', fontsize=20)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)

    # Tweak layout to make it look fabulous
    plt.tight_layout()

    # Display the plot inside the Tkinter window
    figure = plt.gcf()
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# GUI Design
tk.Label(root, text="Month").pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

tk.Label(root, text="Income").pack(pady=5)
income_entry = tk.Entry(root)
income_entry.pack(pady=5)

tk.Label(root, text="Expenses").pack(pady=5)
expenses_entry = tk.Entry(root)
expenses_entry.pack(pady=5)

tk.Button(root, text="Add Data", command=add_data).pack(pady=10)
tk.Button(root, text="Visualize Data", command=visualize_data).pack(pady=10)

root.mainloop()
