import pickle
import sys
from unittest.mock import patch

from testy_do_lekcji_M08L04.budget import cli
import testy_do_lekcji_M08L04.budget as budget


def test_add_command(tmp_path, monkeypatch):
    # Izolacja bazy w tmp_path
    db_file = tmp_path / "budget.db"
    monkeypatch.setenv("BUDGET_DB", str(db_file))

    # Symulacja wywołania CLI: budget add 100 Test expense
    test_args = ["budget", "add", "100", "Test expense"]
    with patch.object(sys, 'argv', test_args):
        cli()

    # Sprawdzenie, czy wydatek został zapisany
    loaded = budget.read_or_init_budget()
    assert any(e.amount == 100 and e.description == "Test expense" for e in loaded)

    # Sprawdzenie pliku pickle bezpośrednio
    with open(db_file, 'rb') as f:
        expenses = pickle.load(f)
    assert any(e.amount == 100 and e.description == "Test expense" for e in expenses)


def test_report_and_total(tmp_path, monkeypatch, capsys):
    # Izolacja bazy w tmp_path
    db_file = tmp_path / "budget.db"
    monkeypatch.setenv("BUDGET_DB", str(db_file))

    # Przygotuj bazę z dwoma wydatkami
    from testy_do_lekcji_M08L04.budget import save_budget, Expense
    expenses = [
        Expense(id=1, amount=100, description="a"),
        Expense(id=2, amount=200.5, description="b")
    ]
    save_budget(expenses)

    # Symulacja wywołania CLI: budget report
    test_args = ["budget", "report"]
    with patch.object(sys, 'argv', test_args):
        cli()

    # Przechwycenie i analiza wyjścia
    captured = capsys.readouterr()
    output = captured.out

    assert "a" in output and "100.00" in output
    assert "b" in output and "200.50" in output
    assert "Total=" in output and "300.50" in output

