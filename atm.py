print("Welcome to ABC Bank")
class Bank():
    acbal = 10000
    count = 0
    def viewOptions(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")
    def deposite(self):
        dep = int(input("Enter the amount to be deposited: "))
        if dep < 100:
            print("Minimum deposit amount should be 100")
        elif dep % 100 != 0:
            print("Amount should be a multiple of 100")
        elif dep > 50000:
            print("Maximum deposit amount is 50000")
        else:
            self.acbal=self.acbal+dep
            print("Your balance after deposition is", self.acbal)

    def withdraw(self):
        if self.count >= 3:
            print("Transaction limit is 3 times")
            return
        wit = int(input("Enter the amount to be withdrawn: "))
        if self.acbal > 500:
            if wit < 100:
                print("Minimum amount to withdraw is 100")
            elif wit % 100 != 0:
                print("Amount should be a multiple of 100")
            elif wit > self.acbal:
                print("Withdraw amount should be less than account balance")
            elif wit > 20000:
                print("Transaction amount limit is 20000")
            else:
                self.acbal=self.acbal-wit
                self.count=self.count+1
                print("Your balance after withdrawal is", self.acbal)
        else:
            print("Insufficient balance")
    def bal(self):
        print("Your current balance is", self.acbal)
    def validation(self):
        for i in range(3, 0, -1):
            pin = int(input("Enter your pin: "))
            if pin == 1234:
                self.viewOptions()
                while True:
                    choice = int(input("Enter your choice: "))
                    match choice:
                        case 1:
                            self.deposite()
                        case 2:
                            self.withdraw()
                        case 3:
                            self.bal()
                        case 4:
                            print("exiting")
                            exit()
                        case 0:
                            print("Invalid choice")
                break
            else:
                if i == 1:
                    print("Card blocked")
                else:
                    print("Invalid pin number. Attempts left:", i - 1)

obj = Bank()
obj.validation()