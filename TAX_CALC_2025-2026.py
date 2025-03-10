import streamlit as st

# Function to calculate tax under new tax regime
def calculate_new_regime_tax(income, deductions):
    rebate = 60000  # Rebate for income up to ₹12,00,000
    tax = 0
    
    taxable_income = income - deductions

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
    
    # Rebate for income up to ₹12,00,000
    if income <= 1200000:
        tax = max(tax - rebate, 0)
        
    # Add Health and Education Cess of 4%
    cess = tax * 0.04
    total_tax = tax + cess
    
    return total_tax, taxable_income

# Function to calculate tax under old tax regime
def calculate_old_regime_tax(income, deductions):
    taxable_income = max(income - deductions, 0)
    
    tax = 0
    
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.20
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.30
    
    cess = tax * 0.04
    total_tax = tax + cess
    
    return total_tax, taxable_income

# Streamlit UI
def main():
    st.title("🇮🇳 Income Tax Calculator - India (FY 2025-26)")
    st.write("🔎 Calculate your income tax based on the latest slabs and deductions.")

    regime = st.radio("Choose Tax Regime", ['New Regime (2025-26)', 'Old Regime'])

    income = st.number_input("Enter your Annual Income (₹)", min_value=0, value=1000000)

    if regime == 'New Regime (2025-26)':
        st.subheader("✅ Deductions Available in New Regime")

        standard_deduction = 75000
        employer_nps = st.number_input("Employer Contribution to NPS (No limit):", min_value=0, value=0)
        epf_contribution = st.number_input("Employer Contribution to EPF (up to 12% of salary):", min_value=0, value=0)
        section_80tta = st.number_input("Interest on Savings (Senior Citizens - Max ₹50,000):", min_value=0, max_value=50000, value=0)
        professional_tax = st.number_input("Professional Tax (Max ₹2,500):", min_value=0, max_value=2500, value=0)

        total_deductions = standard_deduction + employer_nps + epf_contribution + section_80tta + professional_tax
        
        st.write(f"💡 **Total Deductions:** ₹{total_deductions:.2f}")

    else:
        st.subheader("💼 Deductions (Only for Old Regime)")
        section_80c = st.number_input("Section 80C (Max ₹1,50,000):", min_value=0, max_value=150000, value=0)
        health_insurance = st.number_input("Health Insurance Premium (Max ₹25,000):", min_value=0, max_value=25000, value=0)
        home_loan_interest = st.number_input("Home Loan Interest (Max ₹2,00,000):", min_value=0, max_value=200000, value=0)
        standard_deduction = 50000
        total_deductions = section_80c + health_insurance + home_loan_interest + standard_deduction

    if st.button("🧮 Calculate Tax"):
        if regime == 'New Regime (2025-26)':
            tax, taxable_income = calculate_new_regime_tax(income, total_deductions)
        else:
            tax, taxable_income = calculate_old_regime_tax(income, total_deductions)
        
        st.subheader("📊 Result")
        st.write(f"**Gross Income:** ₹{income:.2f}")
        st.write(f"**Taxable Income:** ₹{taxable_income:.2f}")
        st.write(f"**Total Tax Payable:** ₹{tax:.2f}")

if __name__ == "__main__":
    main()
