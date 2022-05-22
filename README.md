# Check if your password has been leaked online

---

Example:

<img src="https://user-images.githubusercontent.com/17888328/169696347-200e0289-5bfe-4f9a-bfdc-4db30cfd2828.png" width="600" height="230"/>

This tool hashes your password using sha1 function.

Part of the hash is sent to the database of breached hashes.

API returns all the hashes that contain the input.

<<<<<<< HEAD
The script matches input hash with the result and prints the frequency.
=======
The script matches input hash with the result and print the frequency.
>>>>>>> 4ddf5a5dc1eddf809eeec9fa28d6d7f7c24b1f39

Dependencies:

1. hashlib
2. requests
3. pwinput
4. colorama

The API used for this tool: https://haveibeenpwned.com
