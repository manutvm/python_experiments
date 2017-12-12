class Customer:

    def __init__(self, account_number, customer_name, zip_code, account_date):
        self.account_number = account_number
        self.customer_name = customer_name
        self.zip_code = zip_code
        self.account_date = account_date
    
    def _print(self):
        print "Hello"    

    def printAccountInfo(self):
        print "Account Number: %s" % self.account_number
        print "Customer Name: %s" % self.customer_name
        print "Pin Code: %s" % self.zip_code
        print "Account Date: %s" % self.account_date


class Loan(Customer):
    
    def __init__(self, account_number, customer_name, zip_code, account_date, loan_account, loan_amount):
        Customer.__init__(self, account_number, customer_name, zip_code, account_date)
        self.loan_account = loan_account
        self.loan_amount = loan_amount
    
    def printLoanInfo(self):
        self.printAccountInfo()
        print "Loan Account Number: %s" % self.loan_account
        print "Loan Amount: %s" % self.loan_amount


loan = Loan("00631140023980", 'Manoj Kumar R', 695573, "01/05/1989", 9020029098, 10000)
loan._print()
loan.printLoanInfo()
