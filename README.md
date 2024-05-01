# wifi_password_dicts
- [rockyou_wpa2.txt](https://github.com/sakkarose/rockyou_wpa2_dicts/blob/main/rockyou_wpa2.txt) - Modified rockyou wordlist for WPA2 
(Original rockyou file is from Kali Linux 2021.3)
- [date_of_birth.txt](https://github.com/sakkarose/wifi_password_dicts/blob/main/date_of_birth.txt) - Valid date of birth that Vietnamese uses (DDMMYYYY and MMDDYYYY format) with YYYY being from 1970 to 2024. Generated and optimized using [DoB_gen.py](https://github.com/sakkarose/wifi_password_dicts/blob/main/DoB_gen.py).
- vie-phonenumber_main.txt - Possible phone numbers for every 3 digits prefix that the 3 largest providers (Viettel, Mobifone and Vinaphone) use. Generated and optimized using [PNm_gen.py](https://github.com/sakkarose/wifi_password_dicts/blob/main/PNm_gen.py). The wordlist is not uploaded since I don't use it (too large ~ 3.2GB).
- [vie-phonenumber_main.rule](https://github.com/sakkarose/wifi_password_dicts/blob/main/vie-phonenumber_main.rule) - Created to replace the wordlist with the same output for Mask attack on hashcat. 033, 086, 077, 093 and 088 being the high priority due to being the most used phone number prefix from the same providers.
- [On-going] - Usernames from exposed log files. 
- [On-going] - Passwords from exposed log files. 

# WiFi Password Dictionaries

This repository contains specialized wordlists tailored for cracking WiFi passwords, with a focus on likely patterns found in Vietnam.

**Wordlists**

* **rockyou_wpa2.txt** - A modified version of the classic Rockyou wordlist optimized for WPA2 password attacks (original source: Kali Linux 2021.3).

* **date_of_birth.txt** -  Common Vietnamese date-of-birth formats (DDMMYYYY and MMDDYYYY), covering the years 1970 to 2024.  Generated and optimized using DoB_gen.py.

* **vie-phonenumber_main.rule** - A Hashcat rule file designed to generate 10-digit Vietnamese phone numbers for mask-based attacks. Prioritizes commonly used prefixes from major providers (Viettel, Mobifone, and Vinaphone).

**On-going Projects**

* **Usernames from exposed log files** - A collection of usernames extracted from publicly available log file exposures.

* **Passwords from exposed log files** - A collection of passwords extracted from publicly available log file exposures.

**Explanation of vie-phonenumber_main**

The `vie-phonenumber_main.txt` wordlist was omitted due to its large size (~3.2GB).  The `vie-phonenumber_main.rule` file serves as a compact and efficient replacement for mask attacks in Hashcat.

**Important Note:** Please use these resources responsibly and ethically. 
