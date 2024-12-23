class A:
    """
    Base class representing an employee with basic attributes.

    Attributes:
        id_set (set): A set to store unique employee IDs.
        id (str): The employee's ID.
        name (str): The employee's name.
        age (str): The employee's age.
        role (str): The employee's role in the company.
        salary (str): The employee's salary.
        company (str): The company the employee works for.
    """
    id_set = set({})
    
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None
        self.role = None
        self.salary = None
        self.company = None

class B(A):
    """
    Subclass representing an employee with the ability to set employee data.

    Inherits from class A.

    Methods:
        set_data: Prompts the user to input and validates employee data.
        get_role: Prints the employee's ID and role.
    """
    def set_data(self):
        """
        Prompts the user for employee details (ID, name, age, role, salary, company).
        
        If an employee ID already exists, prompts the user to enter a unique ID.
        Once data is entered, it is stored in the emp_dictionary attribute.
        """
        print("\nEnter employee data:")
        self.id = input("Enter the id:")
        is_on = True
        while is_on: 
            if self.id in A.id_set:
                print("\nThis emp id already allocated to an employee!")
                print("\nPlease enter your employee id!")
                self.id = input("Enter the id:")
            else:
                A.id_set.add(self.id)
                self.name = input("Enter the name:").title()
                self.age = input("Enter the age:")
                self.role = input("Enter the role:").title()
                self.salary = input("Enter the salary:")
                self.company = input("Enter the company:").title()
                self.emp_dictionary = {'ID': self.id, 'Name': self.name, 'Age': self.age, 'Role': self.role, 'Salary': self.salary, 'Company': self.company}
                is_on = False
    
    def get_role(self):
        """
        Prints the employee's ID and role from the emp_dictionary.
        """
        print()
        for j, i in self.emp_dictionary.items():
            if j == 'ID' or j == 'Role':
                print(f"{j}:{i} ", end=" ")
        
class C(B):
    """
    Subclass representing an employee with additional methods to view specific employee data.
    
    Inherits from class B.

    Methods:
        get_all_data: Prints all employee data from the emp_dictionary.
        get_salary: Prints the employee's ID and salary.
        get_age: Prints the employee's ID and age.
        print_all_data: Prints the data of multiple employees in a formatted table.
    """
    def get_all_data(self):
        """
        Prints all employee data from the emp_dictionary.
        """
        print()
        for j, i in self.emp_dictionary.items():
            print(f"{j}:{i} ", end=" ")
        
    def get_salary(self):
        """
        Prints the employee's ID and salary.
        """
        print()
        for j, i in self.emp_dictionary.items():
            if j == 'ID' or j == 'Salary':
                print(f"{j}:{i} ", end=" ")
        
    def get_age(self):
        """
        Prints the employee's ID and age.
        """
        print()
        for j, i in self.emp_dictionary.items():
            if j == 'ID' or j == 'Age':
                print(f"{j}:{i} ", end=" ")
    
    def print_all_data(self, data):
        """
        Prints a formatted table of data for multiple employees.

        Args:
            data (list of dict): A list of dictionaries where each dictionary contains
                                  employee information (ID, name, age, role, salary, company).
        
        Prints:
            A neatly formatted table of employee data with headers and values aligned.
        """
        # Print header
        headers = ["ID", "Name", "Age", "Role", "Salary", "Company"]
        print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Role':<15}{'Salary':<15}{'Company':<20}")
        print("-" * 80)  # Underline header

        # Print each employee's data
        for emp in data:
            print(f"{emp['ID']:<10}{emp['Name']:<20}{int(emp['Age']):<10}{emp['Role']:<15}{emp['Salary']:<15}{emp['Company']:<20}")

Employees = []    
e = C()
Employees_Data = []

while True:
    """
    Main loop for displaying the menu and processing the user's choice.

    The program continuously displays a menu of options and executes the appropriate 
    operation based on the user's selection. The available operations are:
    - Adding new employee data
    - Viewing all or specific employee data
    - Updating an individual or all employees' data
    - Deleting specific or all employees' data
    - Comparing the salaries of two employees
    - Exiting the program
    """
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
        """
        Add a new employee's data.

        This operation allows the user to input data for a new employee, including their
        ID, name, age, role, salary, and company. The system ensures that the ID is unique
        before adding the employee's data to the system.

        Returns:
            None
        """
        emp = C()
        emp.set_data()
        Employees.append(emp)
        print("\nNew Employee Data Added Successfully!")
        Employees_Data.append(emp.emp_dictionary)
        
    elif choice == 2:
        """
        View employee data.

        This operation gives the user two options:
        1. View all employee data
        2. View specific employee data based on a chosen attribute (e.g., name, ID, role).
        The user can also filter data by selecting specific attributes such as Role, Salary, or Age.

        Returns:
            None
        """
        print("\n\nPress 1 for see all employee data")
        print("Press 2 for see specific employee data")
        
        option = int(input("\nEnter your option:"))
        if option == 1:
            """
            View all employee data.

            This operation displays either all employee data or specific employee data based 
            on the user's choice. It shows data for all employees or allows filtering by 
            attributes such as role, salary, or age.

            Returns:
                None
            """
            print("\n\nYou want to see all data of all employee then enter 'All'")
            print("You want to see specific data of all employee then enter 'Specific Data'")
            data_type = input("\nEnter your choice:").title()
            if data_type == 'All':
                if Employees_Data != []:
                    e.print_all_data(Employees_Data)
                else:
                    print("\nThere is no such employee data found!")
            elif data_type == 'Specific Data':
                """
                View specific data for employees.

                This operation allows the user to filter the employee data based on specific 
                attributes like role, salary, or age. The user can select a data type, and the 
                system will show relevant details for all employees.

                Returns:
                    None
                """
                while True:
                    print("\n\nWhich data you want to see")
                    print("If you want to see only job role data then enter the 'Role'")
                    print("You want to see only salary data then enter the 'Salary'")
                    print("You want to see only age data then enter the 'Age'")
                    print("Enter the 'Exit' for exit")
                    data = input("\nEnter your choice:").title()
                    if Employees_Data!=[]:
                        if data=='Role':
                            for i in Employees:
                                i.get_role()
                            
                        elif data=='Salary':
                            for i in Employees:
                                i.get_salary()
                                
                        elif data=='Age':
                            for i in Employees:
                                i.get_age()
                                
                        elif data=='Exit':
                            break
                        else:
                            print("\nPlease enter the valid data type!")
                    elif data=='Exit':
                        break
                    else:
                        print('\nThere is no such employee data found!')
                        
        elif option == 2:
            """
            View specific employee data based on user input.

            This operation allows the user to search for employees based on specific 
            data attributes such as name, ID, role, age, salary, or company. If the 
            specified attribute matches any employee's information, the details will 
            be displayed.

            Returns:
                None
            """
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
                    """
                    Search and display employee data by name.

                    This operation searches the employee data based on the provided name 
                    and displays the matching records.

                    Returns:
                        None
                    """
                    name = input("\nEnter the employee name:").title()
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
                    """
                    Search and display employee data by ID.

                    This operation searches the employee data based on the provided ID 
                    and displays the matching record.

                    Returns:
                        None
                    """
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
                    """
                    Search and display employee data by Role.

                    This operation searches the employee data based on the provided Role 
                    and displays the matching record.

                    Returns:
                        None
                    """
                    Role = input("\nEnter the employee Role:").title()
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
                    """
                    Search and display employee data by Age.

                    This operation searches the employee data based on the provided Age 
                    and displays the matching record.

                    Returns:
                        None
                    """
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
                    """
                    Searches and displays employee data based on salary comparison.

                    This section allows the user to input a salary and choose whether they want to find employees with a salary greater than, less than, or equal to the entered salary.
                    It then searches through the employee data and displays matching results.
                    If no employees match the criteria, a message is displayed indicating no matches.

                    Parameters:
                    -----------
                    None

                    Returns:
                    --------
                    None
                    """
                    Salary = int(input("\nEnter the employee Salary:"))
                    print("\nDo you want to greater than specified salary then enter the 'Greater'")
                    print("Do you want to less than specified salary then enter the 'Less'")
                    print("Do you want to equal to specified salary then enter the 'Equal'")
                    order = input("\nEnter your order choice:").title()
                    if order == 'Greater':
                        target_data = []
                        for i in Employees_Data:
                            if Salary < int(i['Salary']):
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
                            if Salary > int(i['Salary']):
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
                            if Salary == int(i['Salary']):
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
                    """
                    Search and display employee data by Company Name.

                    This operation searches the employee data based on the provided Company Name and displays the matching record.

                    Returns:
                        None
                    """
                    Company = input("\nEnter the company name:").title()
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
        """
        Allows the user to update specific data for an employee based on their ID.

        This section prompts the user to enter an employee's ID, searches for the employee in the system,
        and provides options to update specific data fields, such as ID, name, age, role, salary, or company.
        If the employee is found, the user can choose which field to update and enter the new value.
        If no matching employee is found, an error message is displayed.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        is_found=False
        data=input("\nEnter the your targeted employee ID:")
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
                    new=input("\nEnter the employee's updated Name:").title()
                    employee['Name']=new
                    print("\nEmployee Name updated succussfully!")
                elif data1=='Age':
                    new=input("\nEnter the employee's new Age:")
                    employee['Age']=new
                    print("\nEmployee Age updated succussfully!")
                elif data1=='Role':
                    new=input("\nEnter the employee's new Role:").title()
                    employee['Role']=new
                    print("\nEmployee Role updated succussfully!")
                elif data1=='Salary':
                    new=input("\nEnter the employee's new Salary:")
                    employee['Salary']=new
                    print("\nEmployee Salary updated succussfully!")
                elif data1=='Company':
                    new=input("\nEnter the employee's new Company:").title()
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
        """
        Allows the user to update all employees' data that matches a specific value.

        This section prompts the user to enter a value that they want to update across all employee data. 
        The system searches for the value in all employee records, and if the value matches any entry, 
        the user can update it with a new value. Once the user inputs the new value, it updates the corresponding 
        field for all employees with that matching value. If no matching data is found, an error message is displayed.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
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
        """
        Deletes an employee's data from the system based on the provided employee ID.

        This section prompts the user to enter an employee ID that they wish to delete. 
        The system searches for the employee with the given ID in the employee records. 
        If the employee is found, the corresponding data is removed from the `Employees_Data` list, 
        and the employee ID is also removed from the `id_set` to ensure uniqueness of employee IDs.
        If the employee ID is not found, an error message is displayed.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        id = input("\n\nEnter the employee ID which you want to delete from the system:")
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
        """
        Deletes all employees' data from the system that contains a specified value.

        This section prompts the user to enter a data value (such as name, role, etc.) that they wish to delete. 
        The system searches for any employee records that contain the specified value. 
        If a match is found, the corresponding employee's data is removed from the `Employees_Data` list, 
        and their ID is also removed from the `id_set`. The process repeats for each matching employee.
        If no employee data matches the specified value, an error message is displayed.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
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
        """
        Compares the salaries of two employees based on their IDs.

        This section prompts the user to enter the IDs of two employees. It searches for the employees 
        corresponding to the entered IDs in the `Employees_Data` list. After finding the matching employees, 
        it compares their salaries and displays the result as follows:
        
        - If the first employee's salary is higher, the difference in salary is shown.
        - If the first employee's salary is lower, the difference in salary is shown.
        - If both employees have the same salary, a message indicating the equality is displayed.
        
        If either of the entered IDs doesn't match any employee, no comparison is made. If both IDs 
        are valid, the program shows the salary comparison with the difference (if applicable).

        Additionally, if the user chooses option 0, the program will exit the loop. If an invalid choice 
        is entered, an error message is displayed and the user is prompted to try again.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        id1=input('\nEnter the ID of First Employee:')
        id2=input('Enter the ID of Second Employee:')
        emp1=None
        emp2=None
        for employee in Employees_Data:
            for i in employee:
                if employee[i]==id1:
                    emp1=employee
                if employee[i]==id2:
                    emp2=employee
        print("\nComparing Salaries:")
        if int(emp1['Salary'])>int(emp2['Salary']):
            print(f"\n{emp1['Name']}'s salary is more than {emp2['Name']}'s salary by {int(emp1['Salary'])-int(emp2['Salary'])}!")
        elif int(emp1['Salary'])<int(emp2['Salary']):
            print(f"\n{emp1['Name']}'s salary is less than {emp2['Name']}'s salary by {int(emp2['Salary'])-int(emp1['Salary'])}!")
        else:
            print(f"\n{emp1['Name']} and {emp2['Name']}'s salary is equal, both salaries is {emp1['Salary']}!")
                
    elif choice == 0:
        """
        Exits the program.

        If the user selects option 0, the program will exit the loop, effectively terminating the 
        program. No further operations will be executed, and the program will stop.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        break
    
    else:
        """
        Handles invalid choices.

        If the user enters an invalid choice (a number outside the valid range), an error message 
        is displayed, and the user is prompted to enter a valid choice. This ensures that only valid 
        options are processed, keeping the user experience clear and error-free.

        Parameters:
        -----------
        None

        Returns:
        --------
        None
        """
        print("\nInvalid choice! Please try again.")    