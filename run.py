"""
This program allows the user to work out their monthly take home pay
using their gross earnings
Income tax and National Insurance rates are relevant to 2022/23 UK tax year
"""
import re
from tabulate import tabulate


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
        taxable_income = get_taxable_income(gross_earnings, tax_free_amt)
        income_tax = income_tax_breakdown(tax_free_amt, gross_earnings, taxable_income)
        national_insurance = national_insurance_breakdown(gross_earnings)
        workout_take_home(gross_earnings, income_tax, national_insurance)
        take_home = workout_take_home(gross_earnings, income_tax, national_insurance)
        give_results(gross_earnings, income_tax, national_insurance, taxable_income, take_home)
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
    # return tax_free_amt

    if gross_earnings <= 100000:
        tax_free_amt = int(cleaned_tax_code) * 10
    elif gross_earnings > 100000:
        if gross_earnings < 125140:
            tax_free_amt = 12570 - ((gross_earnings - 100000) / 2)
    else:
        tax_free_amt = 0

    return tax_free_amt


def get_gross_earnings():
    """
    Gets user's total earnings before tax and national insurance are deducted
    """
    gross_earnings = input("Enter your gross earnings here: \n")
    return int(gross_earnings)


def get_taxable_income(gross_earnings, tax_free_amt):
    """
    Returns taxable income dependant on gross earnings
    """
    taxable_income = 0
    tax_free_limit = 100000
    if gross_earnings <= 100000:
        taxable_income = gross_earnings - tax_free_amt
    else:
        taxable_income = gross_earnings - (12570 - ((gross_earnings - tax_free_limit) / 2))
    if gross_earnings > tax_free_limit:
        if gross_earnings < 125140:
            taxable_income = gross_earnings - (12570 - ((gross_earnings - tax_free_limit) / 2))
        else:
            taxable_income = gross_earnings

    return taxable_income


def income_tax_breakdown(tax_free_amt, gross_earnings, taxable_income):
    """
    Works out taxable income by subtracting annual salary and tax free amount.
    Then works out the basic tax rate, high tax rate, and Higher tax rate.
    Finally returns total tax deducted which is the sum of all the tax rates.
    """
    taxable_income = gross_earnings - tax_free_amt
    basic_rate = 50270
    higher_rate = 150000
    basic_rate_amount = 0
    higher_rate_amt = 0
    additional_rate_amt = 0
    income_tax = 0

    if gross_earnings <= 50270:
        basic_rate_amount = taxable_income * 0.2
    else:
        basic_rate_amount = (basic_rate - 12570) * 0.2
    if gross_earnings > basic_rate:
        if gross_earnings <= higher_rate:
            # higher_rate_amt = (gross_earnings - 50270) * 0.4
            higher_rate_amt = (gross_earnings - (37700 + tax_free_amt)) * 0.4
        else:
            higher_rate_amt = (150000 - 112300) * 0.4
            additional_rate_amt = (taxable_income - higher_rate) * 0.45

        if gross_earnings > higher_rate:
            additional_rate_amt = (taxable_income - higher_rate) * 0.45
        # else:
            # print("no higher rate tax deducted")

    print("Your Income Tax breakdown is as follows:")
    print(f"Taxable income is: £{taxable_income:.2f}")
    print(f"Basic rate tax deducted is: £{basic_rate_amount:.2f}")
    print(f"Higher rate tax deducted is: £{higher_rate_amt:.2f}")
    print(f"Additional rate tax deducted is: £{additional_rate_amt:.2f}")
    # print(f"Total income tax deducted is: {income_tax:.2f}")

    # income_tax = int(basic_rate_amount) + int(higher_rate_amt) + int(additional_rate_amt)

    return income_tax


def national_insurance_breakdown(gross_earnings):
    """
    Works out the class 1 national insurance amount deducted per below:
    - 0% NI tax on gross earnings below 12570
    - 12.73% NI. tax over 12570 to 50270 per year  
    - 2.73% NI tax over 50270 gross earnings per year
    """
    lower_ni_limit = 12570
    # lower_ni_limit = 11908
    basic_ni_limit = 50270
    basic_ni_amount = 0
    higher_ni_amount = 0

    if gross_earnings > lower_ni_limit:
        if gross_earnings <= basic_ni_limit:
            basic_ni_amount = (basic_ni_limit - lower_ni_limit) * 0.1273
        else:
            basic_ni_amount = (basic_ni_limit - lower_ni_limit) * 0.1273
            higher_ni_amount = (gross_earnings - basic_ni_limit) * 0.0273

    national_insurance = basic_ni_amount + higher_ni_amount

    print("Your National Insurance Breakdown is as follows: ")
    print(f"Primary threshold NI deducted is: £{basic_ni_amount:.2f}")
    print(f"Upper limit NI deducted is: £{higher_ni_amount:.2f}")
    print(f"Total National Insurance deducted is: £{national_insurance:.2f}")

    return national_insurance


def workout_take_home(gross_earnings, income_tax, national_insurance):
    """
    Returns take home amount by subtracting the income tax and
    national insurance deducted from gross earnings 
    """

    take_home = gross_earnings - national_insurance - income_tax
    print(f"Annual take home amount is: £{take_home:.2f}")

    return take_home


def give_results(gross_earnings, income_tax, national_insurance, taxable_income, take_home):
    """
    Presents the take home amount alongside gross earnings, income tax and
    nataional insurance deductions in a table
    """
    annual_gross_earnings = gross_earnings
    monthly_gross_earnings = gross_earnings / 12
    annual_taxable_income = taxable_income
    monthly_taxable_income = taxable_income / 12
    annual_income_tax = income_tax
    monthly_income_tax = income_tax / 12
    annual_ni = national_insurance
    monthly_ni = national_insurance / 12
    annual_take_home = take_home
    monthly_take_home = take_home / 12

    tax_data = [
        ['Gross Earnings', {annual_gross_earnings}, {monthly_gross_earnings}],
        ["Taxable Income", {annual_taxable_income}, {monthly_taxable_income}],
        ['Income Tax', {annual_income_tax}, {monthly_income_tax}],
        ['National Insurance', {annual_ni}, {monthly_ni}],
        ['Take Home', {annual_take_home}, {monthly_take_home}]
    ]
    print(tabulate(tax_data, headers=["Type", "Yearly", "Monthly"]))


def main():
    """
    Runs all program functions
    """
    show_menu()


main()
