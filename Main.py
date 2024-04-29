import CleanUp
import DataRetrieve
import Logger
from secrets_1 import key

# Pip install requests
import requests

def main():
    
    zip_code = input(f"Please Enter a zipcode... ")
    
    # Check the zip code to see if it is valid
    if CleanUp.zipSanitize(zip_code) == False:
        print(f'Invalid Zipcode')
        Logger.logger.error(f'Invalid Input Detected')
        main()
    else:
        try:
            weather = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={zip_code},US&units=imperial&APPID={key}")
            stuff = weather.json()
            Logger.logger.info(f'API Request Successful')
        except:
            print(f'Something went wrong try again...')
            Logger.logger.error(f'API Request Failed')
            main()
             
        if CleanUp.validate_json(stuff) == False:
            print(f'Bad Data...Try again...')
            Logger.logger.error(f'Data from API was not JSON...BAD DATA')
            main()
        else:
            # Runs if the JSON is not, not empty/ not found
            if stuff["cod"] != "404":
                # print(stuff)
                day2 = DataRetrieve.get_date(8, stuff)
                day3 = DataRetrieve.get_date(16, stuff)
                print(f"The weather for today is " + str(DataRetrieve.get_temp(0, stuff)) + " and " + str(DataRetrieve.get_type(0, stuff)))
                print(f"The weather for " + day2 + " is " + str(DataRetrieve.get_temp(8, stuff)) + " degrees and " + str(DataRetrieve.get_type(8, stuff)))
                print(f"The weather for " + day3 + " is " + str(DataRetrieve.get_temp(16, stuff)) + " degrees and " + str(DataRetrieve.get_type(16, stuff)))
            else:
                print(f'Could not find location try again...')
                Logger.logger.error(f'Trouble reading the JSON file')
                main()
main()
