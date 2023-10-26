class Student:
    def __init__(self,Roll_No,Name,Marks):
        self.Roll_No=Roll_No
        self.Name=Name
        self.Marks=Marks
    def __str__(self):
        return f"Roll.No={self.Roll_No},Name={self.Name},Marks={self.Marks}"
Student_list=[]
while 1:
    ch=int(input("\n1)Add student.\t2)Show student.\n3)Update Student.\t4)Delete Student.\nExit\nEnter The Choice="))
    match ch:
        case 1:
            print("Add Student.......")
            Add_Student=int(input("Enter The Number of Student To Add in List="))
            for i in range(0,Add_Student):
                Roll_No=int(input("Enter The Roll No="))
                Name=input("Enter The Name=")
                Marks=float(input("Enter The Obtained Marks="))
                S1=Student(Roll_No,Name,Marks)
                Student_list.append(S1)
            print("Students Added.....")
        case 2:
            ch = int(input('select number\n'\
                           '1.Show student info by Roll Number'
                           '\n2.Show student info by Name'
                           '\n3.Enter The Choice='
                           ))
            match ch:
                case 1:
                    roll = int(input('Enter roll number Here='))
                    for student in Student_list:
                        if student.Roll_No == roll:
                            print(student)
                            break
                    else:
                        print(f'No student having Roll Number={roll}')
                case 2:
                    name = input('Enter name Here=')
                    
                    for student in Student_list:
                        if student.Name == name:
                            print(student)
                            break
                    else:
                        print(f'No student having Roll Number={name}')
                case _:
                    print('Incorrect Input')
            
        case 3:
             print("UPDATE STUDENTS....")
             Update_Student=int(input("Enter The Roll No To Update="))
             for i in Student_list:
                 if Update_Student==i.Roll_No:
                     while 1:
                         ch=int(input("1)Update Marks.\n2)Update Name.3)Exit\nEnter The Choice="))
                         if ch==1:
                            i.Marks=float(input("enter update marks:"))
                         elif ch==2:
                             i.Name=input("Enter Update Name=")
                         elif ch==3:
                            break
        case 4:
            print("Delete STUDENTS....")
            RN=int(input("Enter The Roll No to Delete="))
            Found=False
            Remove = False
            for student in Student_list:
                if i.Roll_No==RN:
                    Found=True
                    Remove=student
                if Remove:
                    Student_list.remove(Remove)
                    print(Remove)
                    break
        case 5:
            print("Student List Sort....")
            index=0
            for student in Student_list:
                index+=1
                Student_list.sort()
                print(Student_list)
        case 6:
           print("Exiting.....")
           break
        case _:
           print("Invalid Case...")








                    
            
                        
                
                
            
                  
                
                 
                 




        
