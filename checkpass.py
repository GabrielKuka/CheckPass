import requests
from pwinput import pwinput
from helper import error, success, hash, ENDPOINT


def get_pw_freq(suffix, result):
    if not (suffix and result):
        return 0
    try:
        result = int(list(filter(lambda x: x.startswith(suffix), result))[0].split(':')[1])
    except Exception as e:
        print(error(f"Error: {e}"))
        return 0
    else:
        return result

if __name__ == '__main__':

    pw = pwinput("Enter password: ", mask='*')

    prefix, suffix = hash(pw)

    r = requests.get(f'{ENDPOINT}/{prefix}')

    if r.status_code != 200:
        print(error(f"Request Error. Status code: {r.status_code}"))
        exit()

    is_present = suffix in r.text
    if is_present:
        freq = get_pw_freq(suffix, r.text.splitlines()) 
        print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+\n")

        print(error(f"\tThere {'was' if freq==1 else 'were' } {freq:,} occurrence{'s' if freq > 1 else ''} of your password online!"))

        print(error("\tChange your password for safer measures.\n"))

        print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")
    else:
        print(success("Your password has not been leaked."))

    print(success("Bye!"))


