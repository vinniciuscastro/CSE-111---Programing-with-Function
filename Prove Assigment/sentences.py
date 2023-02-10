# Vinnicius Castro 
# Feb 1 2023
import random
import datetime
# Create a list of strings and assign
# the list to a variable named words.
words = ["boy", "girl", "cat", "dog", "bird", "house"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
word = random.choice(words)

# This could be any word from any source.
word = "horse"

# Call the capitalize method which will
# capitalize the first letter of the word.
cap_word = word.capitalize()
def main():
    #creativity display the day of the week
    today = datetime.date.today()
    print("Today's date:", today.strftime("%d/%m/%Y"))
    print("Your 6 random sentences:\n")

    #assignment I also add a number so the user will no the sentence number. 
    determiner = get_determiner(1)
    verb = get_verb(1, "past")
    noun = get_noun(1)
    preposition = get_preposition()
    prepositional = get_prepositional_phrase(1)
    print(f"1. {determiner} {noun} {verb} {preposition} {prepositional}.")

    determiner = get_determiner(1)
    verb = get_verb(1, "present")
    noun = get_noun(1)
    preposition = get_preposition()
    prepositional = get_prepositional_phrase(1)
    print(f"2. {determiner} {noun} {verb} {preposition} {prepositional}.")

    determiner = get_determiner(1)
    verb = get_verb(1, "future")
    noun = get_noun(1)
    preposition = get_preposition()
    prepositional = get_prepositional_phrase(1)
    print(f"3. {determiner} {noun} {verb} {preposition} {prepositional}.")

    determiner = get_determiner(2)
    verb = get_verb(2, "past")
    noun = get_noun(2)
    preposition = get_preposition()
    prepositional = get_prepositional_phrase(2)
    print(f"4. {determiner} {noun} {verb} {preposition} {prepositional}.")

    determiner = get_determiner(2)
    verb = get_verb(2, "present")
    noun = get_noun(2)
    preposition = get_preposition()
    prepositional = get_prepositional_phrase(1)
    print(f"5. {determiner} {noun} {verb} {preposition} {prepositional}.")

    determiner = get_determiner(2)
    verb = get_verb(2, "future")
    noun = get_noun(2)
    preposition = get_preposition()
    prepositional = get_prepositional_phrase(1)
    print(f"6. {determiner} {noun} {verb} {preposition} {prepositional}.")

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word.capitalize()

def get_noun(quantity):
        """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
        if quantity == 1:
            words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
            word = random.choice(words)
            return word
        else:
            words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
            word = random.choice(words)
            return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if quantity == 1 and tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
        word = random.choice(words)
        return word
    elif quantity == 1 and tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        word = random.choice(words)
        return word
    elif quantity == 2 and tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
        word = random.choice(words)
        return word
    else:
        words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
        word = random.choice(words)
        return word

def get_preposition():
    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"] 
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    determiner_singular = get_determiner(1)
    noun_singular = get_noun(1)
    noun_plural = get_noun(2)
    determiner_plural =get_determiner(2)
    if quantity == 1:
        words = f"{determiner_singular.lower()} {noun_singular}"
        return words
    else:
        words = f"{determiner_plural.lower()} {noun_plural}"
        return words


if __name__ == "__main__":
    main()
    