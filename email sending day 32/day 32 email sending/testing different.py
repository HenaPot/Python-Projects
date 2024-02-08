import smtplib

my_email = "testmail@yahoo.com"
# this is the actual passoword and thats why this isnt working,
# we cannot generate a password at yahoo rn because the fature has been unavailable last 4 months
password = "testpassword"

connection = smtplib.SMTP("smtp.mail.yahoo.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="fakemail@gmail.com",
    msg="Subject:Hello\n\nTrying something new."
)
connection.close()