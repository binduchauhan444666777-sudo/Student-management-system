class Studentinfo:
   def __init__(self,name,department,rollno,year):
      self.name = name
      self.department = department
      self.rollno = rollno
      self.year = year

student = Studentinfo(["Kajal", "Preeti", "Bindu","Aastha", "Paakhi", "Vishakha"],["Engineering", "Pharmacy", "Commerce", "Physics", "Medicine", "Mathematics"],[6,7,9,8,10,11],[1,2,3,4,1,3])

while True:
   print("\n 1. SEARCH A STUDENT ")
   print("2. ADD A STUDENT INFO ")
   print("3. SORT ROLLNO")
   print("4. DELETE STUDENT INFO")
   print("5. EXIT")

   choice = int(input("--- Enter choice : ---"))

   if (choice == 1) :
      name = input("Enter a name to search :")
      if name in student.name :
       print("FOUND")

   elif(choice == 2):
     choice2 = input("ENTER 'a' to add new name , 'b' to add new rollno, 'c' to add new department, 'd' to add new year")
     if (choice2 == 'a'):
      new_name = input("Enter a name to add :")
      student.name.append(new_name)

     elif(choice2 == 'b'):
       student.rollno.append(int(input("Enter rollno to add")))
       print("***New rollno has been added successfully***")

     elif(choice2 == 'c'):
       new_department = input("Enter new department you wish to add :")
       student.department.append(new_department)

     else:
       student.year.append(int(input("Enter a new year to add :")))
       print("***New year has been added successfully***")

   elif(choice == 3):
     student.rollno.sort()
     print("Sorted rollno are " ,student.rollno)
   
   elif(choice == 4):
     delete_name = ("Enter  a name you wish to delete :")
     if delete_name in student.name:
      student.name.remove(delete_name)
     
   elif(choice == 5):
     break




