import SendMail as sm

sender = "me@gmail.com"
sender_password = "password_for_me@gmail.com"
receiver = "you@your_provider.com"
subject = "the subject"
message = "the message"

mail_ = sm.SendMail(sender, sender_password, receiver, subject, message)
mail_.SendEmail()



