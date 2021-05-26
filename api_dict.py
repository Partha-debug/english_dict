import  json
import  requests


def get_definations(word, app_id="62729565" ,app_key="936bbea1433d5fcf6bf319bb0c265e56"):
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/en-gb/' + word.lower() + '?fields=definitions&strictMatch=false';
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    json_data = r.text
    loaded_json = json.loads(json_data)
    definations = [i['definitions'][0] for i in loaded_json['results'][0]['lexicalEntries'][0]['entries'][0]['senses']]
    return definations


def print_defination(definations):
    for index, meaning in enumerate(definations, start=1):
        if len(definations) > 1:
            print(f"The word have {len(definations)} meanings.")
            print(f"\n{index} --> {meaning.capitalize()}")
        else:
            print(f"\nIt means {meaning}\n")


def main():
    try:
        word = str(input("Please enter the word: "))
        if word != '':
            definations = get_definations(word)
            print_defination(definations)
        else:
            print("You can't leave the field blank please enter a proper word.")
            main()
    except requests.exceptions.ConnectionError:
        print("Please connect to the internet and try again.")
    except KeyError:
        print("The entered word doesn't exist, please recheck it and try again.")
        main()
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception:
        print("Something went wrong please try again after sometime...")


if __name__ == '__main__':
       
    main()