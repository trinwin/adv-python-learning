import bs4
import urllib.request
import urllib.parse
import re

"""
Web page script. Web Scraping.  

"""

def parse_population_soup(population_soup, numbers_dict):
    """
    Extract the total population for each of these countries
    :param population_soup:
    :param numbers_dict: contains each country
    :return: population_dict
    """

    # key is country, value is population
    population_dict = {}

    for pair in numbers_dict:
        regex = re.compile(pair, re.IGNORECASE)
        div = population_soup.find_all("div", {"id": "mw-content-text"})
        tables = div[0].find_all('table')
        all_trs = tables[0].find_all('tr')[1:]

        for current_tr in all_trs:
            tr = current_tr.find("td", {"align": "left"})

            if tr is not None:
                country = tr.find('a').text
                if re.search(regex, country) is not None:
                    population = \
                        current_tr.find("td", {"style": "text-align:right"})
                    population_dict[country] = population.text

    return population_dict

def parse_soup(soup, search_term):
    """
    Extract number of cases and number of deaths per country.
    Extract the relevant information for all countries whose
    name contains the search term specified (regardless of case).

    :param soup:
    :param search_term:
    :return: paragraph_dict, numbers_dict
    """

    base = "https://en.wikipedia.org/wiki"
    regex = re.compile(search_term, re.IGNORECASE);
    # key is country , value is corresponding link to first paragraph
    paragraph_dict = {}
    # key is country, value is tuple (nums_of_death, nums_of_cases)
    numbers_dict = {}

    container = soup.find_all("div", {"id": "covid19-container"})
    table = container[0].find_all('table', {"id": "thetable"})
    # we don't care about the first 3 trs in the list hence [2:]
    all_trs = table[0].find_all('tr')[2:]

    for current_tr in all_trs:
        th_scopes = current_tr.find_all('th', {"scope": "row"})

        if len(th_scopes) == 2:
            # key = name of country
            key = th_scopes[1].find('a').text

            if re.search(regex, key) is not None:
                relative_url = th_scopes[1].find('a').get('href', None)
                abs_url = urllib.parse.urljoin(base, relative_url)
                paragraph_dict[key] = abs_url

                #print(key)
                cases = current_tr.find_all('td')
                num_of_deaths = cases[1].text
                num_of_cases = cases[0].text

                value = (num_of_deaths, num_of_cases)
                numbers_dict[key] = value

    return paragraph_dict, numbers_dict

def read_url(url):

    try:
        with urllib.request.urlopen(url) as url_file:
              url_bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    else:
        soup = bs4.BeautifulSoup(url_bytes, 'html.parser')
        return soup

def user_input():

    search_term = input("Please enter a search term: ")
    file = search_term + "summary.txt"
    return file, search_term

def main():

    file_name, search_term = user_input()

    soup = read_url("https://en.wikipedia.org/wiki/2019%E2%80%9320"
                    "_coronavirus_pandemic_by_country_and_territory")

    paragraph_dict, numbers_dict = parse_soup(soup, search_term)

    population_soup = read_url("https://en.wikipedia.org/wiki/List_of_"
                               "countries_and_dependencies_by_population")
    population_dict = parse_population_soup(population_soup, numbers_dict)

    print("\n")
    print(paragraph_dict)
    print(numbers_dict)
    print(population_dict)
    print("\n")

    # save data
    print("Your data has been saved in the file {}".format(file_name))


if __name__ == '__main__':
    main()