#Functions with Outputs
# def my_myfunction()

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"First name is: {formated_f_name}, last name is: {formated_l_name}"
formated_string = format_name("Ozodbek", "Devana")
print(format_name(input("What is you first name? "), input("What is your last name? ")))

print("-------------------------------------------------")

def is_leap(year):
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    #if month > 12 or month < 1:
        #return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    print(month_days[month - 1])


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
month = days_in_month(year, month)
print(year)

print("-------------------------------------------------")

print(format_name(input("What is your name? "), input("What is your last name? ")))


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name}, {formated_l_name}"






























