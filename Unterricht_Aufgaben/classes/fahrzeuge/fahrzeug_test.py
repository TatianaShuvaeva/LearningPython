from fahrzeug import Fahrzeug
from lkw import LKW
from pkw import PKW

import pytest


# Überprüfung der Funktionalität raise ValueError("Kilometerstand muss positiv sein."))
def test_init_test_negative_km_stand_raises_value_error():
    with pytest.raises(ValueError, match="Kilometerstand muss positiv sein."):
        Fahrzeug("BMW", 2020, -100, "Rot")


# Überprüfung set_km_stand
def test_set_km_stand_test_neu_km_stand():
    f = Fahrzeug("BMW", 2022, 10000, "schwarz")
    f.set_km_stand(12000)

    assert f.get_km_stand() == 12000, 'set_km_stand soll man steigen'


# Überprüfung der Funktionalität raise ValueError("Neuer Kilometerstand muss größer oder gleich alter sein.")
def test_set_km_stand_test_value_error():
    with pytest.raises(ValueError, match="Neuer Kilometerstand muss größer oder gleich alter sein."):
        f = Fahrzeug("BMW", 2020, 100, "Rot")
        f.set_km_stand(90)
