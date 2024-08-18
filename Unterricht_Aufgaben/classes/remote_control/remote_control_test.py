from remote_control import RemoteControl


# Lautstärkeprüfung
def test_get_lautstärke(): 
    rc = RemoteControl(2)
    assert rc.get_lautstärke() == 0, 'Lautstärke soll man 0 sein'

# Überprüfung max Lautstärke
def test_plus_lautstärke_10_max():
    # Arrange
    rc = RemoteControl(2)
    
    # Act
    for _ in range(0,11):
        rc.plus_lautstärke()
    
    # Assert
    assert rc.get_lautstärke() == 10, '10 - max Lautstärke'


def test_minus_lautstärke(): 
    # Arrange
    rc = RemoteControl(5)
    for _ in range(0,4):
        rc.plus_lautstärke()

    # Arrange
    for _ in range(4,0,-1):
        rc.minus_lautstärke()
    # Assert
    assert rc.get_lautstärke() == 0, 'Lautstärke soll man 0 sein'

 
# Prüfung des aktuellen Programms
def test_aktuelles_programm():
    # Arrange
    rc = RemoteControl(5)
    
    # Arrange, Assert
    assert rc.aktuelles_programm == None, 'Soll None sein'

def test_set_programm_name():
    # Arrange
    rc = RemoteControl(5)
    
    # Arrange
    rc.setProgramName("KiKA")
    
    # Assert
    assert rc.aktuelles_programm == "KiKA", 'Soll "KiKA" sein'

def test_next_programm():
    # Arrange
    rc = RemoteControl(5)
    rc.setProgramName("KiKA")
    
    # Act
    rc.nextProgram()
    rc.nextProgram()
    
    # Assert
    assert rc.aktuelles_programm == "ZDF", 'Soll "ZDF" sein'

#rc4.printProgram()
