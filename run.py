"""
This program allows the user to work out their monthly take home pay
using their gross earnings
Income tax and National Insurance rates are relevant to 2022/23 UK tax year
"""
import re
import texttable as tt


def show_menu():
    """
    Asks user to choose whether to continue using the calculator or quit
    """
    print('''Hi there, thank you for choosing our simple UK wage calculator,
    press:
    1. Workout Monthly Wage
    2. Quit
    ''')
    instruct = input('').strip().lower()
    possible_answers = ['1', '2']
    # validates user input
    while instruct not in possible_answers:
        print('You must enter a 1 or a 2, one of the choices...')
        instruct = input('').strip().lower()
    if instruct == '1':
        tax_code = get_tax_code()
        annual_gross_earnings = get_gross_earnings()
        tax_free_amt = extract_tax_free_from_tax_code(tax_code, annual_gross_earnings)
        annual_taxable_income = get_taxable_income(annual_gross_earnings, tax_free_amt)
        annual_income_tax = income_tax_breakdown(tax_free_amt, annual_gross_earnings, annual_taxable_income)
        annual_ni = national_insurance_breakdown(annual_gross_earnings)
        annual_take_home = workout_take_home(annual_gross_earnings, annual_income_tax, annual_ni)
        tax_table_display(annual_gross_earnings, annual_taxable_income, annual_income_tax, annual_ni, annual_take_home)
    if instruct == '2':
        exit()


def get_tax_code():
    """
    Asks user to input their tax code. Then validates that four numbers and
    a letter has been entered. Then returns the entered tax code if valid
    """
    entered_tax_code = input('Please enter your UK tax code, it must be four digits followed by a '
                             'letter').strip().lower()
    patten = re.compile('\d{4}[a-z]{1}')
    is_tax_code = patten.match(entered_tax_code)
    while is_tax_code is None:
        print('No, that is not a correctly formatted UK tax code!')
        entered_tax_code = input('Please enter your UK tax code, it must be four digits followed by a letter')
        is_tax_code = patten.match(entered_tax_code)
    return entered_tax_code


def extract_tax_free_from_tax_code(tax_code, annual_gross_earnings):
    """
    Returns the tax free amount
    """
    cleaned_tax_code = tax_code[:4]
    tax_free_amt = int(cleaned_tax_code) * 10

    if annual_gross_earnings <= 100000:
        tax_free_amt = int(cleaned_tax_code) * 10
    elif annual_gross_earnings > 100000:
        if annual_gross_earnings < 125140:
            tax_free_amt = 12570 - ((annual_gross_earnings - 100000) / 2)
    else:
        tax_free_amt = 0

    return tax_free_amt


def get_gross_earnings():
    """
    Asks user to input annual gross earnings
    """
    annual_gross_earnings = input("Enter your gross earnings here: \n")
    return int(annual_gross_earnings)


def get_taxable_income(annual_gross_earnings, tax_free_amt):
    """
    Returns taxable income dependant on gross earnings input
    """
    annual_taxable_income = 0
    tax_free_limit = 100000
    if annual_gross_earnings <= 100000:
        annual_taxable_income = annual_gross_earnings - tax_free_amt
    else:
        annual_taxable_income = annual_gross_earnings - (12570 - ((annual_gross_earnings - tax_free_limit) / 2))
    if annual_gross_earnings > tax_free_limit:
        if annual_gross_earnings < 125140:
            annual_taxable_income = annual_gross_earnings - (12570 - ((annual_gross_earnings - tax_free_limit) / 2))
        else:
            annual_taxable_income = annual_gross_earnings

    return annual_taxable_income


def income_tax_breakdown(tax_free_amt, annual_gross_earnings, annual_taxable_income):
    """
    Returns annual taxable income using annual gross earnings and tax free amount.
    Then works out the basic tax rate, high tax rate, and Higher tax rate.
    Finally returns total tax deducted.
    """
    annual_taxable_income = annual_gross_earnings - tax_free_amt
    basic_rate = 50270
    higher_rate = 150000
    basic_rate_amount = 0
    higher_rate_amt = 0
    additional_rate_amt = 0
    annual_income_tax = 0

    if annual_gross_earnings <= 50270:
        basic_rate_amount = annual_taxable_income * 0.2
    else:
        basic_rate_amount = (basic_rate - 12570) * 0.2
    if annual_gross_earnings > basic_rate:
        if annual_gross_earnings <= higher_rate:
            higher_rate_amt = (annual_gross_earnings - (37700 + tax_free_amt)) * 0.4
        else:
            higher_rate_amt = (150000 - 112300) * 0.4
            additional_rate_amt = (annual_taxable_income - higher_rate) * 0.45

        if annual_gross_earnings > higher_rate:
            additional_rate_amt = (annual_taxable_income - higher_rate) * 0.45

    print("Your Income Tax breakdown is as follows:")
    print(f"Annual taxable income is: £{annual_taxable_income:.2f}")
    print(f"Basic rate tax deducted is: £{basic_rate_amount:.2f}")
    print(f"Higher rate tax deducted is: £{higher_rate_amt:.2f}")
    print(f"Additional rate tax deducted is: £{additional_rate_amt:.2f}")
    print(f"Total income tax deducted is: {annual_income_tax:.2f}")

    annual_income_tax = basic_rate_amount + higher_rate_amt + additional_rate_amt

    return annual_income_tax


def national_insurance_breakdown(annual_gross_earnings):
    """
    Works out the class 1 national insurance amount deducted per below:
    - 0% NI tax on gross earnings below 12570
    - 12.73% NI. tax over 12570 to 50270 per year
    - 2.73% NI tax over 50270 gross earnings per year
    """
    lower_ni_limit = 12570
    basic_ni_limit = 50270
    basic_ni_amount = 0
    higher_ni_amount = 0

    if annual_gross_earnings > lower_ni_limit:
        if annual_gross_earnings <= basic_ni_limit:
            basic_ni_amount = (basic_ni_limit - lower_ni_limit) * 0.1273
        else:
            basic_ni_amount = (basic_ni_limit - lower_ni_limit) * 0.1273
            higher_ni_amount = (annual_gross_earnings - basic_ni_limit) * 0.0273

    annual_ni = basic_ni_amount + higher_ni_amount

    print("Your National Insurance Breakdown is as follows: ")
    print(f"Primary threshold NI deducted is: £{basic_ni_amount:.2f}")
    print(f"Upper limit NI deducted is: £{higher_ni_amount:.2f}")
    print(f"Total National Insurance deducted is: £{annual_ni:.2f}")

    return annual_ni


def workout_take_home(annual_gross_earnings, income_tax, annual_ni):
    """
    Returns take home amount by subtracting the income tax and
    national insurance deducted from gross earnings
    """

    annual_take_home = annual_gross_earnings - annual_ni - income_tax
    print(f"Annual take home amount is: £{annual_take_home:.2f}")

    return annual_take_home


def tax_table_display(annual_gross_earnings, annual_taxable_income, annual_income_tax, annual_ni, annual_take_home):
    """
    Returns all values breakdown assembled in a texttable
    """
    month_gross_earnings = annual_gross_earnings / 12
    month_taxable_income = annual_taxable_income / 12
    monthly_income_tax = annual_income_tax / 12
    monthly_ni = annual_ni / 12
    monthly_take_home = annual_take_home / 12

    tb = tt.Texttable()
    tb.header(["Item", "Yearly £ ", "Monthly £ "])
    tb.add_row(["Gross Earnings", annual_gross_earnings, month_gross_earnings])
    tb.add_row(["Taxable Income", annual_taxable_income, month_taxable_income])
    tb.add_row(['Income Tax', annual_income_tax, monthly_income_tax])
    tb.add_row(['National Insurance', annual_ni, monthly_ni])
    tb.add_row(['Take Home', annual_take_home, monthly_take_home])
    print(tb.draw())


def main():
    """
    Runs all program functions
    """
    show_menu()


main()
