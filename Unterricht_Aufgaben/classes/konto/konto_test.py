from konto import Konto

import pytest


# Überprüfung der Funktionalität raise ValueError(" Der Umsatz muss größer als 0, aber kleiner als der maximalen Tagesumsatz sein"))
@pytest.mark.parametrize("falscher_neue_umsatz", [-0.1, -0.01, -1, 201, 200.01])
def test_umsatz_set_raises_value_error(falscher_neue_umsatz: float):
    with pytest.raises(ValueError, match="Der Umsatz muss größer als 0, aber kleiner als der maximalen Tagesumsatz sein"):
        konto1 = Konto("Schmidt", 12345678911, 5000.67, 200)
        konto1.umsatz = falscher_neue_umsatz


def test_richtiger_umsatz_set():
    konto = Konto("Schmidt", 12345678911, 250.67, 200)
    konto.umsatz = 0
    konto.umsatz += 0.01
    konto.umsatz += 100
    konto.umsatz += 99.99

    assert konto.umsatz == 200


def test_eq_kontonummer_false():
    konto1 = Konto("Müller", 21345678910, 250.67, 200)
    konto2 = Konto("Müller", 12345678911, 250.67, 200)
    
    assert konto1 != konto2

def test_eq_inhaber_false():
    konto1 = Konto("Schmidt", 12345678911, 250.67, 200)
    konto2 = Konto("Müller", 12345678911, 250.67, 200)
   
    assert konto1 != konto2

def test_eq_kontostant_false():
    konto1 = Konto("Schmidt", 12345678911, 250.67, 150)
    konto2 = Konto("Schmidt", 12345678911, 200.67, 150)
    
    assert konto1 != konto2

def test_eq_umsatz_false():
    konto1 = Konto("Schmidt", 12345678911, 200.67, 150)
    konto2 = Konto("Schmidt", 12345678911, 200.67, 150)
    konto1.umsatz = 1
   
    assert konto1 != konto2

def test_eq_inhaber_true():
    konto1 = Konto("Schmidt", 12345678911, 5000.67, 200)
    konto2 = Konto("schMidt", 12345678911, 5000.67, 200)
    
    assert konto1 == konto2


def test_eq_umsatz_true():
    konto1 = Konto("Schmidt", 12345678911, 250.67, 200)
    konto2 = Konto("Schmidt", 12345678911, 200.67, 200)
    konto1.umsatz = 100
    konto2.umsatz = 50

    assert konto1 == konto2
