"""
This program allows the user to work out their monthly take home pay
using their gross earnings
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
        tax_free_amt = extract_tax_free_from_tax_code(tax_code)
        print(tax_free_amt)
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
    tax_free_amt = int(cleaned_tax_code) * 10
    return tax_free_amt


def get_gross_earnings():
    """
    Gets user's total earnings before tax and national insurance are deducted
    """
    gross_earnings = input("Enter your gross earnings here: \n")
    print(f"Your gross earnings are: {gross_earnings}")

    return gross_earnings


def workout_income_tax_breakdown(tax_free_amt, gross_earnings):
    """
    Works out taxable income by subtracting annual salary and tax free amount.
    Then works out the basic tax rate, high tax rate, and Higher tax rate.
    Finally returns total tax deducted which is the sum of all the tax rates.
    """
    income_tax = int()
    zero_rate = int()
    basic_rate = int()
    high_rate = int()
    higher_rate = int()
    # additional_tax = int()
    remaining_taxable_income_h = int()
    tax_code = get_tax_code()
    tax_free_amt = extract_tax_free_from_tax_code(tax_code)
    taxable_income = int(gross_earnings) - int(tax_free_amt)

    if int(gross_earnings) <= tax_free_amt:
        zero_rate = int(tax_free_amt) * 0
        print(zero_rate)

    elif int(gross_earnings) <= 50270:
        basic_rate = (int(gross_earnings) - 12570) * 0.2

    elif int(gross_earnings) <= 150000:
        high_rate = basic_rate + (int(gross_earnings) - 50270) * 0.4

    else:
        remaining_taxable_income_h = taxable_income - basic_rate
        higher_rate = remaining_taxable_income_h - 150000 * 0.45

    income_tax = basic_rate + high_rate + higher_rate

    print(f"Taxable income is: {round(taxable_income)}")
    print(f"Basic rate tax deducted is: {round(basic_rate)}")
    print(f"High rate tax deducted is: {round(high_rate)}")
    print(f"Higher rax tax deducted is: {round(higher_rate)}")
    print(f"Total income tax deducted is: {round(income_tax)}")

    return income_tax


def workout_national_tax_breakdown(gross_earnings):
    """
    Works out the class 1 national insurance amount deducted from all employees
    """
    # lower_earnings_limit = 6396    # per year@ 0%
    pri_thresh = 12570    # per year @ 0%
    upper_limit = 50270   # per year @ 12%
    above_upper_limit = 50271   # plus @2%
    taxable_pt_ni = int()
    taxable_uel_ni = int()
    above_uel_ni = int()

    if int(gross_earnings) <= int(pri_thresh):
        taxable_pt_ni = int(pri_thresh) * 0

    elif int(gross_earnings) <= int(upper_limit):
        taxable_uel_ni = float(int(upper_limit) - int(pri_thresh)) * 0.12

    elif int(gross_earnings) > int(above_upper_limit):
        above_uel_ni = (int(gross_earnings) - int(upper_limit)) * 0.2

    national_insurance = taxable_pt_ni + taxable_uel_ni + above_uel_ni

    print("NI breakdown is as follows: ")
    print(f"Primary threshold NI deducted is: {float(taxable_pt_ni)}")
    print(f"Upper limit NI deducted is: {float(taxable_uel_ni)}")
    print(f"Above upper limit NI deducted is: {float(above_uel_ni)}")
    print(f"Total National Insurance deducted is: {float(national_insurance)}")

    return national_insurance


def workout_take_home(gross_earnings, income_tax_deducted, national_insurance):
    """
    Returns take home amount using the annual salary figure, tax deducted and
    national insurance deducteds
    """
    income_tax = int()
    take_home = int(gross_earnings) - (int((national_insurance) + int(income_tax)))

    print(f"monthly take home is: {float(take_home)}")

    return take_home / 12


def give_results(tax_code, gross_earnings, tax, national_insurance, take_home):
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
    gross_earnings = get_gross_earnings()
    tax_code = get_tax_code()
    # extract_tax_free_from_tax_code(tax_code)
    tax_free_amt = extract_tax_free_from_tax_code(tax_code)
    workout_income_tax_breakdown(tax_free_amt, gross_earnings)
    workout_national_tax_breakdown(gross_earnings)
    income_tax = workout_income_tax_breakdown(tax_free_amt, gross_earnings)
    national_insurance = workout_income_tax_breakdown(tax_free_amt, gross_earnings)
    workout_take_home(gross_earnings, income_tax, national_insurance)


main()
