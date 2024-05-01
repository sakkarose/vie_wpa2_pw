def is_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def remove_duplicates(filename):
    with open(filename, "r") as infile:
        lines = infile.readlines()  

    unique_lines = set(lines)  

    with open(filename, "w") as outfile:  
        outfile.writelines(unique_lines)

filename = "vie-date_of_birth.txt" 

with open(filename, "a") as outfile:  
    for year in range(1970, 2025):
        for month in range(1, 13):
            # Adjust number of days based on month and leap year
            if month == 2:
                if is_leap_year(year):
                    max_days = 29
                else:
                    max_days = 28
            elif month in [4, 6, 9, 11]:
                max_days = 30
            else:
                max_days = 31

            for day in range(1, max_days + 1):
                # Output both formats
                outfile.write(f"{day:02d}{month:02d}{year}\n")   
                outfile.write(f"{month:02d}{day:02d}{year}\n")  

# Remove duplicates after generation is complete
remove_duplicates(filename) 
