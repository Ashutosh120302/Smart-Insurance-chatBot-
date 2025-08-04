import pandas as pd
import re

#extract the total amount from Invioce
def extract_total(text):
    match = re.search(r'(Total|Grand Total|Amount Payable|Total Charges|Amount Due)[^\d]*(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))', text, re.IGNORECASE)
    return match.group(2) if match else "N/A"

#extract the name of the pationt
def extract_patient_name(text):
    match = re.search(r'(Patient Name|Patient|Name of Patient)[\s:]*([A-Z][a-z]+\s+[A-Z][a-z]+)', text)
    return match.group(2).strip() if match else "N/A"

#extract the date of Billing
def extract_date(text):
    match = re.search(r'(Invoice Date|Billing Date|Date of Invoice|Date)[^\d]*(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})', text, re.IGNORECASE)
    return match.group(2) if match else "N/A"

#this is a feature to extract data from the table rows 
def extract_table_rows(text):
    rows = []
    lines = text.split("\n")
    for line in lines:
        # Clean up line
        line = line.strip()
        # Match service + amount patterns (ending with price)
        match = re.match(r'(.+?)\s+[$₹£]?\s?(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?)$', line)
        if match:
            desc, price = match.groups()
            rows.append({'Description': desc.strip(), 'Price': price})
    return pd.DataFrame(rows)


# Run extractors
invoice_date = extract_date(text)
patient_name = extract_patient_name(text)
total_amount = extract_total(text)
table_df = extract_table_rows(text)



# Use the functions
print("\n=== Extracted Info ===")
print("Invoice Date:", invoice_date)
print("Pationt Name:", extract_patient_name(text))
print("Grand Total:", extract_total(text))
print(table_df)
