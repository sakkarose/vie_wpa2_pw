# WPA2 Dicts & Hashcat Rules

This is the resources I have researched and learned as a wireless network pentester which is my part-time work. This repository contains specialized wordlists tailored for cracking WiFi passwords, with a focus on likely patterns found in Vietnam (with **vie-** as file prefix, and none for generic rules file).

**Important Note:** Please use these resources responsibly and ethically

**Route**
* Since I analyzed the dictionaries to determine the most efficient route for dehashing by removing duplicates, you can benefit from my optimized approach.
* **vie-personal_dehashed_dict.txt** > **vie-common_date.txt** > **vie-phonenumber_main.rule** > **vie-miscnumber.rule** > **rockyou_wpa2.txt** > **...** > **vie-phonenumber_sub.rule**

**Wordlists**

* **vie-personal_dehashed_dict.txt** - Actual Vietnamese AP passwords that I have through dehashing pcap files my multiple Raspberry Pi devices collected.

* **vie-common_date.txt** -  Combined common Vietnamese date-related formats dictionary. Generated and optimized using **CDate_gen.py**. This includes:
  - Days from 1970 to 2025 in DDMMYYYY & MMDDYYYY formats.
  - Every combinations of 2 random years from 1970 to 2025 in YYYYyyyy format.
  - Every combinations of 2 random date in a year in DDMMddmm & MMDDmmdd formats.

* **vie-phonenumber_main.rule** - A Hashcat rule file designed to generate 10-digit Vietnamese phone numbers for mask-based attacks.
  - Prioritizes prefixes from major providers including Viettel, Mobifone, and Vinaphone (Viettel 032, 033, 034, 035, 036, 037, 038, 039, 086, 096, 097, 098 / Mobifone 070, 076, 077, 078, 079, 089, 090, 093 / Vinaphone 081, 082, 083, 084, 085, 088, 091, 094).
  - Prefixes (033, 086, 077, 093, 088) have higher priority than the rests.

* **vie-phonenumber_sub.rule** - A Hashcat rule file designed to generate 10-digit Vietnamese phone numbers for mask-based attacks.
  - Consists of prefixes from minor providers including Vietnammobile, Gmobile, Itelecom, Wintel, VNSKY, FPT and myLocal (Vietnamobile 052, 056, 058, 092 / Gmobile 059, 099 / Itelecom 087 / Wintel 0559 / VNSKY 0777 / FPT 0775 / myLocal 0898, 0896, 0899).

* **vie-miscnumber.rule** -A Hashcat rule file designed for many short masks that aren't long enough to warrant a separate rule file. This includes:
  - 8-digits Vietnamese Hotline prefixes (1800 & 1900)
 
* **rockyou_wpa2.txt** - A modified version of the classic Rockyou wordlist optimized for WPA2 password attacks (original source: Kali Linux 2021.3)

* **vie-phonenumber_main.txt** - Replaced by **vie-phonenumber_*.rule** files. Generated and optimized using **PNm_gen.py**.

**Miscellaneous**

* **Dup_check.py** - Used for doublechecking if there are duplicates in a wordlist.
* **SSID_remove.py** - Used for doublechecking if there are possible SSID in a wordlist instead of a possible password.
* **Potfile_update.py** - Used for adding (actual) new entry from my potfile to **vie-personal_dehashed_dict.txt**.

**Explanation of vie-phonenumber_main**

The `vie-phonenumber_main.txt` wordlist was omitted due to its large size (~3.2GB).  The `vie-phonenumber_main.rule` file serves as a compact and efficient replacement for mask attacks in Hashcat. If needed, you can use the **PNm_gen.py** to generate the wordlist.
