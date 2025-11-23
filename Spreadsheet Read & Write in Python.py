from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Select the active sheet
sheet = wb.active

# Write data into the sheet
sheet['A1'] = "Name"
sheet['B1'] = "Marks"

sheet['A2'] = "Alice"
sheet['B2'] = 85

sheet['A3'] = "Bob"
sheet['B3'] = 92

# Save the workbook
wb.save("student_data.xlsx")

print("Data written successfully to student_data.xlsx")
