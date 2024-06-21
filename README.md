# Handcrafted WiFi Password Dictionaries & Rules for VIE Access Points

This repository contains specialized wordlists tailored for cracking WiFi passwords, with a focus on likely patterns found in Vietnam.

**Wordlists**

* **rockyou_wpa2.txt** - A modified version of the classic Rockyou wordlist optimized for WPA2 password attacks (original source: Kali Linux 2021.3).

* **vie-common_date.txt** -  Combined common Vietnamese possible date-related formats. Generated and optimized using CDate_gen.py.
  - DDMMYYYY & MMDDYYYY as legit days 1970 to 2025.
  - YYYY+yyyy with both being years from 1970 to 2025.
  - DDMM+ddmm with both being possible date in a year.

* **vie-phonenumber_main.txt** - Replaced by .rule file.

* **vie-phonenumber_main.rule** - A Hashcat rule file designed to generate 10-digit Vietnamese phone numbers for mask-based attacks. Prioritizes commonly used prefixes from major providers (Viettel, Mobifone, and Vinaphone).

**On-going Projects**

* **Usernames from exposed log files** - A collection of usernames extracted from publicly available log file exposures.

* **Passwords from exposed log files** - A collection of passwords extracted from publicly available log file exposures.

**Explanation of vie-phonenumber_main**

The `vie-phonenumber_main.txt` wordlist was omitted due to its large size (~3.2GB).  The `vie-phonenumber_main.rule` file serves as a compact and efficient replacement for mask attacks in Hashcat. If needed, you can use the **PNm_gen.py** to generate the wordlist.

**Important Note:** Please use these resources responsibly and ethically. 
