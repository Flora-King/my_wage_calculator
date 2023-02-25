# this program enables you to work out your monthly take home pay

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
    this function asks the user to input a tax code. it then uses a regular expression which validates
    that four numbers and a letter has been inputted. Upon getting a valid response it returns the entered tax code
    :return: entered tax code
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
    """ write doc string here """
    cleaned_tax_code = tax_code[:4]
    tax_free_amount = int(cleaned_tax_code) * 10
    return tax_free_amount


def get_annual_salary():
    return


def workout_tax_breakdown(tax_free, salary):
    return


def workout_nation_insurance(tax_free, salary):
    return


def workout_take_home(annualSalary, tax, nationalInsurance):
    return


def give_results(taxcode, salary, tax, nationalInsurance, takehome):
    return



show_menu()
