import csv
import os


def getUniqueMonths(yearList):
    unique_list = []
    for x in yearList:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


DataSet = []
csv_data_file = "SingaporeWeather.csv"
with open(csv_data_file, mode='r') as file:
    CsvFile = csv.reader(file)
    lineNumber = 0
    for lines in CsvFile:
        if lineNumber >= 1:
            TimeStamp = lines[1].split()
            Data = {"Date": TimeStamp[0], "Station": lines[2], "Temperature": lines[3], "Humidity": lines[4]}
            DataSet.append(Data)
        lineNumber += 1
input_start_year = int(input("Enter Start Year(YYYY): "))
input_end_year = int(input("Enter End Year(YYYY): "))
input_station_name = str(input("Enter Station Name(Changi,Paya Lebar): "))
found_search_records = []
print("Data is processing please wait...")
start_year = input_start_year
while start_year <= input_end_year:
    all_record_of_that_year = []
    FinalDataSet = []
    for day in DataSet:
        parse_year = int(day["Date"].split("-")[0])
        if parse_year == start_year:
            parse_month = int(day["Date"].split("-")[1])
            all_record_of_that_year.append(parse_month)
            FinalDataSet.append(day)
    unique_list = getUniqueMonths(all_record_of_that_year)
    for month in unique_list :
        list_of_temperature = []
        list_of_humidity = []
        for day in FinalDataSet:
            parse_year = int(day["Date"].split("-")[0])
            parse_month = int(day["Date"].split("-")[1])
            if parse_year == start_year and month == parse_month and day["Station"] == input_station_name:
                list_of_temperature.append((day["Temperature"]))
                list_of_humidity.append(day["Humidity"])
        for day in FinalDataSet:
            parse_year = int(day["Date"].split("-")[0])
            parse_month = int(day["Date"].split("-")[1])
            if parse_year == start_year and month == parse_month and day["Station"] == input_station_name and (day["Humidity"]) == min(list_of_humidity):
                Data1 = {"Date": day["Date"], "Station": input_station_name, "Category": "Max humidity",
                         "Value": day["Humidity"]}
                found_search_records.append(Data1)
            if parse_year == start_year and month == parse_month and day["Station"] == input_station_name and (day["Humidity"]) == max(list_of_humidity):
                Data2 = {"Date": day["Date"], "Station": input_station_name, "Category": "Min humidity",
                         "Value": day["Humidity"]}
                found_search_records.append(Data2)
            if parse_year == start_year and month == parse_month and day["Station"] == input_station_name and (day["Temperature"]) == max(list_of_temperature):
                Data3 = {"Date": day["Date"], "Station": input_station_name, "Category": "Max Temperature",
                         "Value": day["Temperature"]}
                found_search_records.append(Data3)
            if parse_year == start_year and month == parse_month and day["Station"] == input_station_name and (day["Temperature"]) == min(list_of_temperature):
                Data4 = {"Date": day["Date"], "Station": input_station_name, "Category": "Min Temperature",
                         "Value": day["Temperature"]}
                found_search_records.append(Data4)
    start_year += 1
result = []
for i in found_search_records:
    if i not in result:
        result.append(i)
print(result)
ScanResult_columns = ['Date','Station','Category','Value']
ScanResult_file = "ScanResult.csv"
try:
    with open(ScanResult_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=ScanResult_columns)
        writer.writeheader()
        writer.writerows(result)
        print("Search Result are saved in file.")
        os.startfile(ScanResult_file, 'open')
except IOError:
    print("I/O error")




