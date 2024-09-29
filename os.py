import os
import random
import datetime

# Function to generate a list of random dates across multiple years
def generate_random_dates(years, commits_per_year=50):
    random_dates = []
    for year in years:
        for _ in range(commits_per_year):
            # Randomly choose a month and day in the given year
            month = random.randint(1, 12)
            day = random.randint(1, 28)  # Safe to keep it up to 28 to avoid invalid days in February
            random_date = datetime.datetime(year, month, day)
            random_dates.append(random_date)
    return random_dates

# Generate dates for 2019, 2020, 2021, 2022, 2023, and 2024
years_to_generate = [2019, 2020, 2021, 2022, 2023, 2024]
dates = generate_random_dates(years_to_generate)

# Loop through each generated date and create a commit
for commit_date in dates:
    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    # Write to the text file to simulate changes
    with open("test.txt", "a") as file:
        file.write(f"Commit on {date_str}\n")
    
    # Stage the changes
    os.system("git add test.txt")
    # Commit with the specific backdated date
    os.system(f'git commit --date="{date_str}" -m "Commit on {date_str}"')

# Force push the new commits to the main branch
os.system("git push -u origin master -f")
