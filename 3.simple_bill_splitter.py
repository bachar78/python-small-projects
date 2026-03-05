
num_people = int(input("How many people are splitting the bill? ").strip())
names = []
for i in range(num_people):
    name = input(f"Enter the name of person {i+1}: ").strip()
    names.append(name)
def get_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.") 
total_bill = get_float("What is the total bill amount? ")
share = round(total_bill / num_people, 2)

print("\nBill Split:")
for name in names:
    print(f"{name} owes: ${share:.2f}")

