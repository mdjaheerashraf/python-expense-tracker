import matplotlib.pyplot as plt

expenses = {}
total = 0

while True:
    category = input("Enter category (Food/Travel/etc): ").strip()
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        continue

    total += amount
    expenses[category] = expenses.get(category, 0) + amount

    more = input("Add more? (yes/no): ").strip().lower()
    if more == "no":
        break

print("\n========== Expense Summary ==========")
print(f"Total Expense: {total:.2f}")

print("\nCategory-wise Breakdown:")
for cat, amt in expenses.items():
    print(f"{cat}: {amt:.2f}")

# Chart
plt.figure(figsize=(6,6))
plt.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.show()
