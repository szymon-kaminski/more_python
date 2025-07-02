import os
import pickle
import pytest
import sys
from unittest.mock import patch


CLI_SCRIPT = "testy_do_lekcji_M08L04.budget"


def test_add_command(tmp_path, monkeypatch):
    # Izolacja bazy w tmp_path
    db_file = tmp_path / "budget.db"
    monkeypatch.setenv("BUDGET_DB", str(db_file))

    # Symulacja wywołania CLI: python -m budget add 100 Test expense
    test_args = [sys.executable, "-m", CLI_SCRIPT, "add", "100", "Test expense"]
    with patch.object(sys, 'argv', test_args):
        import budget
        budget.cli()

    # Sprawdzenie pliku pickle
    with open(db_file, 'rb') as f:
        expenses = pickle.load(f)
    assert any(e.amount == 100 and e.description == "Test expense" for e in expenses)

