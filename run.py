"""
This program allows the user to work out their monthly take home pay
using their gross income/salary
"""

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
    Asks the user to input a tax code. Then validates that four numbers and
    a letter has been entered using regular expression.
    Then returns the entered tax code if latter is valid
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

    return annual_salary


def workout_income_tax_breakdown(tax_free_amount, annual_salary):
    """
    Works out taxable income by subtracting annual salary and tax free amount.
    Then works out the basic tax rate, high tax rate and Higher tax rate.
    Finally returns total tax deducted which is the sum of all the tax rates.
    """
    income_tax_deducted = int()
    zero_rate = int()
    basic_rate = int()
    high_rate = int()
    higher_rate = int()
    remaining_taxable_income_h = int()
    taxable_income = int(annual_salary) - int(tax_free_amount)

    if int(annual_salary) <= tax_free_amount:
        zero_rate = int(tax_free_amount) * 0

    elif int(annual_salary) <= 50270:
        basic_rate = (int(annual_salary) - 12570) * 0.2
            
    elif int(annual_salary) <= 150000:
        high_rate = basic_rate + (int(annual_salary) - 50270) * 0.4

    else:
        remaining_taxable_income_h = taxable_income - basic_rate
        higher_rate = remaining_taxable_income_h - 150000 * 0.45

    income_tax_deducted = basic_rate + high_rate + higher_rate

    print(f"Taxable income is: {round(taxable_income)}")
    print(f"Basic rate tax deducted is: {round(basic_rate)}")
    print(f"High rate tax deducted is: {round(high_rate)}")
    print(f"Higher rax tax deducted is: {round(higher_rate)}")
    print(f"Total income tax deducted is: {round(income_tax_deducted)}")

    return income_tax_deducted


def workout_basic_tax_rate(tax_free_amount, annual_salary):

    # zero_rate = int()
    taxable_income_b = int()

    # taxable_income_b = int(annual_salary) - int(tax_free_amount)

    if taxable_income_b > tax_free_amount and int(taxable_income_b) <= 50270:
        taxable_income_b -= tax_free_amount
        return taxable_income_b * 0.2

    # print(f"Taxable income is: {round(taxable_income)}")
    print(f"Basic rate tax deducted is: {round(taxable_income_b)}")


def workout_national_insurance(tax_free_amount, annual_salary):
    """
    Works out the national insurance amount to be deducted/paid
    """
    return


def workout_take_home(annual_salary, tax, national_insurance):
    """
    Returns take home amount using the annual salary figure, tax deducted and 
    national insurance deducteds
    """
    return


def give_results(tax_code, annual_salary, tax, national_insurance, take_home):
    """
    Presents the take home amount alongside annual salary, tax and 
    nataional insurance
    """
    return


def main():
    """
    Runs all program functions
    """

    show_menu()
    # get_tax_code()
    annual_salary = get_annual_salary()
    # get_annual_salary()
    tax_code = get_tax_code()
    tax_free_amount = extract_tax_free_from_tax_code(tax_code)
    # workout_basic_tax_rate(tax_free_amount, annual_salary)
    workout_income_tax_breakdown(tax_free_amount, annual_salary)


main()
