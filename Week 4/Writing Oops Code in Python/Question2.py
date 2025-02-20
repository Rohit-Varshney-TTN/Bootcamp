import imaplib
import email
import json
import os

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

        email_type={ "jobs":[], "attachments":[],"pictures":[] }

        for i in email_ids:
            result,data=self.mail.fetch(i,"(RFC822)")
            x=data[0][1]
            msg=email.message_from_bytes(x)
            header=self.email_header(msg)

            if self.job_email(msg):
                email_type["jobs"].append(header)

            if self.attachment_email(msg):
                email_type["attachments"].append(header)

            if self.picture_emails(msg):
                email_type["pictures"].append(header)

        self.save_emails(email_type)

    def job_email(self, msg):
        subject=""
        if msg["Subject"]:
            subject=msg["Subject"].lower()

        body=self.extract_body(msg).lower()
        job_keywords=["job","hiring","position","vacancy","career"]

        for keyword in job_keywords:
            if keyword in subject or keyword in body:
                return True
        return False


    def attachment_email(self,msg):
        for part in msg.walk():
            if part.get_filename():
                return True
        return False

    def picture_emails(self,msg):
        picture_extensions=[".jpg",".jpeg",".png",".gif"]
        for part in msg.walk():
            if part.get_filename():
                file_name=part.get_filename().lower()
                if any(file_name.endswith(t) for t in picture_extensions):
                    return True
        return False

    def email_header(self,msg):
        subject=msg["Subject"]
        e_from=msg["From"]
        date=msg["Date"]
        ebody,words,lines,attachments,total_attachments=self.content(msg)

        return {
            "Subject":subject,
            "Date":date,
            "From":e_from,
            "Words":words,
            "Lines":lines,
            "No of Attachment":total_attachments,
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
        return ebody,words,lines,attachments,len(attachments)

    def save_attachment(self,file,part):
        os.makedirs("Attachments",exist_ok=True)
        file_path=os.path.join("Attachments",file)
        with open(file_path,"wb") as f:
            f.write(part.get_payload(decode=True))

    def extract_body(self,msg):
        for part in msg.walk():
            if part.get_content_type()=="text/plain":
                return part.get_payload(decode=True).decode(errors="ignore")
        return ""

    def save_emails(self,email_type):
        with open("Emails2.json","w") as f:
            json.dump(email_type,f,indent=4)
    def close(self):
        self.mail.logout()

user_id=input("Enter the User email: ")
passwd=input("Enter the App password: ")
obj=Gmail(user_id, passwd)
obj.connection()
obj.get_emails(5)
obj.close()