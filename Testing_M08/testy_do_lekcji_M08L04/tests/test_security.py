import os
import pytest
from testy_do_lekcji_M08L04.budget import Expense, save_budget, read_or_init_budget


def test_naughty_strings_security(tmp_path, monkeypatch):
    db_file = tmp_path / "budget.db"
    monkeypatch.setenv("BUDGET_DB", str(db_file))  # jeśli kod obsługuje env var, inaczej: monkeypatch DB_FILENAME

    naughty_strings = [
        "undefined", "undef", "null", "NULL", "nil", "(null)", "NIL",
        "true", "false", "True", "False", "None", "hasOwnProperty",
        "\", "\\", "0", "1", "1.00", "$1.00", "1/2",
    ]

    for naughty in naughty_strings:
    try:
        exp = Expense(id=1, amount=100.0, description=naughty)
    except Exception as e:
        pytest.fail(f"Cannot instantiate Expense with description '{naughty}': {e}")
