# ----------------------------------------------------------------------
# Name:        songstats
# Purpose:     Demonstrate the use of dictionaries
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------
"""
Generate some statistics on the words of the Beatles song 'Yesterday'.

Print all the words found in the song alphabetically
followed by the number of times they appear in the song.
Print all the words found in the song in descending order of frequency.
Print the longest word found in the song.
Print the number of distinct words in the song.
Print the number of total words in the song.
"""
import string

YESTERDAY = '''
            Yesterday, all my troubles seemed so far away
            Now it looks as though they're here to stay
            Oh, I believe in yesterday
            Suddenly, I'm not half the man I used to be
            There's a shadow hanging over me.
            Oh, yesterday came suddenly
            Why she had to go I don't know she wouldn't say
            I said something wrong, now I long for yesterday
            Yesterday, love was such an easy game to play
            Now I need a place to hide away
            Oh, I believe in yesterday
            Why she had to go I don't know she wouldn't say
            I said something wrong, now I long for yesterday
            Yesterday, love was such an easy game to play
            Now I need a place to hide away
            Oh, I believe in yesterday
            '''


def count_words(song):
    """
    Count the words in the song specified ignoring capitalization and
    leading and trailing punctuation.
    :param song: string - song lyrics
    :return: a tally dictionary with items of the form word: count
    """
    tally = {}  # Initialize the dictionary
    lower_song = song.lower()  # Convert to lowercase
    words = lower_song.split()  # Split into a list of words
    for each_word in words:
        # Take out leading and trailing punctuation characters
        each_word = each_word.strip(string.punctuation)
        tally[each_word] = tally.get(each_word, 0) + 1
    return tally


def report(word_count):
    """
    Print some statistics based on the given dictionary
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    # Your code here
    return {word for word in word_count if word_count[word] >= 5}


def main():
    occurrences = count_words(YESTERDAY)
    # print(report(occurrences))

    temperature = {'SJ': 92, 'MT': 89, 'SF': 75, 'F': 91}
    description = {city: 'hot' if temperature[city] >= 90 else 'ok' for city in
                   temperature}
    print(description)
if __name__ == '__main__':
    main()
