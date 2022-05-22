from colorama import Fore, Style
import hashlib

ENDPOINT = "https://api.pwnedpasswords.com/range"

def error(msg):
    return f"{Fore.RED}[!] {msg}{Style.RESET_ALL}"

def success(msg):
    return f"{Fore.GREEN}{msg}{Style.RESET_ALL}"

def hash(value):
    if not value: return []

    digest = hashlib.sha1(bytes(f'{value}', encoding='utf-8')).hexdigest()

    prefix = digest[:5].upper()
    suffix = digest[5:].upper()

    return (prefix, suffix)