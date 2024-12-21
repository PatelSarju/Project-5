class A:
    id_set = set({})
    
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None
        self.role = None
        self.salary = None
        self.company = None

class B(A):
    def set_data(self):
        print("\nEnter employee data:")
        self.id = int(input("Enter the id:"))
        is_on = True
        while is_on: 
            if self.id in A.id_set:
                print("\nThis emp id already allocated to an employee!")
                print("\nPlease enter your employee id!")
                self.id = int(input("Enter the id:"))
            else:
                A.id_set.add(self.id)
                self.name = input("Enter the name:")
                self.age = input("Enter the age:")
                self.role = input("Enter the role:")
                self.salary = input("Enter the salary:")
                self.company = input("Enter the company:")
                self.emp_dictionary = {'ID': self.id, 'Name': self.name, 'Age': self.age, 'Role': self.role, 'Salary': self.salary, 'Company': self.company}
                is_on = False
    
    def get_role(self):
        print()
        for j, i in self.emp_dictionary.items():
            if j == 'ID' or j == 'Role':
                print(f"{j}:{i} ", end=" ")
        
class C(B):
    def get_all_data(self):
        print()
        for j, i in self.emp_dictionary.items():
            print(f"{j}:{i} ", end=" ")
        
    def get_salary(self):
        print()
        for j, i in self.emp_dictionary.items():
            if j == 'ID' or j == 'Salary':
                print(f"{j}:{i} ", end=" ")
        
    def get_age(self):
        print()
        for j, i in self.emp_dictionary.items():
            if j == 'ID' or j == 'Age':
                print(f"{j}:{i} ", end=" ")
    
    def print_all_data(self, data):
        # Print header
        headers = ["ID", "Name", "Age", "Role", "Salary", "Company"]
        print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Role':<15}{'Salary':<15}{'Company':<20}")
        print("-" * 80)  # Underline header

        # Print each employee's data
        for emp in data:
            print(f"{int(emp['ID']):<10}{emp['Name']:<20}{int(emp['Age']):<10}{emp['Role']:<15}{emp['Salary']:<15}{emp['Company']:<20}")

Employees = []    
e = C()
Employees_Data = []

while True:
    print("\n\nPress 1 for adding an employee data")
    print("Press 2 for getting employee data")
    print("Press 3 for update the single employee data")
    print("Press 4 for update the similar all employee data")
    print("Press 5 for delete specific employee data")
    print("Press 6 for delete similar all employee data")
    print("Press 7 for compare the salaries of two employee")
    print("Press 0 for exit")
    
    choice = int(input("\nEnter your choice:"))
    
    if choice == 1:
        emp = C()
        emp.set_data()
        Employees.append(emp)
        print("\nNew Employee Data Added Successfully!")
        Employees_Data.append(emp.emp_dictionary)
        
    elif choice == 2:
        print("\n\nPress 1 for see all employee data")
        print("Press 2 for see specific employee data")
        
        option = int(input("\nEnter your option:"))
        if option == 1:
            print("\n\nYou want to see all data of all employee then enter 'All'")
            print("You want to see specific data of all employee then enter 'Specific Data'")
            data_type = input("\nEnter your choice:").title()
            if data_type == 'All':
                if Employees_Data != []:
                    e.print_all_data(Employees_Data)
                else:
                    print("\nThere is no such employee data found!")
            elif data_type == 'Specific Data':
                while True:
                    print("\n\nWhich data you want to see")
                    print("If you want to see only job role data then enter the 'role'")
                    print("You want to see only salary data then enter the 'salary'")
                    print("You want to see only age data then enter the 'age'")
                    print("Enter the 'exit' for exit")
                    data = input("\nEnter your choice:").lower()
                    if Employees_Data!=[]:
                        if data=='role':
                            for i in Employees:
                                i.get_role()
                            
                        elif data=='salary':
                            for i in Employees:
                                i.get_salary()
                                
                        elif data=='age':
                            for i in Employees:
                                i.get_age()
                                
                        elif data=='exit':
                            break
                        else:
                            print("\nPlease enter the valid data type!")
                    elif data=='exit':
                        break
                    else:
                        print('\nThere is no such employee data found!')
                        
        elif option == 2:
            while True:
                print("\n\nWhich type of data you have")
                print("If you have 'name' then enter the 'Name'")
                print("If you have 'id' then enter the 'Id'")
                print("If you have 'role' then enter the 'Role'")
                print("If you have 'age' then enter the 'Age'")
                print("If you have 'salary' amount then enter the 'Salary'")
                print("If you have 'company' then enter the 'Company'")
                print("If you want to exit from this section then enter the 'Exit'")
                data = input("\nEnter the type of data:").title()
                if data == 'Name':
                    name = input("\nEnter the employee name:")
                    target_data = []
                    for i in Employees_Data:
                        if name == i['Name']:
                            target_data.append(i)
                    print()
                    if target_data != []:
                        for i in target_data:
                            for j, k in i.items():
                                print(j, ":", k)
                            print()
                    else: 
                        print("\nYour entered Name is not found in the system!")
                
                elif data == 'Id':
                    Id = input("\nEnter the employee ID:")
                    target_data = None
                    for i in Employees_Data:
                        if Id == i['ID']:
                            target_data = i
                    print()
                    if target_data != None:
                        for j, k in target_data.items():
                            print(j, ":", k)
                    else:
                        print("\nYour entered ID is not found in the system!")
                
                elif data == 'Role':
                    Role = input("\nEnter the employee Role:")
                    target_data = []
                    for i in Employees_Data:
                        if Role == i['Role']:
                            target_data.append(i)
                    print()
                    if target_data != []:
                        for i in target_data:
                            for j, k in i.items():
                                print(j, ":", k)
                            print()
                    else:
                        print("\nYour entered Job Role is not found in the system!")
                
                elif data == 'Age':
                    Age = input("\nEnter the employee Age:")
                    target_data = []
                    for i in Employees_Data:
                        if Age == i['Age']:
                            target_data.append(i)
                    print()
                    if target_data != []:
                        for i in target_data:
                            for j, k in i.items():
                                print(j, ":", k)
                            print()
                    else:
                        print("\nYour entered age's employee is not found in the system!")
                
                elif data == 'Salary':
                    Salary = int(input("\nEnter the employee Salary:"))
                    print("\nDo you want to greater than specified salary then enter the 'Greater'")
                    print("Do you want to less than specified salary then enter the 'Less'")
                    print("Do you want to equal to specified salary then enter the 'Equal'")
                    order = input("\nEnter your order choice:").title()
                    if order == 'Greater':
                        target_data = []
                        for i in Employees_Data:
                            if Salary < i['Salary']:
                                target_data.append(i)
                        print()
                        if target_data != []:
                            for i in target_data:
                                for j, k in i.items():
                                    print(j, ":", k)
                                print()
                        else:
                            print("\nAny employee doesn't have greater than your entered salary in the system!")
                    
                    elif order == 'Less':
                        target_data = []
                        for i in Employees_Data:
                            if Salary > i['Salary']:
                                target_data.append(i)
                        print()
                        if target_data != []:
                            for i in target_data:
                                for j, k in i.items():
                                    print(j, ":", k)
                                print()
                        else:
                            print("\nAny employee doesn't have less than your entered salary in the system!")
                    
                    elif order == 'Equal':
                        target_data = []
                        for i in Employees_Data:
                            if Salary == i['Salary']:
                                target_data.append(i)
                        print()
                        if target_data != []:
                            for i in target_data:
                                for j, k in i.items():
                                    print(j, ":", k)
                                print()
                        else:
                            print("\nAny employee doesn't have equal salary with your entered salary in the system!")
                
                elif data == 'Company':
                    Company = input("\nEnter the company name:")
                    target_data = []
                    for i in Employees_Data:
                        if Company == i['Company']:
                            target_data.append(i)
                    print()
                    if target_data != []:
                        for i in target_data:
                            for j, k in i.items():
                                print(j, ":", k)
                            print()
                    else:
                        print("\nYour entered company is not found in the system!")
                
                elif data == 'Exit':
                    break
                else:
                    print("\nPlease enter valid input!")
    
    elif choice==3:
        is_found=False
        data=int(input("\nEnter the your targeted employee ID:"))
        for i in Employees_Data:
            if data==i['ID']:
                is_found=True
                employee=i
                print(employee)
                data1=input("\nWhich data you want to update of this employee:").title()
                if data1=='Id':
                    new=int(input("\nEnter the employee's new Id:"))
                    employee['ID']=new
                    print("\nEmployee ID updated succussfully!")
                elif data1=='Name':
                    new=input("\nEnter the employee's updated Name:")
                    employee['Name']=new
                    print("\nEmployee Name updated succussfully!")
                elif data1=='Age':
                    new=input("\nEnter the employee's new Age:")
                    employee['Age']=new
                    print("\nEmployee Age updated succussfully!")
                elif data1=='Role':
                    new=input("\nEnter the employee's new Role:")
                    employee['Role']=new
                    print("\nEmployee Role updated succussfully!")
                elif data1=='Salary':
                    new=input("\nEnter the employee's new Salary:")
                    employee['Salary']=new
                    print("\nEmployee Salary updated succussfully!")
                elif data1=='Company':
                    new=input("\nEnter the employee's new Company:")
                    employee['Company']=new
                    print("\nEmployee Company updated succussfully!")
                elif data1=='None':
                    print("\nYou don't update any value in this time!")
                    break
                else:
                    print("\nYou entered the wrong column name!")
            if is_found==False:
                print("\nYour entered employee ID is not found in the system!")            
    
    elif choice==4:
        is_found1=False
        data=input("\nEnter the value of data which you want to update:")
        target=None
        for i in Employees_Data:
            for j,k in i.items():
                if data==k:
                    if i[j]==data:
                        is_found1=True
                        target=j
                        new_value=input(f"\nEnter the new value of {target} column of {i['Name']} employee:")
                        i[j]=new_value
                        print('\nValue updated successfully!')
                
        if is_found1==False:
            print('\nYour entered target value is not found in the system!')

    elif choice == 5:
        id = int(input("\n\nEnter the employee ID which you want to delete from the system:"))
        is_found = False
        for i in Employees_Data:
            if id == i['ID']:
                is_found = True
                # Remove employee from the list
                Employees_Data.remove(i)
                # Remove ID from the id_set
                A.id_set.remove(id)
                print("\nEmployee data removed successfully from the system!")
                break
        if not is_found:
            print("\nEmployee ID not found in the system!")
    
    elif choice == 6:
        data = input("\n\nEnter the employee data value to delete from the system:")
        is_found = False
        for i in Employees_Data[:]:
            if data in i.values():
                is_found = True
                # Remove employee from the list
                Employees_Data.remove(i)
                # Remove the ID from the id_set
                A.id_set.remove(i['ID'])
                print(f"Employee with ID {i['ID']} removed successfully from the system.")
        
        if not is_found:
            print("\nNo employee data found with the entered value.")
    
    elif choice==7:
        id1=int(input('\nEnter the ID of First Employee:'))
        id2=int(input('Enter the ID of Second Employee:'))
        emp1=None
        emp2=None
        for employee in Employees_Data:
            for i in employee:
                if employee[i]==id1:
                    emp1=employee
                if employee[i]==id2:
                    emp2=employee
        print("\nComparing Salaries:")
        if emp1['Salary']>emp2['Salary']:
            print(f"\n{emp1['Name']}'s salary is more than {emp2['Name']}'s salary by {int(emp1['Salary'])-int(emp2['Salary'])}!")
        elif emp1['Salary']<emp2['Salary']:
            print(f"\n{emp1['Name']}'s salary is less than {emp2['Name']}'s salary by {int(emp2['Salary'])-int(emp1['Salary'])}!")
        else:
            print(f"\n{emp1['Name']} and {emp2['Name']}'s salary is equal, both salaries is {emp1['Salary']}!")
                
    elif choice == 0:
        break
    
    else:
        print("\nInvalid choice! Please try again.")    