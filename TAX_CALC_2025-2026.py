import streamlit as st

# Function to calculate tax under new tax regime
def calculate_new_regime_tax(income):
    rebate = 60000  # Rebate for income up to ₹12,00,000
    tax = 0
    
    if income <= 400000:
        tax = 0
    elif income <= 800000:
        tax = (income - 400000) * 0.05
    elif income <= 1200000:
        tax = 20000 + (income - 800000) * 0.10
    elif income <= 1600000:
        tax = 60000 + (income - 1200000) * 0.15
    elif income <= 2000000:
        tax = 120000 + (income - 1600000) * 0.20
    elif income <= 2400000:
        tax = 200000 + (income - 2000000) * 0.25
    else:
        tax = 300000 + (income - 2400000) * 0.30
    
    # Rebate for income up to ₹12,00,000
    if income <= 1200000:
        tax = max(tax - rebate, 0)
        
    # Add Health and Education Cess of 4%
    cess = tax * 0.04
    total_tax = tax + cess
    
    return total_tax

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
    
    # Add Health and Education Cess of 4%
    cess = tax * 0.04
    total_tax = tax + cess
    
    return total_tax, taxable_income

# Streamlit UI
def main():
    st.title("🇮🇳 Income Tax Calculator - India (FY 2025-26)")
    st.write("🔎 Calculate your income tax based on the latest slabs and deductions.")

    # Option to select tax regime
    regime = st.radio("Choose Tax Regime", ['New Regime (2025-26)', 'Old Regime'])

    # Input Section
    income = st.number_input("Enter your Annual Income (₹)", min_value=0, value=1000000)

    if regime == 'Old Regime':
        st.subheader("💼 Deductions (Only for Old Regime)")

        section_80c = st.number_input("Section 80C - Investments (Max ₹1,50,000):", min_value=0, max_value=150000, value=0)
        section_80d = st.number_input("Section 80D - Health Insurance Premium (Max ₹25,000):", min_value=0, max_value=25000, value=0)
        section_24b = st.number_input("Section 24(b) - Home Loan Interest (Max ₹2,00,000):", min_value=0, max_value=200000, value=0)
        section_80e = st.number_input("Section 80E - Education Loan Interest:", min_value=0, value=0)
        section_80tta = st.number_input("Section 80TTA - Savings Interest (Max ₹10,000):", min_value=0, max_value=10000, value=0)
        section_80g = st.number_input("Section 80G - Donations to Charity:", min_value=0, value=0)
        section_80ccd = st.number_input("Section 80CCD(1B) - NPS Contribution (Max ₹50,000):", min_value=0, max_value=50000, value=0)

        # Apply standard deduction for salaried individuals in old regime
        standard_deduction = 50000
        total_deductions = (
            section_80c + section_80d + section_24b + section_80e +
            section_80tta + section_80g + section_80ccd + standard_deduction
        )
        
        st.write(f"✅ **Total Deductions:** ₹{total_deductions:.2f}")

    if st.button("🧮 Calculate Tax"):
        if regime == 'New Regime (2025-26)':
            if income <= 1275000:
                st.success("✅ No tax payable (including rebate and standard deduction)!")
            else:
                tax = calculate_new_regime_tax(income)
                st.subheader("📊 Result")
                st.write(f"**Gross Income:** ₹{income:.2f}")
                st.write(f"**Total Tax Payable (including 4% Cess):** ₹{tax:.2f}")

        elif regime == 'Old Regime':
            tax, taxable_income = calculate_old_regime_tax(income, total_deductions)
            st.subheader("📊 Result")
            st.write(f"**Gross Income:** ₹{income:.2f}")
            st.write(f"**Deductions:** ₹{total_deductions:.2f}")
            st.write(f"**Taxable Income:** ₹{taxable_income:.2f}")
            st.write(f"**Total Tax Payable (including 4% Cess):** ₹{tax:.2f}")
            if tax == 0:
                st.success("✅ No tax payable!")
            else:
                st.warning(f"⚠️ You have to pay ₹{tax:.2f} as tax.")

if __name__ == "__main__":
    main()
