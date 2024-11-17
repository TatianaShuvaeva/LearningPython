from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vorhersage:
    datum_zeit: datetime
    temperature: float
    min_temperature: float
    max_temperature: float
