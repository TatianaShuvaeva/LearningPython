def get_leerzeichen(wort) -> str:
    """
    Diese Funktion fügt Leerzeichen vor ein Wort ein,
    sodass die Gesamtlänge des resultierenden Strings 70 beträgt.

    Parameters:
    wort (str): Das Wort, dem Leerzeichen hinzugefügt werden sollen.

    Returns:
    str: Der resultierende String mit Leerzeichen vor dem Wort.
    """
    wort_len = len(wort)
    anzahl_links = 70 - wort_len
    leerzeichen = " " * anzahl_links
    ergebniss = leerzeichen + wort
    return ergebniss


str1 = 'blblblblb'
ergebniss1 = get_leerzeichen(str1)


# Email configuration
sender_email = "sender_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "your_email_password"

# Create the email message
subject = "Leerzeichen Result"
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the result to the email body
body = f"Result: {ergebniss1}"
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)


# def ridht_justify(str):
#     pro=" "*(70-len(str))
#     justify=pro+str

# str='allen'
# ridht_justify(justify)


# def print_zweimal(str):
#     print(str)
#     print(str)

# def zweimal_cat(teil1,teil2):
#     cat = teil1 + " " + teil2
#     print_zweimal(cat)

# zeile1="Hallo Welt"
# zeile2="from Tatiana"
# zweimal_cat(zeile1,zeile2)
