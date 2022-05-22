# Check if your password has been leaked online

---

Example:
<img src="https://user-images.githubusercontent.com/17888328/169696347-200e0289-5bfe-4f9a-bfdc-4db30cfd2828.png" width="600" height="230"/>

This tool will hash your input for security and send only part of the hash to a big leaked password database.
The result will be all the hashes that contain the part sent and their frequencies.
The tool then matches your password (the hashed version) with the result of the request and grab the frequency.

Dependencies:

1. hashlib
2. requests
3. pwinput
4. colorama

The API used for this tool: https://haveibeenpwned.com
