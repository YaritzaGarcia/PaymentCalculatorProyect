def is_file(filename):
    try:
        fh=open(filename,'r')
        fh.close()
        return True
    except FileNotFoundError:
        return False

def print_program_menu():

    print("Welcome to payment calculator. Please, choose an option:\n")
    print("1. Employees payment (will create a employees_payment.txt file)\n")
    print("2. Employee name with maximum number of work hours\n")
    print("3. Employee name with minimum number of work hours\n")
    print("4. Employee name with maximum rate\n")
    print("5. Employee name with minimum rate\n")
    print("6. Exit")


#This function allows to verify the entered option
def identify_option(option):
    if option.isdigit():
        numeric_option = int(option)
        if numeric_option >= 1 and numeric_option <= 6:
            return numeric_option
        else:
            return -1
    else:
        return -1

def calculate_payment(hours,rate):
    pay = hours * rate
    if hours > 40:
        xtrapay = (hours * rate) + (rate * 1.5) + rate
        print (xtrapay)

    if rate > 50:
        print(pay)

def process_request(option):
    filename = input("Enter the name of the file to be processed: ")
    if is_file(filename):
        fhandle = open(filename,'r')
    else:
        print("Illegal file name. Input file was not found")
    if option == 1:
        option_1(filename)
    if option == 2:
        option_2(filename)
    if option == 3:
        option_3(filename)
    if option == 4:
        option_4(filename)
    if option == 5:
        option_5(filename)
    if option == 6:
        option_6()

#1. Employees payment (will create a employees_payment.txt file)
def option_1(file_name):
    file = open(file_name, 'r')
    f = open("employees_payment.txt", "w")
    employee_payment = 0
    employee_name = ""
    employee_hours = 0
    employee_rate = 0
    for line in file:
        if line[0:4] != "time":
            employee_name = line[0:line.find(',')]
            employee_hours = int(line[line.find(','):line.rfind(',')].strip(","))
            employee_rate = int(line[line.rfind(','):].strip(","))
            if employee_hours <= 40 or employee_rate > 50:
                employee_payment = employee_hours * employee_rate
            else:
                employee_payment = (40 * employee_rate) + ((employee_hours-40) * (1.5*employee_rate))
            f.write(str(employee_name) + "   $" + str(int(employee_payment)) +"\n")


    print("A file employees_payment.txt containing the payment information has been created. \n")


#2. Employee name with maximum number of work hours
def option_2(file_name):
        counter = 0
        employee_name = ""
        employee_hours = 0
        file = open(file_name, 'r')
        for line in file:
            if line[0:4] != "time":
                name = line[0:line.find(',')]
                hours = line[line.find(','):line.rfind(',')].strip(",")
                if counter == 0:
                    employee_hours = hours
                    employee_name = name
                    counter = 1
                else:
                    if hours > employee_hours:
                        employee_name = name
                        employee_hours = hours
                    elif hours == employee_hours:
                        employee_name = employee_name + "and" + name
                        employee_hours = hours

        print("The employee with the maximum number of work hours is: " + employee_name + "\n")


#3. Employee name with minimum number of work hours
def option_3(file_name):
    counter = 0
    employee_name = ""
    employee_hours = 0
    file = open(file_name, 'r')
    for line in file:
        if line[0:4] != "time":
            name = line[0:line.find(',')]
            hours = line[line.find(','):line.rfind(',')].strip(",")
            if counter == 0:
                employee_hours = hours
                employee_name = name
                counter = 1
            else:
                if hours < employee_hours:
                    employee_name = name
                    employee_hours = hours
                elif hours == employee_hours:
                    employee_name = employee_name + "and" + name
                    employee_hours = hours

    print("The employee with the minimum number of work hours is: " + employee_name + "\n")


#4. Employee name with maximum rate
def option_4(file_name):
    counter = 0
    employee_name = ""
    employee_rate = 0
    file = open(file_name, 'r')
    for line in file:
        if line[0:4] != "time":
            name = line[0:line.find(',')]
            rate = line[line.rfind(','):].strip(",")
            if counter == 0:
                employee_rate = rate
                employee_name = name
                counter = 1
            else:
                if rate > employee_rate:
                    employee_name = name
                    employee_rate = rate
                elif rate == employee_rate:
                    employee_name = employee_name + "and" + name
                    employee_rate = rate

    print("The employee with the maximum rate is: " + employee_name + "\n")


#5. Employee name with minimum rate
def option_5(file_name):
    counter = 0
    employee_name = ""
    employee_rate = 0
    file = open(file_name, 'r')
    for line in file:
        if line[0:4] != "time":
            name = line[0:line.find(',')]
            rate = line[line.rfind(','):].strip(",")
            if counter == 0:
                employee_rate = rate
                employee_name = name
                counter = 1
            else:
                if rate < employee_rate:
                    employee_name = name
                    employee_rate = rate
                elif rate == employee_rate:
                    employee_name = employee_name + "and" + name
                    employee_rate = rate

    print("The employee with the minimum rate is: " + employee_name + "\n")


#6. Exit
def option_6():
    print ("Thanks for using the payment calculator program")


################################################################

def main():
    done = False
    while not done:
        print_program_menu()
        user_option = input("Enter option: ")
        option_info = identify_option(user_option)
        if option_info != -1:
            if option_info == 6:
                done = True
                print( "Thanks for using the payment calculation program")
            else:
                process_request(option_info)
        else:
            print("Invalid Option\n")

if __name__ == "__main__":
    main()
