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
