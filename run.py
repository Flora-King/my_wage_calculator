"""
This program allows the user to work out their monthly take home pay
using their gross earnings
"""
import re


def show_menu():
    """
    Asks user to choose whether to continue using the calculator or quit
    """
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
        gross_earnings = get_gross_earnings()
        tax_free_amt = extract_tax_free_from_tax_code(tax_code, gross_earnings)
        income_tax = income_tax_breakdown(tax_free_amt, gross_earnings)
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


def extract_tax_free_from_tax_code(tax_code, gross_earnings):
    """
    Returns the tax free amount by multiplying by the numbers in tax code by 10
    """
    cleaned_tax_code = tax_code[:4]
    tax_free_amt = int(cleaned_tax_code) * 10
    return tax_free_amt


def get_gross_earnings():
    """
    Gets user's total earnings before tax and national insurance are deducted
    """
    gross_earnings = input("Enter your gross earnings here: \n")
    return int(gross_earnings)


def income_tax_breakdown(tax_free_amt, gross_earnings):
    """
    Works out taxable income by subtracting annual salary and tax free amount.
    Then works out the basic tax rate, high tax rate, and Higher tax rate.
    Finally returns total tax deducted which is the sum of all the tax rates.
    """
    taxable_income = gross_earnings - tax_free_amt
    basic_rate = 50270
    high_rate = 150000
    basic_rate_amount = 0
    high_rate_amount = 0
    higher_rate_amount = 0
    income_tax = 0

    if gross_earnings <= 50000:
        basic_rate_amount = (gross_earnings - tax_free_amt) * 0.2
    else:
        basic_rate_amount = (50270 - tax_free_amt) * 0.2
    if gross_earnings > 50000:
        high_rate_amount = (gross_earnings - 50270) * 0.4
        # elif gross_earnings > 150000:
    else:
        higher_rate_amount = (gross_earnings - 150000) * 0.45

    print(f"Taxable income is: {taxable_income:.2f}")
    print(f"Basic rate tax deducted is: {basic_rate_amount:.2f}")
    print(f"High rate tax deducted is: {high_rate_amount:.2f}")
    print(f"Higher rate tax deducted is: {higher_rate_amount:.2f}")
    # print(f"Total income tax deducted is: {income_tax:.2f}")
    return income_tax


def workout_take_home(gross_earnings, income_tax, national_insurance):
    """
    Returns take home amount using the annual salary figure, tax deducted and
    national insurance deducteds
    """
    income_tax = int()
    take_home = int(gross_earnings) - (int((national_insurance) + int(income_tax)))
    print(f"monthly take home is: {float(take_home)}")
    return take_home / 12


def give_results(gross_earnings, income_tax, national_insurance, take_home):
    """
    Presents the take home amount alongside gross earnings, income tax and
    nataional insurance deductions in a table
    """
    return



def main():
    """
    Runs all program functions
    """
    show_menu()
main()
