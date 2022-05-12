import hashlib
import requests

value = input("Check password (Press q to exit): ")

while value != 'q':
    hash = hashlib.sha1(bytes(f'{value}', encoding='utf-8')).hexdigest()
    r = requests.get(f'https://api.pwnedpasswords.com/range/{hash[:5].upper()}')
    suffix = hash[5:].upper()
    is_present = suffix in r.text
    if is_present:
        result = int(list(filter(lambda x: x.startswith(suffix), r.text.splitlines()))[0].split(':')[1])
        print(f"There {'was' if result==1 else 'were' } {result} occurrence{'s' if result > 1 else ''} of your password online!")
    else:
        print("Your password has not been leaked.")
    value = input("Check password (Press q to exit): ")


