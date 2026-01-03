import pytest
import sys
import os

# Ensure project root is on sys.path so tests can import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from quem_faz_pokemon import eliminar_jogadores


def test_single_elimination():
    jogadores = {
        "A": {"erros": 5, "tipos": []},
        "B": {"erros": 0, "tipos": []},
    }

    eliminados = eliminar_jogadores(jogadores, 5)

    assert "A" in eliminados
    assert "A" not in jogadores
    assert "B" in jogadores


def test_multiple_elimination():
    jogadores = {
        "A": {"erros": 6, "tipos": []},
        "B": {"erros": 5, "tipos": []},
        "C": {"erros": 1, "tipos": []},
    }

    eliminados = eliminar_jogadores(jogadores, 5)

    assert set(eliminados) == {"A", "B"}
    assert "C" in jogadores


def test_no_elimination():
    jogadores = {
        "A": {"erros": 1},
        "B": {"erros": 4},
    }

    eliminados = eliminar_jogadores(jogadores, 5)

    assert eliminados == []
    assert set(jogadores.keys()) == {"A", "B"}
