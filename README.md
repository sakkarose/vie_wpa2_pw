# WPA2 Dicts & Hashcat Rules

This repository contains specialized wordlists tailored for cracking WiFi passwords, with a focus on likely patterns found in Vietnam.

**Wordlists**

* **rockyou_wpa2.txt** - A modified version of the classic Rockyou wordlist optimized for WPA2 password attacks (original source: Kali Linux 2021.3).

* **vie-common_date.txt** -  Combined common Vietnamese date-related formats dictionary. Generated and optimized using CDate_gen.py. This includes:
  - Days from 1970 to 2025 in DDMMYYYY & MMDDYYYY formats.
  - Every combinations of 2 random years from 1970 to 2025 in YYYY+yyyy format.
  - Every combinations of 2 random date in a year in DDMM+ddmm MMDD+mmdd formats.

* **vie-phonenumber_main.txt** - Replaced by .rule file.

* **vie-phonenumber_main.rule** - A Hashcat rule file designed to generate 10-digit Vietnamese phone numbers for mask-based attacks. Prioritizes commonly used prefixes from major providers (Viettel, Mobifone, and Vinaphone).

**Miscellaneous**

* **dupcheck.py** - Used for doublechecking if there are duplicates in a wordlist.

**Explanation of vie-phonenumber_main**

The `vie-phonenumber_main.txt` wordlist was omitted due to its large size (~3.2GB).  The `vie-phonenumber_main.rule` file serves as a compact and efficient replacement for mask attacks in Hashcat. If needed, you can use the **PNm_gen.py** to generate the wordlist.

**Important Note:** Please use these resources responsibly and ethically. 
