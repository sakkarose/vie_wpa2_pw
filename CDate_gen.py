import calendar
import itertools

def generate_date_strings(start_year=1970, end_year=2025):
    """
    Generates unique date strings in various formats (DDMMYYYY, MMDDYYYY, YYYYyyyy, DDMMddmm, MMDDmmdd)
    within the specified range of years.
    """
    unique_dates = set()
    
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            for day in range(1, calendar.monthrange(year, month)[1] + 1):
                unique_dates.update([
                    f"{day:02d}{month:02d}{year}",
                    f"{month:02d}{day:02d}{year}"
                ])

                # Generate date combinations within the same month and year
                for day1, day2 in itertools.combinations(range(1, day + 1), 2):  
                    unique_dates.update([
                        f"{day1:02d}{month:02d}{day2:02d}{month:02d}",
                        f"{month:02d}{day1:02d}{month:02d}{day2:02d}"
                    ])
                    
    # Generate all unique year combinations (YYYYyyyy)
    for year1, year2 in itertools.combinations(range(start_year, end_year + 1), 2):
        unique_dates.add(f"{year1}{year2}")

    return unique_dates

# Get the filename from the user
filename = "vie-common_date.txt"

# Generate and write the date strings
with open(filename, "w") as outfile:
    outfile.writelines(f"{date_str}\n" for date_str in generate_date_strings())
