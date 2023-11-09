import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="admin1234",
    database="SCHOOLS"
)


""" ------------------------CREATE TABLE-------------  """
def create_student_table(table_name):
    query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            STUDENT_ID INT PRIMARY KEY AUTO_INCREMENT,
            FIRST_NAME VARCHAR(50) NOT NULL,
            LAST_NAME VARCHAR(50) NOT NULL,
            DATE_OF_BIRTH DATE
        );
    """
    cursor = connection.cursor()
    cursor.execute(query)



def create_teacher_table(table_name):
    query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            TEACHER_ID INT PRIMARY KEY AUTO_INCREMENT,
            FIRST_NAME VARCHAR(50) NOT NULL,
            LAST_NAME VARCHAR(50) NOT NULL,
            SUBJECT VARCHAR(50) NOT NULL
        );
    """
    cursor = connection.cursor()
    cursor.execute(query)




def create_course_table(table_name):
    query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            COURSE_ID INT PRIMARY KEY,
            COURSE_NAME VARCHAR(50) NOT NULL,
            TEACHER_ID INT,
            SCHEDULE VARCHAR(50) NOT NULL,
            CONSTRAINT CUR_FK FOREIGN KEY (TEACHER_ID) REFERENCES TEACHERS(TEACHER_ID)

        );
    """
    cursor = connection.cursor()
    cursor.execute(query)



def create_attendance_table(table_name):
    query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            ATTENDANCE_ID INT PRIMARY KEY AUTO_INCREMENT,
            COURSE_ID INT,
            STUDENT_ID INT,
            `CURRENT_DATE` DATE NULL,
            FINE INT,
            CONSTRAINT COURSE_FK FOREIGN KEY (COURSE_ID) REFERENCES COURSES(COURSE_ID),
            CONSTRAINT STUDENT_FK FOREIGN KEY (STUDENT_ID) REFERENCES STUDENTS(STUDENT_ID)
        );
    """
    cursor = connection.cursor()
    cursor.execute(query)


""" ---------------------------------   INSERT DATE  ---------------------- """  

def insert_a_studnet(table_name, first_name, last_name, date_of_birth):
    query = f"""
        INSERT INTO {table_name} ( FIRST_NAME, LAST_NAME, DATE_OF_BIRTH)
        VALUES ( %s, %s, %s)
    """
    cursor = connection.cursor()
    cursor.execute(query, ( first_name, last_name, date_of_birth))
    connection.commit()




def insert_a_teacher(table_name, first_name, last_name, subject):
    query = f"""
        INSERT INTO {table_name} ( FIRST_NAME, LAST_NAME, SUBJECT)
        VALUES ( %s, %s, %s)
    """
    cursor = connection.cursor()
    cursor.execute(query, (first_name, last_name, subject))
    connection.commit()




def insert_a_course(table_name,course_id,course_name,teacher_id,schedule):
    query = f"""
        INSERT INTO {table_name} (COURSE_ID, COURSE_NAME, TEACHER_ID, SCHEDULE)
        VALUES (%s, %s, %s, %s)
   
    """
    cursor = connection.cursor()
    cursor.execute(query,(course_id,course_name,teacher_id,schedule))
    connection.commit()



def insert_a_attendance(table_name, course_id, student_id, current_date, fine):
    query = f"""
        INSERT INTO {table_name} (course_id, student_id, `current_date`, fine)
        VALUES (%s, %s, %s, %s)
    """
    cursor = connection.cursor()
    cursor.execute(query, (course_id, student_id, current_date, fine))
    connection.commit()


""" --------------------UPDATE DATE -------------------------- """

def update_date_att(table_name, student_id, fine):
    query = f"""
        UPDATE {table_name} SET fine = %s
        WHERE student_id = %s
    """
    cursor = connection.cursor()
    cursor.execute(query, (student_id, fine))
    connection.commit()
    print("\nSuccessfully Updated\n")

def update_date_att(table_name,fine,student_id):
    query = f"""
        UPDATE {table_name} SET student_id = %s
        WHERE fine = %s
    """
    cursor = connection.cursor()
    cursor.execute(query, (fine,student_id))
    connection.commit()
    print("\nSuccessfully Updated\n")




while True:
    print("STUDENTS")
    print("TEACHERS")
    print("COURSES")
    print("ATTENDANCES")
    print("If you want to create a table, you must follow the table names above")
    print("-----------------------------------------------------------------------\n")

    print("----1.   create table \n")
    print("----2.   insert a inforamtion \n")
    print("----3.   update inforamtion\n")
    print("----4.   logout\n")

    op = int(input("choice your option : "))

    if op == 1:
        name = input("Enter Your Table name: ")

        if name.lower() == "students":
            create_student_table(name)
            print("\n\ncreate table successfully !!\n\n")

        elif name.lower() == "teachers":
            create_teacher_table(name)
            print("\ncreate table successfully !!\n\n")

        elif name.lower() == "courses":
            create_course_table(name)
            print("\ncreate table successfully !!\n\n")

        elif name.lower() == "attendances":
            create_attendance_table(name)
            print("\ncreate table successfully !!\n\n")

        else:
            print("Invalid table name.")
    elif op == 2:

        print("--1. STUDENTS")
        print("--2. TEACHERS")
        print("--3. COURSES")
        print("--4. ATTENDANCES")
        print("insert a value and above information ")
        print("-----------------------------------------------------------------------\n")


        ch = int(input("choice your option : "))
        if ch == 1:
            t_name = input("insert data table name : ")


            first_name = input("Student first name : ")

            last_name = input("Student last name :  ")

            date_of_birth = input("Studnet date of birth : ")

            if t_name.lower() == "students":
                insert_a_studnet(t_name,first_name,last_name,date_of_birth)
                print("\nInformation add successfully !!\n\n")

        elif ch == 2:
            t_name = input("insert data table name : ")

            first_name = input("Teacher first name : ")

            last_name = input("Teacher last name : ")

            subject = input("Subject name : ")

            if t_name.lower() == "teachers":
                insert_a_teacher(t_name,first_name,last_name,subject)
                print("Information add successfully !!!\n\n")
        elif ch == 3:
            t_name = input("insert data table name : ")

            course_id = int(input("Course id : "))

            course_nmae =input("Course name : ")

            teacher_id = int(input("Teacher id : "))

            schedule = input("Class schedule : ")

            insert_a_course(t_name,course_id,course_nmae,teacher_id,schedule)
            print("\nInformation add successfully !!!!\n\n")
        elif ch == 4:
            
            

            t_name = input("insert data table name : ")

            course_id = int(input("Course id : "))

            student_id = int(input("Student id : "))

            print("\n\n\tcurrent date or null")
            current_date = input("Current date : ")
            fine = int(input("Student fine : "))
          
            if current_date == 'null':
                fine+=0
            print("\n\nfine add successfully")




            if t_name.lower() == "attendances":
                insert_a_attendance(t_name, course_id, student_id, None, fine)
                print("\nInformation add successfully !!!!\n\n")
        
    elif op == 3:
        print("------- Update attendance date------------")
        t_name = input("Update table name : ")
        stu_id = int(input("Student id : "))
        f = int(input("Fine : "))
        if t_name.lower() == "attendances":
            update_date_att(t_name,f,stu_id)
    elif op == 4:
        break
    
