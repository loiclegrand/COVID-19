from selenium import webdriver
import selenium
from tabulate import tabulate
from termcolor import colored
import datetime as dt
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


table = []
dates = []
y_country_1 = []
y_country_2 = []
y_country_3 = []
y_country_4 = []
y_country_5 = []
y_country_6 = []
y_country_7 = []
y_country_8 = []
y_country_9 = []
y_country_10 = []

driver = ""
now_time = dt.datetime.now()
now = now_time.strftime("%d-%m-%Y")
my_list = []
############################### MAIN PROGRAM ############################################################################
def main_program():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://ncov2019.live/")

    header()
    main_instances()
    country_instances()
    driver.quit()
    my_table()
    calculate_stuff()
    
#########################################################################################################################
def header():
    author = "HYDRAXII"
    version = "BETA"
    print(colored("Made by: " + author + " version: " + version, "blue"), end="\n\n")
    


### MY CLASS ###
class main_element():
    from selenium import webdriver

    def __init__(self, xpath, name):
        self.xpath = xpath
        self.name = name
        self.cases = 0
        self.percentage = 0 
        self.rounded_percentage = 0
        self.total_cases = driver.find_element_by_xpath("/html/body/div/div/div[1]/div/p[4]").text.replace(",", "")
        self.countryxpath = ""
        self.list = []
        self.make_list = []

    # get country xpath 
    def get_country_xpath_name(self, countryxpath):
        self.countryxpath = driver.find_element_by_xpath(countryxpath).text
    
    def my_country_function(self):
        global table
        self.cases = driver.find_element_by_xpath(self.xpath).text
        if "\n" in self.cases:
            self.cases = self.cases[:self.cases.find("\n")].replace(",", " ")
        else:
            self.cases = self.cases.replace(",", " ")

        # get country percentage
        self.percentage = int(self.cases.replace(" ", "")) / int(self.total_cases.replace(" ", "")) * 100
        self.rounded_percentage = round(self.percentage, 2)

        # add to list
        self.list.append(self.name)
        self.list.append(self.countryxpath)
        self.list.append(self.cases)
        self.list.append(str(self.rounded_percentage) + "%")
        table.append(self.list)
    

        # add to dict
        self.make_list.append(now)
        self.make_list.append(self.countryxpath)
        self.make_list.append(self.cases)
        my_list.append(self.make_list)
        

     # get the x path and only parse the text out of it
    def get_xpath_cases(self):
        self.cases = driver.find_element_by_xpath(self.xpath).text.replace(",", " ")
        print(self.name + ": " + self.cases, end= "  ")
    # get the percentages out of the numbers
    def get_percentages(self):
        self.percentage = int(self.cases.replace(" ", "")) / int(self.total_cases.replace(" ", "")) * 100
        if self.percentage == 100:
            print()
        else:
            rounded_percentage = round(self.percentage, 2)
            print(str(rounded_percentage) + "%")

def main_instances():
    #! main cases !#
    #confirmed cases 
    confirmed = main_element("/html/body/div/div/div[1]/div/p[4]", "Total confirmed cases")
    confirmed.get_xpath_cases()
    confirmed.get_percentages()

    # deceased cases
    deceased = main_element("/html/body/div/div/div[1]/div/p[6]", "Total deceases cases")
    deceased.get_xpath_cases()
    deceased.get_percentages()

    # serious cases
    serious = main_element("/html/body/div/div/div[1]/div/p[8]", "Total serious cases")
    serious.get_xpath_cases()
    serious.get_percentages()

    # recovered cases
    recovered = main_element("/html/body/div/div/div[1]/div/p[10]", "total recovered")
    recovered.get_xpath_cases()
    recovered.get_percentages()

def country_instances():
    global dates
    global y_country_1
    #! make instances of countries !#
    country_1 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[2]/td[3]', "1.")
    country_1.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[2]/td[2]')

    country_2 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[3]/td[3]', "2.")
    country_2.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[3]/td[2]')

    country_3 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[4]/td[3]', "3.")
    country_3.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[4]/td[2]')

    country_4 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[5]/td[3]', "4.")
    country_4.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[5]/td[2]')

    country_5 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[6]/td[3]', "5.")
    country_5.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[6]/td[2]')

    country_6 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[7]/td[3]', "6.")
    country_6.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[7]/td[2]')

    country_5 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[6]/td[3]', "5.")
    country_5.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[6]/td[2]')

    country_6 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[7]/td[3]', "6.")
    country_6.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[7]/td[2]')

    country_7 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[8]/td[3]', "7.")
    country_7.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[8]/td[2]')

    country_8 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[9]/td[3]', "8.")
    country_8.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[9]/td[2]')

    country_9 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[10]/td[3]', "9.")
    country_9.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[10]/td[2]')

    country_10 = main_element('//*[@id="sortable_table_mobile_Global"]/tbody/tr[11]/td[3]', "10.")
    country_10.get_country_xpath_name('//*[@id="sortable_table_mobile_Global"]/tbody/tr[11]/td[2]')

    # executes the my_country_function on all instances below
    country_list = [country_1, country_2, country_3, country_4, country_5, country_6, country_7, country_8, country_9, country_10]
    for country in country_list:
        country.my_country_function()



    #! open the CSV, if the date of today isn't in the file write todays output to it
    filename = "CSV.csv"
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        date_in_file = False

        for line in csv_reader:
            if line["Date"] == now:
                date_in_file = True
            
    if date_in_file == False:
        with open(filename, "a", newline='') as csv_file:
                fieldnames = ["Date", "Country", "Cases"]
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(my_list)

    # reopens the file to read the "new file" and append date to lists
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)        

        for line in csv_reader:
            #country 1
            if line["Country"] == country_1.countryxpath:
                y_country_1.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 2
            elif line["Country"] == country_2.countryxpath:
                y_country_2.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 3
            elif line["Country"] == country_3.countryxpath:
                y_country_3.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 4
            elif line["Country"] == country_4.countryxpath:
                y_country_4.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 5
            elif line["Country"] == country_5.countryxpath:
                y_country_5.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 6
            elif line["Country"] == country_6.countryxpath:
                y_country_6.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 7
            elif line["Country"] == country_7.countryxpath:
                y_country_7.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 8
            elif line["Country"] == country_8.countryxpath:
                y_country_8.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 9
            elif line["Country"] == country_9.countryxpath:
                y_country_9.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])
            # country 10
            elif line["Country"] == country_10.countryxpath:
                y_country_10.append(line["Cases"])
                if line["Date"] not in dates:
                    dates.append(line["Date"])

    x = [dt.datetime.strptime(d, "%d-%m-%Y").date() for d in dates]

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(x, y_country_1, label=country_1.countryxpath)
    plt.plot(x, y_country_2, label=country_2.countryxpath)
    plt.plot(x, y_country_3, label=country_3.countryxpath)
    plt.plot(x, y_country_4, label=country_4.countryxpath)
    plt.plot(x, y_country_5, label=country_5.countryxpath)
    plt.plot(x, y_country_6, label=country_6.countryxpath)
    plt.plot(x, y_country_7, label=country_7.countryxpath)
    plt.plot(x, y_country_8, label=country_8.countryxpath)
    plt.plot(x, y_country_9, label=country_9.countryxpath)
    plt.plot(x, y_country_10, label=country_10.countryxpath)
    plt.title("COVID-19 cases")
    plt.xlabel("Days")
    plt.ylabel("Number of cases")
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()

def my_table():
    #print the output in a table
    print()
    print(tabulate(table, headers=["NR.", "Country", "Total cases", "Percentage"]))

def calculate_stuff():
    return

main_program()   