import bs4
import requests
import collections

# Define a named tuple to store the weather data to make it easier to return
WeatherReport = collections.namedtuple('Measurement', 'condition, temperature, scale, location')

# TODO Print header
# TODO prompt for location
# TODO Get weather from weather underground as HTML using response
# TODO parse weather details to produce an output using BS4
# TODO Display the weather details


def main():
    display_header()
    my_loc = get_location()
    web_content = get_html_from_web(my_loc)
    if web_content == 'False':
        print('Not a known zip code')
        raise SystemExit

    report = parse_web_content(web_content)
    # Display the forecast
    print('The temp in {} is {} {} and {}'.format(
        report.location,
        report.temperature,
        report.scale,
        report.condition
    ))


def display_header():
    print('------------------------------')
    print('     Weather Client App')
    print('Sadly this only works for USA ZIP codes')
    print('------------------------------')
    print()


def get_location():
    location = input('Enter your zip code (e.g. 97201):')
    return location


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/us/or/portland/{}'.format(zipcode)
    response = requests.get(url)
    # A check on the url, if a valid response is received then proceed otherwise exit
    if response.status_code == 200:
        return response.text
    else:
        return 'False'


def parse_web_content(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temperature = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    # Do some clean up and break apart the location string
    location = cleanup_text(location)
    location = find_city_and_state_from_location(location)
    condition = cleanup_text(condition)
    temperature = cleanup_text(temperature)
    scale = cleanup_text(scale)

    report = WeatherReport(location=location, condition=condition, temperature=temperature, scale=scale)
    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
