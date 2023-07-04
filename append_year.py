
# This block of code changes the year on a list of dates

years = ["january 2023" , "May 2025", "April 2024", "August 2034","September 2025"]

update_years = []

for year in years:
    if year.endswith("2025"):
        new = year.replace("2025" , "2030")
        update_years.append(new)


    else:
        update_years.append(year)

print(update_years)

