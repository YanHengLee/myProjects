class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total_amount = 0
        self.withdraw_amount = 0

    # to check if theres enough funds
    def check_funds(self, amount):
        # if not enough
        if amount > self.total_amount:
            return False
        return True

    # deposit amount into category
    def deposit(self, amount, description=None):
        # check if there is description or not
        if description is not None:
            self.dict = {"amount": amount, "description": description}
        else:
            self.dict = {"amount": amount, "description": ""}

        self.ledger.append(self.dict)
        self.total_amount += amount

    # withdraw amount from category
    def withdraw(self, amount, description=None):

        # first check if there is enough money to withdraw
        yes = self.check_funds(amount)
        if yes:
            # check for description
            if description is not None:
                self.dict = {"amount": -amount, "description": description}
            else:
                self.dict = {"amount": -amount, "description": ""}

            self.ledger.append(self.dict)
            self.total_amount -= amount
            self.withdraw_amount += amount
            return True
        # just return false if not enough
        return False

    # transfer money from a category to another
    def transfer(self, amount, category):
        # check if there is enough funds
        yes = self.check_funds(amount)
        if yes:
            # for the category than transfers the money
            self.dict = {"amount": -amount, "description": "Transfer to " + str(category.name).capitalize()}
            self.ledger.append(self.dict)
            self.total_amount -= amount
            self.withdraw_amount += amount

            # for the category that receives the money
            category.dict = {"amount": amount, "description": "Transfer from " + str(self.name).capitalize()}
            category.ledger.append(category.dict)
            category.total_amount += amount
            return True
        # return false if not enough
        return False

    # get the total balance (after deposit, withdraw, transfer)
    def get_balance(self):
        return self.total_amount

    def __str__(self):
        title = f"{str(self.name).capitalize():*^30}\n"
        events = f""

        for i in range(len(self.ledger)):
            description = self.ledger[i]['description'][:23] # the description only contain 23 words
            amount = self.ledger[i]['amount']
            # alignment for the amount(right align)
            align = 30 - len(str(description)) - len(str(".2f".format(amount))) + 2
            events += f"{description} {amount:>{align}.2f}\n" # the amount with 2 decimal in every amount
        last = f"Total: {self.get_balance():.2f}"
        output = title + events + last

        return output


def create_spend_chart(categories):
    line1 = "Percentage spent by category\n"
    line2 = ""
    line3 = ""
    line4 = ""

    total_with_amt = 0
    # to get the total withdraw amount from every category
    for name in categories:
        total_with_amt += name.withdraw_amount

    bar_of_zeros = []
    for name in categories:
        # calculate the amount of "o" for every category
        percentage = ((name.withdraw_amount / total_with_amt) * 100) // 10 + 1
        zeros = int(percentage) * "o"
        output = zeros.rjust(11)  # right align all the "o" so that it starts from bottom of the chart
        bar_of_zeros.append(output)

    # making the bar chart containing number , "|", "o"
    for i, nums in enumerate(range(100, -10, -10)):
        line2 += f"{nums:>3}| " + "  ".join([zero[i] for zero in bar_of_zeros]) + "  \n"

    # calculate the dashes that are needed
    dashes = "-" * (len(categories) * 3 + 1)
    align = len(dashes) + 4  # right align the dashes
    line3 += dashes.rjust(align) + "\n"

    new_catgr_names = []
    for category in categories:
        new_catgr_names.append(str(category.name).capitalize())

    # getting the longest lenght for the names of category
    max_len = max([len(str(category.name)) for category in categories])
    # add spaces to names that are not longest
    for i in range(max_len):
        nameStr = "     "
        for category in new_catgr_names:
            if i >= len(category):
                nameStr += "   "
            else:
                nameStr += category[i] + "  "
        nameStr += "\n"
        line4 += nameStr

    final_output = line1.lstrip() + line2 + line3 + line4
    return final_output.rstrip("\n")
