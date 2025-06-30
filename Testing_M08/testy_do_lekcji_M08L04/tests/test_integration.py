import os
import pytest
from testy_do_lekcji_M08L04.budget import Expense, save_budget, read_or_init_budget, find_next_id

def test_save_load_expenses():
    if os.path.exists('budget.db'):
        os.remove('budget.db')
        
    expenses = []
    expense_id = find_next_id(expenses)
    new_expense = Expense(id=expense_id, amount=500.0, description="Integration test expense")
    expenses.append(new_expense)
    save_budget(expenses)
    
    loaded_expenses = read_or_init_budget()
    assert len(loaded_expenses) == 1
    loaded = loaded_expenses[0]
    assert loaded.id == expense_id
    assert loaded.amount == 500.0
    assert loaded.description == "Integration test expense"