# loan_calculator is a program to calculate different financial parameters and help you make an informed descision.
# The program can be directly run through the command line.

# modules
import math
import argparse

# parsing the arguments for calculations
parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", type=str, help="type of payment")
parser.add_argument("--payment", type=float, help="monthly payment amount")
parser.add_argument("--principal", type=float, help="loan principal")
parser.add_argument("--periods", type=float, help="number of months")
parser.add_argument("--interest", type=float, help="nominal interest")
args = parser.parse_args()

# loading the parsed arguments in the variables
A = args.payment
P = args.principal
n = args.periods

# print the message if the total parsed arguments <= 4 or interest is not passed
if len(vars(args)) <= 4 or not args.interest:
    print("Incorrect parameters.")
else:
    # nominal interest rate
    i = args.interest / (12 * 100)

    # calculations if type is annuity
    if args.type == "annuity":

        # calculate the payment
        if not args.payment:
            A = math.ceil(P * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
            print("Your monthly payment = {}!".format(A))
            print("Overpayment = {}".format(int((A * n) - P)))

        # calculate the principal
        elif not args.principal:
            P = round(A / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
            print("Your loan principal = {}!".format(P))
            print("Overpayment = {}".format(int((A * n) - P)))

        # calculate the periods
        elif not args.periods:
            n = math.ceil(math.log((A / (A - (i * P))), (1 + i)))
            years = n // 12
            months = round(n % 12)
            if years == 0:
                if months > 1:
                    print("It will take {} months to repay this loan!".format(months))
                else:
                    print("It will take {} month to repay this loan!".format(months))
            elif months == 0:
                if years > 1:
                    print("It will take {} years to repay this loan!".format(years))
                else:
                    print("It will take {} year to repay this loan!".format(years))
            print("It will take {} years and {} months to repay this loan!".format(years, months))
            print("Overpayment = {}".format(int((A * n) - P)))

    # calculations if type is diff
    elif args.type == "diff":

        # no calculation if payment is passed
        if args.payment:
            print("Incorrect parameters.")

        # calculate the differentiated payments if payment is not passed
        else:
            months = n
            m = 1
            total_payments = 0
            while months != 0:
                D = math.ceil((P / n) + i * (P - ((P * (m - 1)) / n)))
                print("Month {}: payment is {}".format(m, D))
                total_payments += D
                months -= 1
                m += 1
            print("\nOverpayment = {}".format(int(total_payments - P)))
