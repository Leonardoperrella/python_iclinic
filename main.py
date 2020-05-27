import requests
from calendar import day_name
from datetime import datetime


def get_weekdays_for_unbrella(city_name):
    api_key = 'ff7d5ea19db4e5e6419cdeca8947bace'
    cheked_day = ''
    weekday_list = []
    today = datetime.today().day
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    reponse = requests.get(url)
    if not 200 <= reponse.status_code < 400:
        raise BaseException("Página não encontrada")
    data = reponse.json()
    for d in data['list']:
        current_list_day = datetime.fromtimestamp(d['dt'])
        if not today == current_list_day.day:
            if cheked_day != current_list_day.day and d['main']['humidity'] > 70:
                cheked_day = current_list_day.day
                weekday_list.append(day_name[current_list_day.weekday()])

    str1 = ', '.join(str(e) for e in weekday_list)
    print(f'You should take an umbrella in these days: {str1}')


if __name__ == '__main__':
    get_weekdays_for_unbrella("Ribeirão Preto")