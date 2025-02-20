import imaplib
import email
import json
import os
import pickle

class Gmail:
    def __init__(self,user,passwd,mailbox="INBOX"):
        self.user=user
        self.passwd=passwd
        self.mailbox=mailbox
        self.mail=None

    def connection(self):
        try:
            self.mail=imaplib.IMAP4_SSL("imap.gmail.com")
            self.mail.login(self.user,self.passwd)
            self.mail.select(self.mailbox)
            print("Connection Successful")
        except Exception as e:
            print("Connection Failed")

    def get_emails(self,max_emails=10):
        result,data=self.mail.search(None,"ALL")
        email_ids=data[0].split()[-max_emails:]
        email_list=[]

        for i in email_ids:
            result,data=self.mail.fetch(i,"(RFC822)")
            x=data[0][1]
            msg=email.message_from_bytes(x)

            header=self.email_header(msg)
            email_list.append(header)

        self.save_emails(email_list)

    def email_header(self,msg):
        subject=msg["Subject"]
        e_from=msg["From"]
        date=msg["Date"]
        ebody,words,lines,attachments,Total_attachment=self.content(msg)

        return {
            "Subject":subject,
            "Date":date,
            "From":e_from,
            "Words":words,
            "Lines":lines,
            "No of Attachment":Total_attachment,
            "Attachments":attachments
        }

    def content(self,msg):
        ebody=""
        words=0
        lines=0
        attachments=[]

        for part in msg.walk():
            if part.get_content_type()=="text/plain":
                ebody=part.get_payload(decode=True).decode(errors="ignore")
                words=len(ebody.split())
                lines=len(ebody.split("\n"))

            if part.get_filename():
                file=part.get_filename()
                attachments.append(file)
                self.save_attachment(file,part)

        Total_attachment=len(attachments)
        return ebody, words, lines, attachments,Total_attachment

    def save_attachment(self,file,part):
        os.makedirs("Attachments",exist_ok=True)
        file_path=os.path.join("Attachments",file)
        with open(file_path,"wb") as f:
            f.write(part.get_payload(decode=True))

    def save_emails(self,email_list):
        with open("Emails_p.json","wb") as f:
            pickle.dump(email_list, f)

    def close(self):
        self.mail.logout()


user_id=input("Enter the User email :")
passwd=input("Enter the App password :")

obj=Gmail(user_id,passwd)
obj.connection()
obj.get_emails(5) 
obj.close()

with open("Emails_p.json", "rb") as f:
    email_list = pickle.load(f)

with open("Emails.json", "w") as f:
    json.dump(email_list, f, indent=4)