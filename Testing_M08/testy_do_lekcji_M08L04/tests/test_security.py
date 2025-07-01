import os
import pytest
from testy_do_lekcji_M08L04.budget import Expense, save_budget, read_or_init_budget


def test_naughty_strings_security(tmp_path, monkeypatch):
    pass