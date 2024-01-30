from datetime import date, timedelta, datetime
import datetime

import requests

index = 0


def main():
    key = "536c75445ddd436e3bdf96e3bf10f152"
    zip_code = int(input("Please Enter a zipcode... "))
    if len(str(zip_code)) != 5:
        print('Invalid Zipcode')
        main()
    else:
        weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={zip_code},US&units=imperial&APPID={key}")
        stuff = weather.json()
        if stuff["cod"] != "404":
            print(stuff)
            # current_temp = stuff['list'][index]['main']['temp']
            # current_date = stuff['list'][index]['dt_txt']
            # current_date = current_date[0:10]

            # highest = get_high(current_date, stuff, index)
            # lowest = get_low(current_date, stuff, index)

            #day2 = str(datetime.now().date() + timedelta(days=1))
            #day3 = str(datetime.now().date() + timedelta(days=2))

            day2 = stuff['list'][8]['dt_txt'][0:10]
            day3 = stuff['list'][16]['dt_txt'][0:10]
            print("The weather for today is " + str(get_temp(0, stuff)) + " and " + str(get_type(0, stuff)))
            print("The weather for " + day2 + " is " + str(get_temp(8, stuff)) + " degrees and " + str(get_type(8, stuff)))
            print("The weather for " + day3 + " is " + str(get_temp(16, stuff)) + " degrees and " + str(get_type(16, stuff)))
        else:
            print('Could not find location try again...')
            main()


def get_temp(i, stuff):
    return stuff['list'][i]['main']['temp']

def get_type(i, stuff):
    return stuff['list'][i]['weather'][0]['main']

def get_high(day, stuff, i):
    highest = -10000
    while day == stuff['list'][i]['dt_txt'][0:10]:

        high = stuff['list'][i]['main']['temp_max']
        if high >= highest:
            highest = high
        i += 1
    return highest


def get_low(day, stuff, i):
    lowest = 10000
    while day == stuff['list'][i]['dt_txt'][0:10]:

        low = stuff['list'][i]['main']['temp_min']
        if low <= lowest:
            lowest = low
        i += 1
    return lowest


main()
