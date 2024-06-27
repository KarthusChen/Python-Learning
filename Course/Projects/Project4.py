class Employee:
    def __init__(self,name="",hours_worked=0,hourly_rate=0) -> None:
        self._name=name
        self._hours_worked=hours_worked
        self._hourly_rate=hourly_rate

    def setname(self,name):
        self._name=name

    def getname(self):
        return self._name
    
    def setHoursWorked(self,hours_worked):
        if hours_worked>0:
            self._hours_worked=hours_worked
        else:
            print("The Number You Entered Must be Greater Than 0")

    def getHoursWorked(self):
        return self._hours_worked
    
    def setHourlyRate(self,hourly_rate):
        if hourly_rate>0:
            self._hourly_rate=hourly_rate
        else:
            print("The Number You Entered Must be Greater Than 0")

    def getHourlyRate(self):
        return self._hourly_rate
    
    def get_input(self):
        self.setname(input("Enter a name:"))
        self.setHoursWorked(float(input("Enter hous worked:")))
        self.setHourlyRate(float(input("Enter houly rate:")))
    
    def calc_pay(self):
        OVERTIME_THRESHOLD = 40
        OVERTIME_MULTIPLIER = 1.5
        if self._hours_worked > OVERTIME_THRESHOLD:
            regular_hours = OVERTIME_THRESHOLD
            overtime_hours = self._hours_worked - OVERTIME_THRESHOLD
            return (regular_hours * self._hourly_rate) + (overtime_hours * self._hourly_rate * OVERTIME_MULTIPLIER)
        else:
            return self._hours_worked * self._hourly_rate
        
if __name__ == "__main__":

    employees = []

    print("*********************************************************************")
    print("                 Employee Data Entry Application                     ")
    print("*********************************************************************")

    while(1):
        print("1: Enter an employee")
        print("2: Print employee list")
        print("q: Quit the application")
        option = input(">>> ")

        if option == "1":
            employee = Employee()
            employee.get_input()
            employees.append(employee)
        elif option == "2":
            for idx, employee in enumerate(employees, start=1):
                print(f"Name:                     {employee.getname()}")
                print(f"Hours Worked:             {employee.getHoursWorked():.2f}")
                print(f"Hourly Rate:              ${employee.getHourlyRate():.2f}\n")
        elif option.lower() == "q":
            break
        else:
            print("Invalid option. Please enter again.")

    if employees:
        total_pay = sum(employee.calc_pay() for employee in employees)
        average_pay = total_pay / len(employees)
        print(f"The total amount to be paid is ${total_pay:.2f}.")
        print(f"The average employee is paid ${average_pay:.2f}.")
    else:
        print("No employees were entered.")

