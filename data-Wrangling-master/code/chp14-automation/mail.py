import smtplib


def mail(subject):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("automailsforme@gmail.com", "automailsforme123")

    # message to be sent
    message = subject

    # sending the mail
    s.sendmail("automailsforme@gmail.com", "tinto.t.kurian@gmail.com", message)

    # terminating the session
    s.quit()


def main():
    mail("This is an automated mail")

if __name__ == '__main__':
    main()
