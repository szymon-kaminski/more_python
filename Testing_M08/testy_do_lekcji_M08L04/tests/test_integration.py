import pytest
from budget import Expense, save_budget, read_or_init_budget, find_next_id

def test_save_load_expenses():
    if os.path.exists('budget.db'):
        os.remove('budget.db')
        
    expenses = []
    new_expense = Expense(500, "Integration test expense", find_next_id(expenses))
    expenses.append(new_expense)
    save_budget(expenses)
    
    loaded_expenses = read_or_init_budget()
    assert len(loaded_expenses) == 1
    assert loaded_expenses[0].amount == 500
    assert loaded_expenses[0].description == "Integration test expense"