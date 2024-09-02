class Boat():
    def __init__(self, length):
        if length > 5 and length <= 20:
            self._length = length
        else:
            print("Ungültinge Angabe")
            exit(10)

    def __str__(self):
        return f"Boat - Length {self._length}m "


class Motorboat(Boat):
    def __init__(self, length, power):
        # self._length = length
        super().__init__(length)
        self._power = power

    def setLength(self, length):
        self._length = length

    def __str__(self):
        return f"Motorboat - Length {self._length}m  Power {self._power}"


class SpeedBoat(Motorboat):
    def __init__(self, l, p, d):
        super().__init__(l, p)
        self._drive = d

    def __str__(self):
        return f"Speedboat - Length {self._length}m  Power {self._power} - Drive {self._drive}"
