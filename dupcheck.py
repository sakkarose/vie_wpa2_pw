def check_duplicates(filename):
  """Checks for duplicate entries in a text file.

  Args:
      filename: The path to the text file.

  Returns:
      A list of duplicate entries, or an empty list if no duplicates are found.
  """

  with open(filename, "r") as file:
    lines = file.readlines()

  seen = set()
  duplicates = []
  for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace
    if line in seen:
      duplicates.append(line)
    else:
      seen.add(line)

  return duplicates

# Get the filename from the user
filename = "vie-common_date.txt"  # Replace with your actual file name

# Check for duplicates
duplicates = check_duplicates(filename)

if duplicates:
  print("Duplicate entries found:")
  for duplicate in duplicates:
    print(duplicate)
else:
  print("No duplicate entries found.")
