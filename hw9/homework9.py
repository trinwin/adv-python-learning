# ----------------------------------------------------------------------
# Name:        homework9
# Purpose:     Implement a program that systematically compiles COVID-19
#              information from multiple web pages and saves that
#              information in a text file on the user's computer.
#
# Author(s):   Mandeep Pabla & Trinh Nguyen
# ----------------------------------------------------------------------

"""
Web page script. Web Scraping.

"""
import bs4
import urllib.request
import urllib.parse
import re
import textwrap


def parse_population_soup(country_name, population_soup):
    """
    Extract the total population for a country
    :param country_name (string): name of the country
    :param population_soup (soup object):  has population info
    :return population (string): population of the given country
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
                population = current_tr.find("td", {
                    "style": "text-align:right"}).text
                return population.strip().replace("\n", "")
    return population


def parse_paragraph_soup(abs_url):
    """
    Extract the first non-empty paragraph of the page
    :param abs_url (string): url of the page
    :return paragraph (string): non-empty paragraph
    """
    found_paragraph = ""
    paragraph_soup = read_url(abs_url)
    paragraphs = paragraph_soup.find_all("p")
    for paragraph in paragraphs:
        text = paragraph.text.strip()
        if text:
            found_paragraph = paragraph.text.replace("\n", "")
            return found_paragraph
    return found_paragraph


def calculate_crude_rate(case_num, death_num, population):
    """
    Calculate the crude rate for cases and death of a country per 100000
    :param case_num (string): number of cases
    :param death_num (string): number of deaths
    :param population (string): population
    :return: crude_rate  (string): crude rate of cases
    :return: crude_death_rate (string): crude rate of deaths
    """
    population = int(population.strip().replace(",", ""))
    case_num = int(case_num.strip().replace(",", ""))
    death_num = int(death_num.strip().replace(",", ""))

    crude_rate = str(round(case_num / population * 100000, 1))
    crude_death_rate = str(round(death_num / population * 100000, 1))

    return crude_rate, crude_death_rate


def parse_soup(soup, population_soup, search_term):
    """
    Extract number of cases and number of deaths per country.
    Extract the relevant information for all countries whose
    name contains the search term specified (regardless of case).
    :param soup (soup object): soup object to extract covid19 stats
    :param population_soup (soup object): had population stats
    :param search_term (string): search term user entered
    :return: covid19_stats (dict): dictionary of covid19 stat of all
            countries that match the search term (key = country name,
            value = list of stats)
    """

    base = "https://en.wikipedia.org/wiki"
    regex = re.compile(search_term, re.IGNORECASE)
    # key is country, value is list contains all required info
    covid19_stats = {}

    container = soup.find_all("div", {"id": "covid19-container"})
    table = container[0].find_all('table', {"id": "thetable"})
    all_trs = table[0].find_all('tr')[2:]

    for current_tr in all_trs:
        th_scopes = current_tr.find_all('th', {"scope": "row"})

        if len(th_scopes) == 2:
            # key = name of country
            key = th_scopes[1].find('a').text

            if re.search(regex, key) is not None:
                relative_url = th_scopes[1].find('a').get('href', None)
                abs_url = urllib.parse.urljoin(base, relative_url)
                # extract first empty paragraph
                paragraph = parse_paragraph_soup(abs_url)
                # extract population info
                population = parse_population_soup(key, population_soup)
                cases = current_tr.find_all('td')
                # extract number of cases and deaths
                case_num = cases[0].text.strip().replace("\n", "")
                death_num = cases[1].text.strip().replace("\n", "")
                # calculate crude rate for cases and deaths
                crude_rate, crude_death_rate = calculate_crude_rate(
                    case_num, death_num, population)
                info = [population, case_num, death_num, crude_rate,
                        crude_death_rate, paragraph]
                covid19_stats[key] = info
    return covid19_stats


def read_url(url):
    """
    Open the url and parse HTML document
    :param url (string): url used to be parsed
    :return soup: Soup object of the URL
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            url_bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    else:
        soup = bs4.BeautifulSoup(url_bytes, 'html.parser')
        return soup


def user_input():
    """
    Format user input and create output file name
    :return file (string): file name
    :return search_term (string): search_term
    """
    search_term = input("Please enter a search term: ").strip()
    file = search_term + "summary.txt"
    return file, search_term


def write_to_file(file_name, covid19_stats):
    """
    Write info to file
    :param file_name (string): name of file
    :param covid19_stats (dict): information to write to file
    :return: None
    """
    f = open(file_name, "w")
    for country_name, stats in covid19_stats.items():
        f.write('Country: {}\n'.format(country_name))
        f.write('Population:{:>30}\n'.format(stats[0]))
        f.write('Total Confirmed Cases:{:>19}\n'.format(stats[1]))
        f.write('Total Deaths:{:>28}\n'.format(stats[2]))
        f.write('Cases per 100,000 people:{:>18}\n'.format(stats[3]))
        f.write('Deaths per 100,000 people:{:>17}\n'.format(stats[4]))
        f.write('{}\n\n\n'.format(textwrap.fill(stats[5], 72)))
    f.close()
    print("Your data has been saved in the file {}".format(file_name))


def main():
    file_name, search_term = user_input()

    soup = read_url("https://en.wikipedia.org/wiki/2019%E2%80%9320"
                    "_coronavirus_pandemic_by_country_and_territory")

    population_soup = read_url("https://en.wikipedia.org/wiki/List_of_"
                               "countries_and_dependencies_by_population")

    # Extract covid19 stat for country that matches the search term
    covid19_stats = parse_soup(soup, population_soup, search_term)
    # Write the info to file
    write_to_file(file_name, covid19_stats)


if __name__ == '__main__':
    main()
