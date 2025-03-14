from django.shortcuts import render

# Function to calculate age
def calculate_age(birth_day, birth_month, birth_year, current_day, current_month, current_year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if birth_day > current_day:
        current_day += months[birth_month - 1]
        current_month -= 1

    if birth_month > current_month:
        current_year -= 1
        current_month += 12

    day = current_day - birth_day
    month = current_month - birth_month
    year = current_year - birth_year

    return year, month, day  # Return years, months, days

# View function
def index(request):
    age = None  # Ensure age is None on GET request
    if request.method == "POST":
        try:
            birth_day = int(request.POST.get("birth_day", 0))
            birth_month = int(request.POST.get("birth_month", 0))
            birth_year = int(request.POST.get("birth_year", 0))

            current_day = int(request.POST.get("current_day", 0))
            current_month = int(request.POST.get("current_month", 0))
            current_year = int(request.POST.get("current_year", 0))

            # Check if input is valid
            if birth_day and birth_month and birth_year and current_day and current_month and current_year:
                age = calculate_age(birth_day, birth_month, birth_year, current_day, current_month, current_year)

        except ValueError:
            age = None  # Handle invalid input

    return render(request, "ageapp/index.html", {"age": age})





       

