import smtplib
import string  
import random 
import sys 
import mysql.connector

def insert_data(email,password):
    cnx = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "email_verify"
    )

    cursor = cnx.cursor()
    cursor.execute(f"insert into User_email_verify(User_Email,Verification_Code) values('{email}','{password}')")
    cnx.commit()



def send_mail(email,passwd):
    reciever = email
    print(reciever)
    msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % ('mobmistridesk@gmail.com', reciever, f"your OTP:{passwd}", f"Your OTP is {passwd}")
    try:
        
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("mobmistridesk@gmail.com","mobmistri@007")
        mail.sendmail("mobmistridesk@gmail.com",reciever,msg)
        mail.close()
        return "success"
    except:
        return "failed to send a message"
     
def rand_pass():  
    return (random.randint(999,9999) +1)                        
       
    

if __name__ == "__main__":
    passwd = rand_pass()
    email = sys.argv[1]
    # print(passwd)
    status = send_mail(email,passwd)
    insert_data(email,passwd)
    x = {
        'status':f"{status}",
        "OTP":f"{passwd}"
    }
    print(x)
