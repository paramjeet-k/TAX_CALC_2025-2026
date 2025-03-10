def calculate_tax(income, deductions):
    # Subtract deductions from gross income
    taxable_income = max(income - deductions, 0)
    
    tax = 0
    
    # Apply tax slabs
    if taxable_income <= 400000:
        tax = 0
    elif taxable_income <= 800000:
        tax = (taxable_income - 400000) * 0.05
    elif taxable_income <= 1200000:
        tax = 20000 + (taxable_income - 800000) * 0.10
    elif taxable_income <= 1600000:
        tax = 60000 + (taxable_income - 1200000) * 0.15
    elif taxable_income <= 2000000:
        tax = 120000 + (taxable_income - 1600000) * 0.20
    elif taxable_income <= 2400000:
        tax = 200000 + (taxable_income - 2000000) * 0.25
    else:
        tax = 300000 + (taxable_income - 2400000) * 0.30
    
    # Add Health and Education Cess of 4%
    cess = tax * 0.04
    total_tax = tax + cess
    
    return total_tax, taxable_income

def input_deductions():
    # Collect deduction details
    section_80c = min(float(input("Enter amount for Section 80C (Max ₹1,50,000): ")), 150000)
    section_80d = min(float(input("Enter amount for Section 80D (Health Insurance - Max ₹25,000): ")), 25000)
    section_24b = min(float(input("Enter amount for Home Loan Interest (Max ₹2,00,000): ")), 200000)
    section_80e = float(input("Enter amount for Education Loan Interest: "))
    section_80tta = min(float(input("Enter amount for Savings Interest (Max ₹10,000): ")), 10000)
    section_80g = float(input("Enter amount for Donations to Charity: "))
    section_80ccd = min(float(input("Enter amount for NPS Contribution (Max ₹50,000): ")), 50000)
    standard_deduction = 50000
    
    total_deductions = (section_80c + section_80d + section_24b + section_80e + 
                        section_80tta + section_80g + section_80ccd + standard_deduction)
    
    print(f"\n✅ Total deductions claimed: ₹{total_deductions:.2f}\n")
    
    return total_deductions

# Input Income and Deductions
income = float(input("Enter your annual income (in ₹): "))
print("\n👉 Now entering deductions details...\n")
deductions = input_deductions()

# Calculate Tax
tax, taxable_income = calculate_tax(income, deductions)

# Output Results
print("\n💼 SUMMARY")
print(f"🔹 Gross Income: ₹{income:.2f}")
print(f"🔹 Deductions: ₹{deductions:.2f}")
print(f"🔹 Taxable Income: ₹{taxable_income:.2f}")
print(f"🔹 Total Tax Payable (including 4% Cess): ₹{tax:.2f}")
