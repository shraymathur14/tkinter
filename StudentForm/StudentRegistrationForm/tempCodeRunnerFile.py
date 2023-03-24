sql = "INSERT INTO STUDENTS(RegNo, Date, Name, DOB, Gender, Religion, Class, Skills) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    my_cur.execute(sql)
    my_