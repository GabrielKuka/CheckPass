# Check if your password has been leaked online

### Usage: python3 checkpass.py mysecretpassword

This tool will hash your input for security and send only part of the hash to a big leaked password database.
The result will be all the hashes that contain the part sent and their frequencies.
The tool then matches your password (the hashed version) with the result of the request and grab the frequency.

Dependencies:

1. hashlib
2. requests
3. coloraman

The API used here comes from https://haveibeenpwned.com
