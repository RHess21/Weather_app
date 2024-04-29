def get_date(i, stuff):
    return stuff['list'][i]['dt_txt'][0:10]

def get_temp(i, stuff):
    return stuff['list'][i]['main']['temp']

def get_type(i, stuff):
    return stuff['list'][i]['weather'][0]['main']
