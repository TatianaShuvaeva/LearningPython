'''connectieren einer MSSQL Datenbank '''

#diese Klasse wird für die Connectierung benötigt
import pyodbc

# Verbindungsdaten
# server = '172.25.146.215\\SQLEXPRESS'
server = 'DESKTOP-N5CT0P9\SQLEXPRESS'
database = 'videogames'
username = 'sa'
password = 'Passwort01'
# driver = '{ODBC Driver 18 for SQL Server}'  # Beispiel für den Treibernamen, an deine Version anpassen

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;'
# connectionString = f'SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Verbindungsaufbau Connectionstring ähnlich wie bei C#
# with pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
conn = pyodbc.connect(connectionString) 
# Instanzieren eines cursorss
cursor = conn.cursor()

# Tabelle erstellen (Beispiel)
cursor.execute('''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Produkte' and xtype='U')
    CREATE TABLE Produkte (id INT PRIMARY KEY, name NVARCHAR(250), quantity INT)
''')
conn.commit()

# Daten einfügen
cursor.execute("INSERT INTO Produkte (id, name, quantity) VALUES (?, ?, ?)", (1, 'Game of Heiko', 23))
cursor.execute("INSERT INTO Produkte (id, name, quantity) VALUES (?, ?, ?)", (2, 'Game of Markus', 24))
cursor.execute("INSERT INTO Produkte (id, name, quantity) VALUES (?, ?, ?)", (3, 'Game of IBB', 25))
conn.commit()

# Daten abfragen
cursor.execute("SELECT * FROM Produkte")
for row in cursor:
    print(row)
