# Stage 1
# items = {'Bubblegum':2,'Toffee':0.2,'Ice cream':5,'Milk chocolate':4,'Doughnut':2.5,'Pancake':3.2}
# print('Prices:')
# for key,value in items.items():
#     print(f'{key}: ${value}')

# Stage 2
# monthly_report = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250, 'Milk chocolate': 1680, 'Doughnut': 1075,
#                   'Pancake': 80}
#
# income = 0
#
# print('Earned amount:')
# for key, value in monthly_report.items():
#     income += value
#     print(f'{key}: ${value}')
#
# print(f'\nIncome: ${income:.1f}')

# Stage 3
monthly_report = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250, 'Milk chocolate': 1680, 'Doughnut': 1075,
                  'Pancake': 80}

income = 0

print('Earned amount:')
for key, value in monthly_report.items():
    income += value
    print(f'{key}: ${value}')

print(f'\nIncome: ${income:.1f}')

print(f'Staff Expenses:')
staff_expenses = int(input())

print(f'Other expenses:')
other_expenses = int(input())

net_income = income - staff_expenses - other_expenses
print(f'Net income: ${net_income:.1f}')