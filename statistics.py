from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def print_options(data_list):
    """
    Function "print_options" definition
    The function displays on the screen the saved names from the webpage along with their serial numbers.
    """
    for i in range(1, len(data_list) + 1):
        print(str(i) + ".", data_list[i - 1]["name"])


"""Launch Firefox in headless mode."""
options = Options()
options.add_argument("-headless")
browser = webdriver.Firefox(options=options)

"""Saving indicator names and their values from Statistics Estonia's homepage."""
browser.get('https://www.stat.ee/en/avasta-statistikat/main-indicators')
indicators_names = browser.find_elements(By.CLASS_NAME, "indicator-single__title")  # Names
indicators_values = browser.find_elements(By.CLASS_NAME, "indicator-single__value")  # Indicators
indicators_change = browser.find_elements(By.CLASS_NAME, "indicator-single__details")  # Change, since last update


"""Writing data of the indicators to a file."""
with open("Indicators.txt", "w", encoding="UTF-8") as f:
    for name, value, change in zip(indicators_names, indicators_values, indicators_change):
        f.write(f"{name.text};{value.text};{change.text}" + "\n")

browser.close()


"""Reading indicators from the file and adding them line by line to a dictionary without newline characters."""
indicators = []
with open("Indicators.txt") as f:
    for indicator in f:
        data = indicator.strip("\n")
        data = data.split(";")
        indicators.append({"name": data[0], "value": data[1], "change": data[2]})


"""Displaying all saved main indicator names from the webpage with serial numbers to the user."""
print("Which indicator would you like to display? \nOptions:")
print_options(indicators)


"""
Asking the user for an integer, i.e., the serial number of the indicator, and displaying
the desired indicator based on the received response.
"""
choice = input("Enter the serial number (as an integer): ")
while True:
    try:
        choice = int(choice)
        if choice < 1:
            raise IndexError
        elif indicators[choice - 1]["change"]:
            print("According to Statistics Estonia, the", indicators[choice - 1]["name"].lower(), "is",
                  indicators[choice - 1]["value"], "and it has changed", indicators[choice - 1]["change"] + ".")
        else:
            print("According to Statistics Estonia, the", indicators[choice - 1]["name"].lower(), "is",
                  indicators[choice - 1]["value"] + ".")
        choice = input("Enter the serial number (as an integer): ")

    except IndexError:
        choice = input("Please enter a valid serial number: ")

    except ValueError:
        choice = input("Please enter a valid serial number: ")
