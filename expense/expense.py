# Expense Class representing an Individual expense
# Attributes to the object 'class'
# Method to describe the behaviour of the object

import uuid
from datetime import datetime

class Expense:
    pass
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())              
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, new_title=None, new_amount=None):
        if new_title is not None:
            self.title = new_title
        if new_amount is not None:
            self.amount = new_amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense):
        self.expenses.remove(expense)

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]


# Initialization of Expense:
expense = Expense("My_monthly_school_fee", 30.00)
print(expense.to_dict())

expense.update(new_title="AltSchoolAfrica", new_amount=100.0)
print(expense.to_dict())


# Initialization of Expense DB:
expense_db = ExpenseDB()
expense_db.add_expense(expense)
print(expense_db.to_dict())

def add_expense(self, expense):
    print(f"(add_expense: {self.expense}")
