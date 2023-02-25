# This program allows the user to work out their monthly take home pay using their gross income/salary

import re


def show_menu():
    print('''Hi there, thanks for using our simple UK wage calculator, press:
    1. Workout Monthly Wage
    2. Quit
    ''')
    instruct = input('').strip().lower()
    possible_answers = ['1', '2']
    # validate user input
    while instruct not in possible_answers:
        print('You must enter a 1 or a 2, one of the choices...')
        instruct = input('').strip().lower()
    if instruct == '1':
        tax_code = get_tax_code()
        tax_free_amount = extract_tax_free_from_tax_code(tax_code)
        print(tax_free_amount)
    if instruct == '2':
        exit()


def get_tax_code():
    """
    Asks the user to input a tax code. Then uses a regular expression to validates 
    that four numbers and a letter has been entered. Then returns the entered tax code if latter is valid
    """
    entered_tax_code = input('Please enter your UK tax code, your UK tax code is four digits followed by a '
                             'letter').strip().lower()
    patten = re.compile('\d{4}[a-z]{1}')
    is_tax_code = patten.match(entered_tax_code)
    while is_tax_code is None:
        print('No, that is not a correctly formatted UK tax code!')
        entered_tax_code = input('Please enter your tax code, your tax code is four digits followed by a letter')
        is_tax_code = patten.match(entered_tax_code)
    return entered_tax_code


def extract_tax_free_from_tax_code(tax_code):
    """ 
    Returns the tax free amount by multiplying by the numbers in tax code by 10 
    """
    cleaned_tax_code = tax_code[:4]
    tax_free_amount = int(cleaned_tax_code) * 10
    return tax_free_amount


def get_annual_salary():
    """ 
    Gets user's annual salary before tax and national insurance are deducted
    """
    annual_salary = input("Enter your annual salary here: \n")
    print(f"Your annual salary is: {annual_salary}")
    
    return  annual_salary


def workout_tax_breakdown(tax_free_amount, annual_salary):
    """
    Worksout tax breakdown using the tax code, the derived tax free amount and the annual salary entered.
    """

    tax_breakdown = []

    amt_to_rate = int(annual_salary) - int(tax_free_amount)

    for amt_to_rate in range(12571, 150000):
        if (amt_to_rate > 12571 and amt_to_rate < 50270):
            tax_rate = amt_to_rate * 0.2

        elif amt_to_rate in range(50271, 150000):
            tax_rate = amt_to_rate * 0.4

        else:
            tax_rate = amt_to_rate * 0.45

    print(f"Tax deducted is: {tax_breakdown}")

    return tax_breakdown


def workout_national_insurance(tax_free_amount, annual_salary):
    """
    Woks out the national insurance amount to be deducted/paid 
    """
    return


def workout_take_home(annual_salary, tax, national_insurance):
    return


def give_results(tax_code, annual_salary, tax, national_insurance, take_home):
    return


def main():
    """
    Runs all program functions
    """

    show_menu()
    #get_tax_code()
    annual_salary = get_annual_salary()
    #get_annual_salary()
    tax_code = get_tax_code()
    tax_free_amount = extract_tax_free_from_tax_code(tax_code)
    workout_tax_breakdown(tax_free_amount, annual_salary)


main()