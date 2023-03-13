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
        gross_earnings = get_gross_earnings()
        tax_free_amt = extract_tax_free_from_tax_code(tax_code, gross_earnings)
        taxable_income = get_taxable_income(gross_earnings, tax_free_amt)
        income_tax = income_tax_breakdown(tax_free_amt, gross_earnings, taxable_income)
        nat_ins = national_insurance_breakdown(gross_earnings)
        take_home = workout_take_home(gross_earnings, income_tax, nat_ins)
        tax_table(gross_earnings, taxable_income, income_tax, nat_ins, take_home)
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
        entered_tax_code = ("input('Please enter your UK tax code, it must"
                            "be four digits followed by a letter')")
        is_tax_code = patten.match(entered_tax_code)
    return entered_tax_code


def extract_tax_free_from_tax_code(tax_code, gross_earnings):
    """
    Returns the tax free amount
    """
    tax_free_lmt = 100000
    cleaned_tax_code = tax_code[:4]
    tax_free_amt = int(cleaned_tax_code) * 10

    if int(gross_earnings) <= tax_free_lmt:
        tax_free_amt = int(cleaned_tax_code) * 10
    elif int(gross_earnings) > tax_free_lmt:
        if gross_earnings < 125140:
            tax_free_amt = 12570 - ((gross_earnings - 100000) / 2)
    else:
        tax_free_amt = 0

    return tax_free_amt


def get_gross_earnings():
    """
    Asks user to input annual gross earnings
    """
    gross_earnings = int(input("Enter your gross earnings here: \n"))
    return gross_earnings


def get_taxable_income(gross_earnings, tax_free_amt):
    """
    Returns annual taxable income dependant using input annual gross earnings
    """
    taxable_income = int(0)
    tax_free_lmt = 100000

    if gross_earnings <= tax_free_lmt:
        taxable_income = gross_earnings - tax_free_amt
    else:
        taxable_income = ('gross_earnings - (12570 - ((gross_earnings -'
                          ' tax_free_lmt) / 2))')
    if gross_earnings > 100000:
        if gross_earnings < 125140:
            taxable_income = ('gross_earnings - (12570 - ((gross_earnings -'
                              ' tax_free_lmt) / 2))')
        else:
            taxable_income = gross_earnings
    if gross_earnings <= tax_free_amt:
        taxable_income = 0

    return taxable_income


def income_tax_breakdown(tax_free_amt, gross_earnings, taxable_income):
    """
    Returns annual taxable income using annual gross earnings and tax free
    amount. Then works out the basic tax rate, high tax rate, and Higher
    tax rate. And finally returns total tax deducted.
    """
    basic_rate = 50270
    high_rate = 150000
    basic_rate_amt = 0
    high_rate_amt = 0
    higher_rate_amt = 0
    income_tax = int()

    if gross_earnings <= basic_rate:
        basic_rate_amt = taxable_income * 0.2
    else:
        basic_rate_amt = (basic_rate - tax_free_amt) * 0.2
    if gross_earnings > basic_rate:
        if gross_earnings <= high_rate:
            high_rate_amt = (gross_earnings - 37700) * 0.4
        else:
            high_rate_amt = (high_rate - 112300) * 0.4
            higher_rate_amt = (taxable_income - high_rate) * 0.45

        if gross_earnings > high_rate:
            higher_rate_amt = (taxable_income - high_rate) * 0.45

    print("Your Income Tax breakdown is as follows:")
    print(f"Annual taxable income is: £{taxable_income:.2f}")
    print(f"Basic rate tax deducted is: £{basic_rate_amt:.2f}")
    print(f"Higher rate tax deducted is: £{high_rate_amt:.2f}")
    print(f"Additional rate tax deducted is: £{higher_rate_amt:.2f}")
    print(f"Total income tax deducted is: {income_tax:.2f}")

    income_tax = int(basic_rate_amt) + int(high_rate_amt) + int(higher_rate_amt)

    return int(income_tax)


def national_insurance_breakdown(gross_earnings):
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

    if gross_earnings > lower_ni_limit:
        if gross_earnings <= basic_ni_limit:
            basic_ni_amount = (basic_ni_limit - lower_ni_limit) * 0.1273
        else:
            basic_ni_amount = (basic_ni_limit - lower_ni_limit) * 0.1273
            higher_ni_amount = (gross_earnings - basic_ni_limit) * 0.0273

    nat_ins = int(basic_ni_amount) + int(higher_ni_amount)

    print("Your National Insurance Breakdown is as follows: ")
    print(f"Primary threshold NI deducted is: £{basic_ni_amount:.2f}")
    print(f"Upper limit NI deducted is: £{higher_ni_amount:.2f}")
    print(f"Total National Insurance deducted is: £{nat_ins:.2f}")

    return nat_ins


def workout_take_home(gross_earnings, income_tax, nat_ins):
    """
    Returns take home amount by subtracting the income tax and
    national insurance from gross earnings
    """
    print({"gross_earnings": gross_earnings, "income_tax": income_tax, "nat_ins": nat_ins})
    take_home = int(gross_earnings) - int(income_tax) - int(nat_ins)
    print(f"Annual take home amount is: £{take_home:.2f}")

    return int(take_home)


def tax_table(gross_earnings, taxable_income, income_tax, nat_ins, take_home):
    """
    Returns all values breakdown assembled in a texttable
    """
    month_gross_earnings = gross_earnings / 12
    month_taxable_income = taxable_income / 12
    monthly_income_tax = income_tax / 12
    monthly_ni = nat_ins / 12
    monthly_take_home = take_home / 12

    tb = tt.Texttable()
    tb.header(["Item", "Yearly £ ", "Monthly £ "])
    tb.add_row(["Gross Earnings", gross_earnings, month_gross_earnings])
    tb.add_row(["Taxable Income", taxable_income, month_taxable_income])
    tb.add_row(['Income Tax', income_tax, monthly_income_tax])
    tb.add_row(['National Insurance', nat_ins, monthly_ni])
    tb.add_row(['Take Home', take_home, monthly_take_home])
    print(tb.draw())


def main():
    """
    Runs all program functions
    """
    show_menu()


main()
