import mysql.connector
from mysql.connector import MySQLConnection
from configparser import ConfigParser
from datetime import date

def read_db_config(filename='config_file.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db        

def add_user():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    name = input('Enter Your Name  : ')
    phone = input('Enter Your Phone  : ')
    email = input('Enter Your Email  : ')
    sql = 'insert into user(name,phone,email) values ("' +name+ '","'+phone+ '","'+email+'");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nNew User added successfully')
    wait = input('\n\n\n Press any key to continue....')

def add_librarian():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    name = input('Enter Your Name  : ')
    phone = input('Enter Your Phone  : ')
    email = input('Enter Your Email  : ')
    sql = 'insert into librarian(name,phone,email) values ("' +name+ '","'+phone+ '","'+email+'");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nNew Librarian added successfully')
    wait = input('\n\n\n Press any key to continue....')

def add_book():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    title = input('Enter Book Title :')
    author = input('Enter Book Author : ')
    publisher = input('Enter Book Publisher : ')
    sql = 'insert into book(title,author,publisher,book_status) values ( "' +title+ '","' + author+'","'+publisher+'","available");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nNew Book added successfully')
    wait = input('\n\n\n Press any key to continue....')
      
def update_user():     # For Modifying User Details
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    print('Modify User Details Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Phone')
    print('\n3. Email id')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'phone'
    if choice == 3:
        field = 'email'
    user_id =input('Enter User ID :')
    value = input('Enter new value to update :')
    if field=='phone':
        sql = 'update user set '+ field +' = '+value+' where userid = '+user_id+';'
    else:
        sql = 'update user set '+ field +' = "'+value+'" where userid = '+user_id+';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('User Details Updated.....')
    wait = input('\n\n\n Press any key to continue....')

def update_bookdetails():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    print('Modify BOOK Details Screen')
    print('-'*120)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n3. Book Publisher')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'title' 
    if choice == 2:
        field = 'author'
    if choice == 3:
        field = 'publisher'
    book_id = input('Enter Book ID :')
    value = input('Enter new value for update :')
    if field =='title' or field =='author' or field == 'publisher':
        sql = 'update book set ' + field + ' = "'+value+'" where bookid = '+book_id+';'
        cursor.execute(sql)
        conn.commit()
        conn.close()
        print('\n\n\nBook details Updated.....')
        wait = input('\n\n\n Press any key to continue....')
      
def delete_user():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    user_id =input('Enter User ID to be deleted:')  
    sql = 'DELETE FROM user WHERE userid ='+user_id+ ';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('User Deleted.....')
    wait = input('\n\n\n Press any key to continue....')
     
def delete_book():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    book_id =input('Enter Book ID to be deleted:')  
    sql = 'DELETE FROM book WHERE bookid ='+book_id+ ';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('Book Deleted.....')
    wait = input('\n\n\n Press any key to continue....')
     
def books_details():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    book_id=input('Enter Book ID for Book details:')
    sql = 'select * from book where bookid ='+book_id + ';'  
    cursor.execute(sql)  
    result = cursor.fetchone()  
    print('Book Details.....',result)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
        
def books_available():    # List of available books in library
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    print('\n BOOK TITLES - Available')
    print('-'*120)
    sql = 'select * from book where book_status = "available";'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for rows in rows:
        print(rows) 
    conn.close()      
    wait = input('\n\n\nPress any key to continue.....')
      
def rent_book():    # Book issue/checkout
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    print('\n BOOK ISSUE SCREEN ')
    print('-'*120)
    book_id = input('Enter Book ID : ')
    user_id  = input('Enter User ID : ')
    try:
        sql = 'select book_status from book where bookid ='+book_id + ';'
        cursor.execute(sql)
        result = cursor.fetchone() 
        for row in result:
            bk_status=row
    except:
        print("Error: Unable to fetch data") 
        conn.close()
     
    today = date.today()
    if bk_status == 'available':
        print("This book is Available")
        sql = 'insert into book_rental(book_id, user_id, doi) values('+book_id+','+user_id+',"'+str(today)+'");'
        cursor.execute(sql)
        conn.commit()    
        sql_book = 'update book set book_status= "issued" where bookid ='+book_id + ';'
        cursor.execute(sql_book)
        conn.commit()
        print('\n\n\n Book issued successfully')
    else:
        print("Not Available- Book already Issued")     
    wait = input('\n\n\n Press any key to continue....')

def return_book():
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    print('\n BOOK RETURN SCREEN ')
    print('-'*120)
    book_id = input('Enter Book  ID : ')
    user_id = input('Enter User ID : ')
    today1 =date.today()
    sql = 'update book_rental set dor ="'+str(today1)+'" where book_id ='+book_id +';'
    cursor.execute(sql)
    conn.commit()
    sql2='update book set book_status ="available" where bookid ='+book_id +';'
    cursor.execute(sql2)
    conn.commit()    
    conn.close() 
    print('\n\n\n Book returned successfully')     
    wait = input('\n\n\nPress any key to continue.....')
  
def fine_calc():     # Fine Amount 
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    print("Fine Calculation-->")
    book_id = input('Enter Book  ID : ')
    user_id = input('Enter User ID : ')
    sql='select doi from book_rental where book_id='+book_id +' and user_id='+user_id +';'
    cursor.execute(sql)
    result1 = cursor.fetchone() 
    for r in result1:
        di=r
    sql1='select dor from book_rental where book_id='+book_id +' and user_id='+user_id +';'
    cursor.execute(sql1)
    result2 = cursor.fetchone() 
    for i in result2:
        dr=i
    t_days = (dr - di).days
    print("Book Returned in",t_days,"Days")
    if t_days>14 and t_days<=20:
        print("REMINDER--Hey User! Book is Issued for more than 2 Weeks. Please Return...")
    elif t_days>=21:
        l=list()
        fine_amt=0
        fine_days=t_days-20
        day_diff=fine_days//5
        for i in range(1,day_diff+1):
            fine=20+(i-1)*5
            l.append(fine)
        for i in range(day_diff):
            fine_amt+=l[i]
        print("Fine Amount is Rs.",fine_amt)   
    sql3='update book_rental set fine = "'+str(fine_amt)+'"  where book_id ='+book_id +' and user_id='+user_id +';'
    cursor.execute(sql3)
    conn.commit()
    conn.close() 
    wait = input('\n\n\nPress any key to continue.....')

def user_signin(email,phone):
    dbconfig=read_db_config()
    conn=MySQLConnection(**dbconfig)
    cursor = conn.cursor()  
    sql = 'select 1 from user where email = "'+email+'" and phone="'+phone+'";'
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    if result is not None:
        for r in result:
            if r==1:
                return True
    else:
        return False      