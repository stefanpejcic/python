from passlib.hash import pbkdf2_sha256
import getpass
import mysql.connector
def enc_pass(pwd):
    hash=pbkdf2_sha256.encrypt(pwd,rounds=200,salt_size=16)
    return hash
def con_database(pwd):
    cnx=mysql.connector.connect(user='*****',password='*****',host='*******',database='******')
    cursor=cnx.cursor() 
    try:
        query=("INSERT INTO usr VALUES(%s,%s);")
        data=(us,pwd)
        cursor.execute(query,data)
        cnx.commit()
        print("user recorded")
    except Exception as e:
        print(e)
        
def user_data():
    global us
    print("Please enter username:")
    us=input(">>")
    print("Please enter password:")
    pwd=getpass.getpass(">>")
    
    return pwd
if __name__=="__main__":
    con_database(enc_pass(user_data()))
