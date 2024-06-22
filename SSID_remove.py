import re

def filter_passwords(filename):
    with open(filename, "r+", encoding="utf-8", newline="\n") as f:  # Specify newline as Unix LF
        lines = f.readlines()
        f.seek(0)
        f.truncate()

        filtered_lines = []
        for line in lines:
            password = line.strip()

            # Check for password length, unicode characters, and space characters
            if 8 <= len(password) <= 29 and not re.search(r'[\u0080-\uffff|\s]', password):
                filtered_lines.append(f"{password}\n")

        # Write filtered content
        f.writelines(filtered_lines)


filename = "vie-personal_dehashed_dict.txt"
filter_passwords(filename)
