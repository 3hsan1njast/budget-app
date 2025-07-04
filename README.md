# Budget App
A Python app to manage budgets across categories and visualize spending.

## Features
- **Category Management**: Track deposits, withdrawals, and transfers.
- **Ledger System**: Records transactions with descriptions.
- **Spending Chart**: Displays a bar chart of spending percentages.
- **Precise Formatting**: Handles amounts with two decimal places.

## Examples
```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)  # Outputs formatted ledger
print(create_spend_chart([food, clothing]))  # Outputs spending chart
```

## Notes
- Supports up to 4 categories in the spending chart.
- Built with ❤️ by Ehsan.
