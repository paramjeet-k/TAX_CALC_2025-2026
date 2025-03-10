import streamlit as st

# Function to calculate income tax based on latest slabs
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

# Streamlit UI
def main():
    st.title("🇮🇳 Income Tax Calculator - India (2024-25)")
    st.write("🔎 Calculate your income tax based on the latest slabs and deductions.")

    # Input Section
    income = st.number_input("Enter your Annual Income (₹)", min_value=0, value=1000000)

    # Deductions Section
    st.subheader("💼 Deductions")

    section_80c = st.number_input("Section 80C - Investments (Max ₹1,50,000):", min_value=0, max_value=150000, value=0)
    section_80d = st.number_input("Section 80D - Health Insurance Premium (Max ₹25,000):", min_value=0, max_value=25000, value=0)
    section_24b = st.number_input("Section 24(b) - Home Loan Interest (Max ₹2,00,000):", min_value=0, max_value=200000, value=0)
    section_80e = st.number_input("Section 80E - Education Loan Interest:", min_value=0, value=0)
    section_80tta = st.number_input("Section 80TTA - Savings Interest (Max ₹10,000):", min_value=0, max_value=10000, value=0)
    section_80g = st.number_input("Section 80G - Donations to Charity:", min_value=0, value=0)
    section_80ccd = st.number_input("Section 80CCD(1B) - NPS Contribution (Max ₹50,000):", min_value=0, max_value=50000, value=0)

    # Apply standard deduction for salaried individuals
    st.write("✅ Standard Deduction of ₹50,000 applied for salaried individuals.")
    standard_deduction = 50000

    # Total Deductions Calculation
    total_deductions = (
        section_80c + section_80d + section_24b + section_80e +
        section_80tta + section_80g + section_80ccd + standard_deduction
    )

    st.write(f"💡 **Total Deductions:** ₹{total_deductions:.2f}")

    # Calculate tax when button is clicked
    if st.button("🧮 Calculate Tax"):
        tax, taxable_income = calculate_tax(income, total_deductions)

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
