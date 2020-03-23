from selenium import webdriver
import selenium
from tabulate import tabulate
import re
from termcolor import colored

### GLOBAL VARIABLES ###

###! QUICK FACTS ###
total_confirmed_cases = ""
total_death_cases = ""
total_serious_cases = ""
total_recovered_cases = ""

# INTEGERS
int_total_confirmed_cases = 0
int_total_death_cases = 0
int_total_serious_cases = 0
int_total_recovered_cases = 0

# Precentages
total_death_percentage = 0
total_serious_percentage = 0
total_recovered_percentage = 0

###! COUNTRIES ###

# CHINA
total_china = 0
number_china = 0
china_percentage = 0 

# ITALY
total_italy = 0
number_italy = 0

# SPAIN
total_spain = 0
number_spain = 0 

#country 1
country_1 = ""
country_1_number_text = ""
country_1_number = 0
country_1_percentage = 0

# country 2
country_2 = ""
country_2_number_text = ""
country_2_number = 0
country_2_percentage = 0

#country 3
country_3 = ""
country_3_number_text = ""
country_3_number = 0
country_3_percentage = 0

#country 4
country_4 = ""
country_4_number_text = ""
country_4_number = 0
country_4_percentage = 0

#country 5
country_5 = ""
country_5_number_text = ""
country_5_number = 0
country_5_percentage = 0

#country 6
country_6 = ""
country_6_number_text = ""
country_6_number = 0
country_6_percentage = 0

#country 7
country_7 = ""
country_7_number_text = ""
country_7_number = 0
country_7_percentage = 0

#country 8
country_8 = ""
country_8_number_text = ""
country_8_number = 0
country_8_percentage = 0
#country 9
country_9 = ""
country_9_number_text = ""
country_9_number = 0
country_9_percentage = 0

#country 10
country_10 = ""
country_10_number_text = ""
country_10_number = 0
country_10_percentage = 0



    # start Google Chrome
driver = webdriver.Chrome()


### MAIN PROGRAM ####################################################################################################
def main_program():

    # program header
    header()

    # Go to this URL
    driver.get("https://ncov2019.live/")

    # find text elements
    find_text_elements()

    # prints out the text
    print_main_cases()


    # percentage calculations 
    calculate_main_percentages()
    
    # print percentages
    print_main_percentages()

    # prints countries cases
    get_countries_number()

    # calculate countries percentages
    calculate_countries_percentages()



    # print countries percentages
    print_countries_output()

    # quit the browser
    driver.quit()
#########################################################################################################################

# the application header
def header():
    author = "HYDRAXII"
    version = 1.0

    print(colored("Author: " + author + "  " + "Version: " + str(version) + "\n" + "\n", "cyan"))



    return

def find_text_elements():

    ##################! QUICK FACTS ###################
    # Find the text of this specific X-path
    global total_confirmed_cases
    global total_death_cases
    global total_serious_cases
    global total_recovered_cases

    # the number of total confirmed cases
    total_confirmed_cases = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/p[4]").text

    # the number of total deaths
    total_death_cases = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/p[6]").text
    
    # the number of serious cases
    total_serious_cases = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/p[8]").text
    
    # the number of serious cases
    total_recovered_cases = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/p[10]").text

    #################! COUNTRIES #####################

    global total_china
    global total_italy
    global total_spain
    global country_1
    global country_1_number_text
    global country_2
    global country_2_number_text
    global country_3
    global country_3_number_text
    global country_4
    global country_4_number_text
    global country_5
    global country_5_number_text
    global country_6
    global country_6_number_text
    global country_7
    global country_7_number_text
    global country_8
    global country_8_number_text
    global country_9
    global country_9_number_text
    global country_10
    global country_10_number_text
    ###! FIND TEXT ELEMENT FOR NAMES AND NUMBERS+ 

    # country 1
    country_1 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[2]/td[1]').text
    country_1_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[2]/td[2]').text
    # country 2
    country_2 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[3]/td[1]').text
    country_2_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[3]/td[2]').text
    # country 3
    country_3 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[4]/td[1]').text
    country_3_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[4]/td[2]').text
    #country 4
    country_4 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[5]/td[1]').text
    country_4_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[5]/td[2]').text
    # country 5
    country_5 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[6]/td[1]').text
    country_5_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[6]/td[2]').text
    # country 6
    country_6 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[7]/td[1]').text
    country_6_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[7]/td[2]').text
    # country 7
    country_7 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[8]/td[1]').text
    country_7_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[8]/td[2]').text
    #country 8
    country_8 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[9]/td[1]').text
    country_8_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[9]/td[2]').text
    #country 9
    country_9 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[10]/td[1]').text
    country_9_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[10]/td[2]').text
    #country 10
    country_10 = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[11]/td[1]').text
    country_10_number_text = driver.find_element_by_xpath('//*[@id="sortable_table_mobile_Global"]/tbody/tr[11]/td[2]').text
    return






# print the results
def print_main_cases():
    ###! print QUICK FACTS ###
    print("Total confirmed cases: " + colored(total_confirmed_cases, "yellow"))
    print("Total death cases: " + colored(total_death_cases, "red"))
    print("Total serious cases: " + colored(total_serious_cases, "yellow"))
    print("Total recovered cases: " + colored(total_recovered_cases, "green") + "\n")

    

def get_countries_number():

        ###! COUNTRIES ###
    # country 1
    global country_1_number
    if "(" in country_1_number_text:
        country_1_number = country_1_number_text[:country_1_number_text.find("(") -1]
    else:
        country_1_number = country_1_number_text

    # country 2
    global country_2_number
    if "(" in country_2_number_text:
        country_2_number = country_2_number_text[:country_2_number_text.find("(") -1]
    else:
        country_2_number = country_2_number_text

    # country 3
    global country_3_number
    if "(" in country_3_number_text:
        country_3_number = country_3_number_text[:country_3_number_text.find("(") -1]
    else:
        country_3_number = country_3_number_text

    # country 4
    global country_4_number
    if "(" in country_4_number_text:
        country_4_number = country_4_number_text[:country_4_number_text.find("(") -1]
 
    else:
        country_4_number = country_4_number_text
 
    # country 5
    global country_5_number
    if "(" in country_5_number_text:
        country_5_number = country_5_number_text[:country_5_number_text.find("(") -1]
 
    else:
        country_5_number = country_5_number_text
 
    # country 6
    global country_6_number
    if "(" in country_6_number_text:
        country_6_number = country_6_number_text[:country_6_number_text.find("(") -1]
    else:
        country_6_number = country_6_number_text

    # country 7
    global country_7_number
    if "(" in country_7_number_text:
        country_7_number = country_7_number_text[:country_7_number_text.find("(") -1]
    else:
        country_7_number = country_7_number_text

    # country 8
    global country_8_number
    if "(" in country_8_number_text:
        country_8_number = country_8_number_text[:country_8_number_text.find("(") -1]
 
    else:
        country_8_number = country_8_number_text

    # country 9
    global country_9_number
    if "(" in country_9_number_text:
        country_9_number = country_9_number_text[:country_9_number_text.find("(") -1]
    else:
        country_9_number = country_9_number_text

    # country 10
    global country_10_number
    if "(" in country_10_number_text:
        country_10_number = country_10_number_text[:country_10_number_text.find("(") -1]
 
    else:
        country_10_number = country_10_number_text


    

    return

def calculate_main_percentages():

    global total_death_percentage
    global total_serious_percentage
    global total_recovered_percentage

    # percentage of death rate
    total_death_percentage = int(total_death_cases.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100
    
    # percentage of serious cases
    total_serious_percentage = int(total_serious_cases.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100

    # percentage of recover rate
    total_recovered_percentage = int(total_recovered_cases.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100
    return


def calculate_countries_percentages():

    # country 1
    global country_1_percentage
    country_1_percentage = int(country_1_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100

    # country 2
    global country_2_percentage
    country_2_percentage = int(country_2_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100
    
    # country 3
    global country_3_percentage
    country_3_percentage = int(country_3_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100

    # country 4
    global country_4_percentage
    country_4_percentage = int(country_4_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100
    
        # country 5
    global country_5_percentage
    country_5_percentage = int(country_5_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100

    # country 6
    global country_6_percentage
    country_6_percentage = int(country_6_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100
    
    # country 7
    global country_7_percentage
    country_7_percentage = int(country_7_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100

    # country 8
    global country_8_percentage
    country_8_percentage = int(country_8_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100

    # country 9
    global country_9_percentage
    country_9_percentage = int(country_9_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100

    # country 10
    global country_10_percentage
    country_10_percentage = int(country_10_number.replace(",", "")) / int(total_confirmed_cases.replace(",", "")) * 100
    return



def print_main_percentages():

    # print death rates
    print("The death rate is " + colored(str(round(total_death_percentage, 2)) + "%", "red"))

    # print serious cases rates
    print("The serious cases rate " + colored(str(round(total_serious_percentage, 2)) + "%", "yellow"))

    # print recover rates
    print("The recover rate is " + colored(str(round(total_recovered_percentage, 2)) + "%", "green"))

    # 2 empty lines at the end
    print("\n")

    return


def print_countries_output():
    print()

    table = [["1", country_1, country_1_number, str(round(country_1_percentage, 2))],
             ["2", country_2, country_2_number, str(round(country_2_percentage, 2))],
             ["3", country_3, country_3_number, str(round(country_3_percentage, 2))],
             ["4", country_4, country_4_number, str(round(country_4_percentage, 2))],
             ["5", country_5, country_5_number, str(round(country_5_percentage, 2))],
             ["6", country_6, country_6_number, str(round(country_6_percentage, 2))],
             ["7", country_7, country_7_number, str(round(country_7_percentage, 2))],
             ["8", country_8, country_8_number, str(round(country_8_percentage, 2))],
             ["9", country_9, country_9_number, str(round(country_9_percentage, 2))],
             ["10", country_10, country_10_number, str(round(country_10_percentage, 2))]]
             
    print(tabulate(table,headers=["NR.", "Country", "Total cases", "Total %"]))



def write_to_file():
    return

main_program()
