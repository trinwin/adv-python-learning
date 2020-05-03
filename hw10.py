import pandas as pd

def q1(df):
    """
    How many cars are made by the division Audi?
    The function must return an integer.
    :param df: Pandas DataFrame representing the yelp data
    :return:
    """
    return len(df.loc[df["Division"].str.contains("Audi", na= False)])

def q2(df):
    """
    How many divisions does the manufacturer General Motors have?
    The function must return an integer.
    :param df: Pandas DataFrame representing the yelp data
    :return: 
    """""

def q3(df):
    """
    Which manufacturer makes the most guzzlers
    (as indicated by the column 'Guzzler?').
    :param df: Pandas DataFrame representing the yelp data
    :return: String - manufacturer that makes the most guzzlers
    """
    return df[['Mfr Name', 'Guzzler?']].groupby(['Mfr Name'])\
        .agg(['count']).idxmax().iloc[0]


def q4(df):
    """
    What is the value of the highest combined Fuel Efficiency as given
    by "Comb FE (Guide) - Conventional Fuel"?
    :param df: Pandas DataFrame representing the yelp data
    :return: Float -  highest combined Fuel Efficiency
    """
    return df['Comb FE (Guide) - Conventional Fuel'].max()

def q5(df):
    """
    Which division and car line has the lowest combined FE - Conventional Fuel?
    :param df: Pandas DataFrame representing the yelp data
    :return: Tuple - ( division, carline )
    """
    carline = df['Comb FE (Guide) - Conventional Fuel'].idxmin()
    division = df.loc[carline, 'Division']
    return division, carline

def q6(df):
    """
    What is the average combined FE - Conventional Fuel among all wheel drives.
    Use 'Drive Desc'.
    :param df: Pandas DataFrame representing the yelp data
    :return: Float - average combined FE - Conventional Fuel among all AWDs
    """

    all_wheel_drive = df.loc[df['Drive Desc'].str.contains("All Wheel Drive",
                                                           na=False)]
    combined_fe = all_wheel_drive['Comb FE (Guide) - Conventional Fuel']
    fuel_awd = [fuel for fuel in combined_fe]
    return sum(fuel_awd)/len(fuel_awd)

def q7(df):
    """
    Which car line has the largest difference between Highway and City Fuel
    efficiency - Conventional Fuel?
    :param df: Pandas DataFrame representing the yelp data
    :return: String - Carline with largest highway/city fuel difference
    """
    city = df['City FE (Guide) - Conventional Fuel']
    highway = df['Hwy FE (Guide) - Conventional Fuel']
    return highway.subtract(city, fill_value=0).idxmax()

def q11_mandeep(df):
    """
    My criteria to buy a car is best Fuel Economy.
    :param df: Pandas DataFrame representing the yelp data
    :return: String - best econ friendly car
    """
    return df['Comb FE (Guide) - Conventional Fuel'].idxmax()



def main():
    df_guide = pd.read_csv('2020 FE Guide.csv', index_col='Carline')
    print(f'Q1: {q1(df_guide)}')
    print(f'Q3: {q3(df_guide)}')
    print(f'Q4: {q4(df_guide)}')
    print(f'Q5: {q5(df_guide)}')
    print(f'Q6: {q6(df_guide)}')
    print(f'Q7: {q7(df_guide)}')
    print(f'Mandeep\'s car: {q11_mandeep(df_guide)}')


if __name__ == "__main__":
    main()