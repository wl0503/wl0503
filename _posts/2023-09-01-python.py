## emoji printing

from emoji import emojize 

def main():
    message = input("Enter a message: ")
    emoji_message = emojize(message)
    print(emoji_message)

if __name__ == "__main__":
    main()

## retrieving wikipedia information

import wikipedia
from IPython.display import display, Markdown

def retrieve_wikipedia_info():
    terms = ["Python (programming language)", "JavaScript"]
    for term in terms:
        result = wikipedia.search(term)
        summary = wikipedia.summary(result[0])
        print(term)
        display(Markdown(summary))

if __name__ == "__main__":
    retrieve_wikipedia_info()

## Calculating the mean

import sys
from typing import Union

Number = Union[int, float]
Numbers = list[Number]

def calculate_mean(scores: Numbers) -> float:
    sum_scores = sum(scores)
    mean_score = sum_scores / len(scores)
    return round(mean_score, 2)

if __name__ == "__main__":
    single_score = 100
    print(f"Print test data: {single_score}")
    print(f"Mean of single number: {calculate_mean([single_score])}\n")

    test_scores = [90.5, 100, 85.4, 88]
    print(f"Print test data: {test_scores}")
    print(f"Average score: {calculate_mean(test_scores)}")
    print(f"Average score (function method): {calculate_mean(test_scores)}\n")

    bad_data = [100, "NaN", 90]
    print(f"Print test data: {bad_data}")
    print(f"Mean with bad data: {calculate_mean(bad_data)}")
