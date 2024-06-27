print(__doc__)

def get_input():
    """
    The Function gets the needed information for the calculations below
    """
    name=(input("Enter the employee name:"))
    HoursWorked=float(input("Enter the hours worked:"))
    HourlyRate=float(input("Enter te Hourly Rate:"))
    return name, HoursWorked,HourlyRate

    
def calc_pay(hours,rate):
    """
    The function calculates the salary for each person
    """
    if hours > 40:
        return ((hours - 40) * (rate * 1.5)) + 40 * rate
    else:
        return hours * rate

if __name__ == "__main__":

    totalSalary=0
    NumberOfEmployees=int(input("Enter the number of Employees:")) 
    """
    Defining number of the employees and the total salary
    """

    for _ in range(NumberOfEmployees):
        """
        Loop to add everthing onto total salary
        """
        Name,HoursWorked,HourlyRate=get_input()
        payment=calc_pay(HoursWorked,HourlyRate)
        totalSalary += payment
        print("The salary for ",Name," would be $",format(payment,'.2f'),sep="")
        print("\n") 
    
    AveragePayment=totalSalary/NumberOfEmployees

    print("The total amount to be paid is $",format(totalSalary,".2f"))
    print("The average employee is paid $",format(AveragePayment,".2f"))