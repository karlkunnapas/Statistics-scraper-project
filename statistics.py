from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def print_options():
    """
    Function "print_options" definition
    The function displays on the screen the saved names from the webpage along with their serial numbers.
    """
    for i in range(1, 19):
        print(str(i) + ".", indicator_names[i - 1])


"""Launch Firefox in headless mode."""
options = Options()
options.add_argument("-headless")
browser = webdriver.Firefox(options=options)

"""Saving indicator names and their values from Statistics Estonia's homepage."""
browser.get('https://www.stat.ee/en/avasta-statistikat/main-indicators')
webpage_names = browser.find_elements(By.CLASS_NAME, "button__label")  # Names
webpage_indicators = browser.find_elements(By.CLASS_NAME, "indicator-single__value")  # Indicators
time_updated = browser.find_elements(By.CLASS_NAME, "indicator-single__bottom__date")  # Time, when it was updated
indicators_change = browser.find_elements(By.CLASS_NAME, "indicator-single__details")  # Change, since last update


"""Writing the numerical values of indicators to a file."""
with open("Indicators.txt", "w", encoding="UTF-8") as f:
    for indicator, indicator_change in zip(webpage_indicators, indicators_change):
        f.write(f"{indicator.text};{indicator_change.text}" + "\n")

with open("Indicators_change.txt", "w", encoding="UTF-8") as f:
    for indicator_change in indicators_change:
        f.write(indicator_change.text + "\n")

"""Adding indicator names to a list."""
indicator_names = []
for name in webpage_names:
    indicator_names.append(name.text)

browser.close()


"""Reading indicators from the file and adding them line by line to a list without newline characters."""
indicators = []
with open("Indicators.txt") as f:
    for indicator in f:
        data = indicator.strip("\n")
        indicators.append(data.split(";"))

indicators_change = []
with open("Indicators_change.txt") as f:
    for indicator_change in f:
        indicators_change.append(indicator_change.strip("\n"))

"""Displaying all saved main indicator names from the webpage with serial numbers to the user."""
print("Which indicator would you like to display? \nOptions:")
print_options()

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
        elif indicators_change[choice - 1]:
            print("According to Statistics Estonia, the", indicator_names[choice - 1].lower(), "is",
                  indicators[choice - 1][0], "and it has changed", indicators[choice - 1][1] + ".")
            choice = input("Enter the serial number (as an integer): ")
        else:
            print("According to Statistics Estonia, the", indicator_names[choice - 1].lower(), "is",
                  indicators[choice - 1][0] + ".")

    except IndexError:
        choice = input("Please enter a valid serial number: ")

    except ValueError:
        choice = input("Please enter a valid serial number: ")
