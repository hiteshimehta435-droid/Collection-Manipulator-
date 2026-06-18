

students_records = []
while True:
  print("\n----- STUDENT DATA -----")
  print("1. Add student")
  print("2. All students records")
  print("3. Update student Information")
  print("4. show student data")
  print("5. Delete student data")
  print("6. Exit")
  option = int(input("Enter your option: "))
  
  match option:
    case 1:
      print("Enter student data: ")
      id = input("student id: ")
      name = input("student name: ")
      age = input("student age: ")
      grade = input("student grade: ")
      birthdate = input("student birthdate: ")
      subjects = input("student subjects: ")
      
      student = {"id": id,
                 "name": name,
                 "age": age,
                 "grade": grade,
                 "birthdate": birthdate,
                 "subjects": subjects}
      
      students_records.append(student)
      print("student add successfully!")
        
    case 2:
      print("\n-- STUDENT RECORDS --")
      for student in students_records:
        print("id:", student["id"])
        print("name:", student["name"])
        print("age:", student["age"])
        print("grade:", student["grade"])
        print("birthdate:", student["birthdate"])
        print("subjects:", student["subjects"])
        
    case 3:
       print("\n-UPDATE STUDENT DATA-")
       
       id = int(input("Enter id: "))
       
       id = input("new id: ") 
       grade = input("new grade: ")
       subjects = input("new subject: ")
       print("Update successfully!")
            
    case 4:
        print("\n-- DISPLAY STUDENT DATA--")
        id = int(input("Enter id: "))
        print(f"name: {student['name']} | age: {student['age']} | grade: {student['grade']}")
        
    case 5:
      print("\n-- STUDENT DATA DELETE--")
      for student in students_records:
        if student["id"] == "students_records":
            student_records.remove(student)
            break
            
    case 6:
      print("\n   EXIT   ")
      break
