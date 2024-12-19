# Import required libraries
from tabulate import tabulate
from datetime import datetime, timedelta

# Step 1: Initialize Static Data
# These are static details related to the consumer and the bill
tariff = "A-1b(01)"  # Tariff applied for the consumer
load = 2  # Load in kW
old_ac_number = "0"  # Placeholder for old account number
division = "Central"  # Area division
sub_division = "Model Town"  # Subdivision name
feeder_name = "College Road"  # Name of the feeder
meter_no = "123456"  # Meter number

# Step 2: Input Consumer Details
# Input consumer name, address, reference number, and consumer ID (DOB)
name = input("Enter your full name: ")
address = input("Enter your address: ")
reference_no = input("Enter your Roll.No(as a reference number): ")
consumer_id = input("Enter your date of birth (DDMMYYYY format): ")  # Example: DDMMYYYY format for 20-07-2003

# Step 3: Validate Reference Number
# Ensure the reference number is numeric and at least 4 digits
while not reference_no.isdigit() or len(reference_no) < 4:
    print("Invalid reference number. It must be at least 4 digits and numeric.")
    reference_no = input("Enter your reference number (at least 4 digits): ")

# Step 4: Initialize Dynamic Data
# Set previous reading and calculate present reading based on reference number
previous_reading = 9742  # Example previous reading
present_reading = 9742 + int(reference_no[-4:])  # Simulate unique consumption based on reference number
units_consumed = present_reading - previous_reading  # Calculate units consumed
meter_factor = 1  # Meter factor (typically 1 for most meters)

# Step 5: Cost Calculations
# Cost per unit of electricity and total cost of electricity
unit_cost = 20  # Fixed cost per unit in Rs
cost_of_electricity = units_consumed * unit_cost  # Total cost for electricity consumed

# Additional fixed charges
fuel_price_adjustment = 700  # Fuel price adjustment
fc_surcharge = 90  # Fuel surcharge
qtr_tariff_adjustment = -14  # Quarterly tariff adjustment

# Total charges excluding TV fee, GST, and FPA
total1 = cost_of_electricity + fuel_price_adjustment + fc_surcharge + qtr_tariff_adjustment

# Step 6: TV Fee, GST, and Other Charges
tv_fee = 35  # TV fee
gst = 800  # GST amount
gst_on_fpa = 108  # GST on fuel price adjustment
total2 = tv_fee + gst + gst_on_fpa  # Total of TV fee, GST, and other charges

# Step 7: Final Bill Calculation
# Calculate the current bill, total FPA, and the payable amounts
current_bill = total1 + total2  # Sum of all charges
total_fpa = 700  # Total FPA charge
payable_within_due_date = current_bill + total_fpa  # Amount payable within due date
lp_surcharge = 400  # Late payment surcharge
payable_after_due_date = payable_within_due_date + lp_surcharge  # Amount payable after due date

# Step 8: Dynamic Date Calculation
# Set dynamic dates based on the current date
today = datetime.today()

# Set dynamic dates based on today
connection_date = (today - timedelta(days=365)).strftime("%d %b %y")  # Connection date one year ago
bill_month = today.strftime("%b %y")  # Current month
reading_date = (today.replace(day=5)).strftime("%d-%b-%y")  # Reading date set to 5th of the current month
issue_date = (today + timedelta(days=1)).strftime("%d-%b-%y")  # Issue date is the next day
due_date = (today + timedelta(days=5)).strftime("%d-%b-%y")  # Due date is 5 days after the issue date

# Step 9: Generate Output Using Tabulate
# Organize the bill details into a list for tabular display
bill_data = [
    ["Connection Date", connection_date],
    ["Bill Month", bill_month],
    ["Reading Date", reading_date],
    ["Issue Date", issue_date],
    ["Due Date", due_date],
    ["Consumer ID", consumer_id],
    ["Tariff", tariff],
    ["Load", load],
    ["Division", division],
    ["Sub Division", sub_division],
    ["Feeder Name", feeder_name],
    ["Reference No", reference_no],
    ["Name & Address", f"{name}, {address}"],
    ["Meter No", meter_no],
    ["Previous Reading", previous_reading],
    ["Present Reading", present_reading],
    ["Units Consumed", units_consumed],
    ["Cost of Electricity", f"Rs. {cost_of_electricity}"],
    ["Fuel Price Adjustment", f"Rs. {fuel_price_adjustment}"],
    ["F.C Surcharge", f"Rs. {fc_surcharge}"],
    ["QTR Tariff Adjustment", f"Rs. {qtr_tariff_adjustment}"],
    ["Total 1", f"Rs. {total1}"],
    ["TV Fee", f"Rs. {tv_fee}"],
    ["GST", f"Rs. {gst}"],
    ["GST on FPA", f"Rs. {gst_on_fpa}"],
    ["Total 2", f"Rs. {total2}"],
    ["Current Bill", f"Rs. {current_bill}"],
    ["Total FPA", f"Rs. {total_fpa}"],
    ["Payable Within Due Date", f"Rs. {payable_within_due_date}"],
    ["L.P. Surcharge", f"Rs. {lp_surcharge}"],
    ["Payable After Due Date", f"Rs. {payable_after_due_date}"],
]

# Step 10: Print the formatted bill
# Using the tabulate library to display the bill in a table format
print("\nElectricity Bill:\n")
print(tabulate(bill_data, headers=["Field", "Details"], tablefmt="grid"))

# Step 11: Added Appropriate Comments
# The code is commented thoroughly to explain the purpose of each section.
# This structure allows for easy understanding and maintenance.
