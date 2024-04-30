import tkinter as tk
from tkinter import ttk

def calculate_compound_interest():
    principal_amount = float(principal_entry.get())
    rate_of_interest = float(rate_entry.get()) / 100
    time_period = int(time_period_entry.get())
    no_of_years = int(no_of_years_entry.get())

    final_amount = principal_amount * (1 + rate_of_interest / time_period) ** (time_period * no_of_years)
    simple_interest_amount = principal_amount * (1 + rate_of_interest * no_of_years)
    amount_saved = final_amount - simple_interest_amount

    result_label.config(text=f'Final amount: {final_amount:,.2f}\nSimple interest amount: {simple_interest_amount:,.2f}\nAmount saved: {amount_saved:,.2f}')

root = tk.Tk()
root.title('Compound Interest Calculator')

principal_label = ttk.Label(root, text='Principal amount:')
principal_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
principal_entry = ttk.Entry(root, width=10)
principal_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

rate_label = ttk.Label(root, text='Rate of interest (%):')
rate_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
rate_entry = ttk.Entry(root, width=10)
rate_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

time_period_label = ttk.Label(root, text='Number of times interest is compounded per year:')
time_period_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
time_period_entry = ttk.Entry(root, width=10)
time_period_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

no_of_years_label = ttk.Label(root, text='Number of years:')
no_of_years_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
no_of_years_entry = ttk.Entry(root, width=10)
no_of_years_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')

calculate_button = ttk.Button(root, text='Calculate', command=calculate_compound_interest)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text='')
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
