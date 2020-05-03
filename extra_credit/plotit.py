# ----------------------------------------------------------------------
# Name:        plotit
# Purpose:     Use matplotlib to explore quality of education of world
# ranking university
#
# Author:      Trinh Nguyen
# ----------------------------------------------------------------------
"""
Use matplotlib to explore quality of education of world ranking university
"""
import pandas as pd
import matplotlib.pyplot as plt


def explore_world_raking_university():
    """
    Use matplotlib to explore quality of education of world ranking university
    """
    df_lang = pd.read_csv('cwurData.csv', index_col=0)
    top_lang = df_lang.loc[1:100, "quality_of_education"]
    ax = plt.gca()
    ax.axis([0, 101, 0, 100])
    plt.bar(top_lang.index, top_lang)
    plt.xlabel("World Ranking University")
    plt.ylabel("Quality of Education Ranking")
    plt.title('Quality of Education of World Ranking University')
    plt.show()


def main():
    explore_world_raking_university()


if __name__ == "__main__":
    main()
