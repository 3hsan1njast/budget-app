def two_decimal(number: float):
    number = str(number)
    if len(number.split('.')[1]) == 1: number = str(number) + '0'
    return number


def round_down_to_nearest_10(num):
    return (num // 10) * 10


def calculate_percentages(categories: list):
    total_amount = float(0)
    spent_percentages = []

    for category in categories:
        total_amount += category.total_spent

    for category in categories:
        percentage = round_down_to_nearest_10(category.total_spent / total_amount * 100)
        spent_percentages.append({category.name: percentage})

    return spent_percentages


def create_spend_chart(categories: list):
    spent_percentages = calculate_percentages(categories)
    category_names_length = []
    chart = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        if i == 0:
            chart += f'  {i}|'
        elif i != 100:
            chart += f' {i}|'
        else:
            chart += f'{i}|'
        for j in range(len(categories)):
            percent = list(spent_percentages[j].values())[0]
            length = len(list(spent_percentages[j].keys())[0])
            if length not in category_names_length: category_names_length.append(length)
            if i <= percent:
                chart += f' o '
            elif i > percent:
                chart += f'   '
            if j == len(categories) - 1: chart += ' '
        chart += '\n'
    chart += '    '
    for _ in categories:
        chart += '---'
    chart += '-'
    longest_length = max(category_names_length)
    for i in range(longest_length):
        chart += "\n    "
        for j in range(len(categories)):
            try:
                chart += f' {categories[j].name[i]} '
            except IndexError:
                chart += '   '
            if j == len(categories) - 1:
                chart += ' '

    return chart


class Category:
    def __init__(self, name):
        self.name = name
        self.balance = float(0)
        self.total_spent = float(0)
        self.ledger = []

    def __str__(self):
        total_length = 30
        description_length = 23
        amount_length = 7

        # Title
        star_count = (total_length - len(self.name)) / 2
        title = ''
        for _ in range(int(star_count)): title += '*'
        title += self.name
        if not len(self.name) % 2 == 0:
            for _ in range(int(star_count) + 1): title += '*'
        else:
            for _ in range(int(star_count)): title += '*'

        # Items in the ledger
        items = ''
        for item in self.ledger:
            amount = two_decimal(item['amount'])
            description = item['description']
            for i in range(description_length):
                try:
                    items += description[i]
                except IndexError:
                    items += " "

            for j in range(amount_length - len(str(amount))):
                items += " "

            items += str(amount) + "\n"

        return f'{title}\n{items}Total: {self.balance}'

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def deposit(self, amount, description=''):
        amount = float(amount)
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        amount = float(amount)
        if self.check_funds(amount):
            self.balance -= amount
            self.total_spent += amount
            self.ledger.append({'amount': amount - (2 * amount), 'description': description})
            return True
        return False

    def transfer(self, amount, category):
        amount = float(amount)
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False


food = Category('Food')

food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25, 'medical')
auto = Category('Auto')
auto.deposit(200)
auto.withdraw(100)

print(create_spend_chart([food, clothing, auto]))
