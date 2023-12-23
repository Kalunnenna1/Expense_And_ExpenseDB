from expense import Expense, ExpenseDatabase

# Initialization of Expense:
expense = Expense()
expense = Expense("My_monthly_school_fee", 30.00)
print(expense.to_dict())

expense.update(new_title="AltSchoolAfrica", new_amount=35.0)
print(expense.to_dict())

# Initialization of Expense DB:
expense_db = ExpenseDB()
expense_db.add_expense(expense)
print(expense_db.to_dict())

def add_expense(self, expense):
    print(f"(add_expense: {self.expense}")

# Add expenses
expense_db = ExpenseDB()
expense_db.add_expense("My_monthly_school_fee", 30.00)
expense_db.add_expense("My_monthly_data", 40.00)
expense_db.add_expense("Additional_resources", 20.00)
print(expense_db.to_dict())

# Print all expenses
print("All expenses:")
for expense in expense_db.to_dict():
    print(expense)

# Update an expense
first_expense_id = expense_db.expenses[0].id
expense_db.get_expense_by_id(first_expense_id).update(title="Monthly_school_fees", amount=30.00)

# Print all expenses after update
print("\nAll expenses after update:")
for expense in expense_db.to_dict():
    print(expense)

# Remove an expense
expense_db.remove_expense(first_expense_id)

# Print all expenses after removal
print("\nAll expenses after removal:")
for expense in expense_db.to_dict():
    print(expense)

# Get expenses by title
print("\nExpenses with title 'Additional_resources':")
for expense in expense_db.get_expense_by_title("Additional_resources"):
    print(expense.to_dict())


