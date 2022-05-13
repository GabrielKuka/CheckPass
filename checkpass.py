import hashlib, requests, sys
from colorama import Fore, Style


def hash(value):
    if not value: return []

    digest = hashlib.sha1(bytes(f'{value}', encoding='utf-8')).hexdigest()

    prefix = digest[:5].upper()
    suffix = digest[5:].upper()

    return (prefix, suffix)

def danger(msg):
    print(f"{Fore.RED}[!] {msg}{Style.RESET_ALL}")

def get_pw_freq(suffix, result):
    if not (suffix and result):
        return 0
    try:
        result = int(list(filter(lambda x: x.startswith(suffix), result))[0].split(':')[1])
    except Exception as e:
        danger(f"Error: {e}")
        return 0
    else:
        return result

if __name__ == '__main__':

    if len(sys.argv) < 2:
        danger("Usage: checkpass [PASSWORD]")
        sys.exit(0)

    value = ' '.join(sys.argv[1:]) 
    prefix, suffix = hash(value)

    r = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')

    if r.status_code != 200:
        print(danger(f"Request Error. Status code: {r.status_code}"))
        sys.exit(0)

    is_present = suffix in r.text
    if is_present:
        freq = get_pw_freq(suffix, r.text.splitlines()) 
        print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+\n")
        danger(f"\tThere {'was' if freq==1 else 'were' } {freq} occurrence{'s' if freq > 1 else ''} of your password online!")
        danger("\tChange your password for safer measures.\n")
        print("~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+")
    else:
        print(f"{Fore.GREEN}Your password has not been leaked.{Style.RESET_ALL}")

    print(f"{Fore.GREEN}Bye!{Style.RESET_ALL}")


