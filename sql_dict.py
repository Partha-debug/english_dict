from difflib import get_close_matches
from mysql import connector
from mysql.connector.errors import InterfaceError
# import threading

def db_cnct():
    my_db = connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )
    return my_db

def translate(word, database):
    my_db = database
    cursor = my_db.cursor(buffered = True)
    query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()

    if not results:
        query = cursor.execute(f"SELECT Expression FROM Dictionary")
        results = cursor.fetchall()
        words = [str(*i) for i in results]
        match = str(*get_close_matches(word, words, n=1))
        if match:
            conformation = str(input(f"Did you meant {match} instead? y if yes or n if no: ")).lower()
            if conformation == "y":
                return translate(match)
            elif conformation == "n":
                return(f"The word {word} doesn't exist. Please doublecheck it and try again.")
            else:
                return("We didn't understand your entry...")
        else: 
            return f"The word {word} doesn't exist. Please doublecheck it and try again."
    else:
        return(results)

if __name__ == '__main__':
# Challange --> try to multi thread word and my_db
    word = str(input("Enter the word: ")).lower()
    my_db = db_cnct()

    try:
        meaning = translate(word, my_db)
    except InterfaceError:
        print("Please check your network connection and try again!!!")
    except Exception as e:
        print(f"Something went wrong error: {e}")
    
    if type(meaning) == list:
        for index, expression in enumerate(meaning, start=1):
            print(f"{index}. {expression[1]}")
    else:
        print(meaning)
