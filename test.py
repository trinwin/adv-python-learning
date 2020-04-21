import bs4
import urllib.request
import urllib.parse
import re
import textwrap
"""
Web page script. Web Scraping.

"""


def parse_population_soup(population_soup, country_name):
    """
    Extract the total population for each of these countries
    :param population_soup:
    :param numbers_dict: contains each country
    :return: population_dict
    """
    population = ""
    regex = re.compile(country_name, re.IGNORECASE)
    div = population_soup.find_all("div", {"id": "mw-content-text"})
    tables = div[0].find_all('table')
    all_trs = tables[0].find_all('tr')[1:]

    for current_tr in all_trs:
        tr = current_tr.find("td", {"align": "left"})

        if tr is not None:
            country = tr.find('a').text

            if re.search(regex, country) is not None:
                population = current_tr.find("td", {"style": "text-align:right"}).text

    return population


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
    regex = re.compile(search_term, re.IGNORECASE)

    container = soup.find_all("div", {"id": "covid19-container"})
    table = container[0].find_all('table', {"id": "thetable"})
    # we don't care about the first 3 trs in the list hence [2:]
    all_trs = table[0].find_all('tr')[2:]

    for current_tr in all_trs:
        th_scopes = current_tr.find_all('th', {"scope": "row"})

        if len(th_scopes) == 2:
            # key = name of country
            country_name = th_scopes[1].find('a').text
            if re.search(regex, country_name) is not None:
                relative_url = th_scopes[1].find('a').get('href', None)
                abs_url = urllib.parse.urljoin(base, relative_url)

                paragraph_soup = read_url(abs_url)
                paragraphs = paragraph_soup.find_all("p")
                for paragraph in paragraphs:
                    text = paragraph.text.strip()
                    if text:
                        found_paragraph = paragraph.text.replace("\n", "")
                        break
                cases = current_tr.find_all('td')
                num_of_death = cases[1].text.strip().replace("\n", "")
                num_of_case = cases[0].text.strip().replace("\n", "")
                return country_name, found_paragraph, num_of_case, num_of_death

    return "", "", "", ""


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


def calculate_crude_rate(case_num, death_num, population):
    population = int(population.strip().replace(",", ""))
    case_num = int(case_num.strip().replace(",", ""))
    death_num = int(death_num.strip().replace(",", ""))

    crude_rate = round(case_num / population * 100000, 1)
    crude_death_rate = round(death_num / population * 100000, 1)

    return crude_rate, crude_death_rate


def main():

    file_name, search_term = user_input()

    soup = read_url(
        "https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory")

    country_name, paragraph, case_num, death_num = parse_soup(soup, search_term)

    population_soup = read_url("https://en.wikipedia.org/wiki/List_of_"
                               "countries_and_dependencies_by_population")
    population = parse_population_soup(population_soup, country_name)

    print("\n")

    print("country_name: ", country_name)
    print("population: ", population)
    print("case_num: ", case_num)
    print("death_num: ", death_num)
    print("crude_rate: ", crude_rate)
    print("crude_death_rate: ", crude_death_rate)
    print("paragraph: ", paragraph)

    print("\n")

    # save data
    print("Your data has been saved in the file {}".format(file_name))


if __name__ == '__main__':
    main()
