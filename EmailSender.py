import smtplib
email="aaaaaaaa@gmail.com"
reciver_email="aaaaaaaa@gmail.com"
subject= "Hello"
message= "Not spam"
text=f"Subject: {subject}\n\n{message}"
def mandarCorreo(email,reciver_email,text):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,"password to your account")#search google app passwords, there you will get a 16 chara key 
    server.sendmail(email,reciver_email,text)
    server.close

for i in range (10):
    mandarCorreo(email,reciver_email,text)
    print("Good")
