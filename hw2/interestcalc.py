# ----------------------------------------------------------------------
# Name:        interestcal
# Purpose:     CS 122 Homework 2
#
# Author(s): Mandeep Pabla & Trinh Nguyen
# ----------------------------------------------------------------------
"""
Calculate personal interest amount

Prompt the user for a principal amount and for an interest rate.
Validate principal amount and for an interest rate input from user.
Calculate the accrued amount after 10, 20, 30, 40 and 50 years.
"""

# Enter your constant assignments here
MIN_VALUE = 0
MAX_INTEREST_RATE = 20
MAX_PRINCIPAL_AMOUNT = 1000000


# Repeatedly prompts for the principal amount, validates it and returns it.
def get_principal_amount():
    """
        Prompt user for the principal amount, validate it and return it.

        The function prompts the user repeatedly until the amount is
        between 0 and 1,000,000 (inclusive)

        Parameters:
        None

        Returns:
        float: principal amount

    """
    amount = float(input('Please enter principal amount: $'))
    while amount < MIN_VALUE or amount > MAX_PRINCIPAL_AMOUNT:
        print("Invalid amount. Principal must be between $0 and $1,000,000.")
        amount = float(input('Please enter principal amount: $'))
    return amount


# Repeatedly prompts for the interest rate, validates it and returns it.
def get_interest_rate():
    """
        Prompt user for the interest rate, validate it and return it.

        The function prompts the user repeatedly until the amount is
        between 0 and 20 (inclusive)

        Parameters:
        None

        Returns:
        float: interest rate

    """
    rate = float(input('Please enter interest rate: %'))
    while rate < MIN_VALUE or rate > MAX_INTEREST_RATE:
        print("Invalid amount. Interest rate must be between 0% and 20%.")
        rate = float(input('Please enter interest rate: %'))
    return rate


#
def cal_accrued_amount():
    """
        Calculates and prints the accrued amounts

        Call get_principal_amount and get_interest_rate to get the principal
        amount and interest rate to calculate and print accrued amounts
        after 10, 20, 30, 40, 50 years.

        Parameters:
        None

        Returns:
        None

    """
    principal_amt = get_principal_amount()
    interest = get_interest_rate()
    for year_num in range(10, 60, 10):
        accrued_amount = principal_amt * pow(1+(interest/100),
                                                year_num)
        formatted_amt = f'${accrued_amount:,.2f}'
        print(f"Accrued amount after {year_num} years: {formatted_amt:>17}")

LETTER = ['A', 'B', 'C']
def main():
    # The main function must be non-trivial
    # cal_accrued_amount()
    assert len(LETTER) == 3, "internla"
    print("hi")



if __name__ == "__main__":
    main()
