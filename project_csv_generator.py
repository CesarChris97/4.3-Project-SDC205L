import csv
from datetime import datetime

# Student ID definition and CSV file path
student_id = "CESORT4471"
file_path = "ZooData.csv"

# Function: convertData
# Description: Converts temperature from Fahrenheit to Celsius
def convertData(val):
    return (val - 32) * 5 / 9

# Function: insertData
# Description: Appends a comma-separated data string to the CSV file using try-except error handling
def insertData(path, data_string):
    try:
        with open(path, mode="a", newline="", encoding="utf-8") as file:
            file.write(data_string + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function: viewData
# Description: Reads and displays the contents of the CSV file using minimal read permissions and try-except error handling
def viewData(path):
    try:
        print(f"The file {path}")
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(",".join(row))
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

# Function: getInput
# Description: Prompts user for inputs, converts data, saves to CSV via insertData, and displays confirmation
def getInput():
    try:
        count = int(input("How many entries are you inputting?\n"))
        for _ in range(count):
            date_str = input("\nEnter a date:\n")
            temp_val = float(input("Enter the highest temp for the inputted date:\n"))
            
            # Convert temperature
            converted_val = convertData(temp_val)
            
            # Format row string: date,original_temp,converted_temp
            formatted_data = f"{date_str},{temp_val},{converted_val}"
            
            # Append data to ZooData.csv using insertData
            insertData(file_path, formatted_data)
            
            # Confirm save with timestamp
            print(f"The following was saved at {datetime.now()} :")
            print(formatted_data)
    except ValueError:
        print("Error: Please enter valid numerical values for entry count and temperature.")

# Main Program Execution & Menu Flow
print(f"{student_id}'s Spreadsheet Automation Menu")

menu_options = {
    "1": "Input Data",
    "2": "View Current Data",
    "3": "Generate Report"
}

print("Choose a number from the following options")
for key, value in menu_options.items():
    print(f"{key} {value}")

choice = input().strip()

# Menu Logic & Routing
if choice == "1":
    print(f"You selected 1 at {datetime.now()}")
    getInput()
elif choice == "2":
    print(f"You selected 2 at {datetime.now()}")
    viewData(file_path)
elif choice == "3":
    print(f"You selected 3 at {datetime.now()}")
    print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected")
