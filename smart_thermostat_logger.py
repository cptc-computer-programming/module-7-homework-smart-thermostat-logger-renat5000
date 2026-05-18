MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76

# 1. Ask the user how many temperature readings they want to enter.
read_temp = int(input("How many temperature readings do you want to enter? "))

# 2. Validate that the number of readings entered is greater than 0.
while read_temp <= 0:
    print("Please enter a number greater than 0.")
    read_temp = int(input("How many temperature readings do you want to enter? "))

# 3. Use a for loop to ask for each temperature reading.
total_temp = 0
below_comfort_count = 0
above_comfort_count = 0  

# 4. Validate that each temperature is between 40 and 100 degrees, inclusive.
for i in range(read_temp):
    temp = float(input(f"Enter temperature reading {i + 1}: "))
    while temp < MIN_VALID_TEMP or temp > MAX_VALID_TEMP:
        print(f"Please enter a temperature between {MIN_VALID_TEMP} and {MAX_VALID_TEMP}.")
        temp = float(input(f"Enter temperature reading {i + 1}: "))

    # 5. Keep a running total of all valid temperature readings.
    total_temp += temp

    # 6. Count how many readings are below the comfort range.
    if temp < COLD_LIMIT:
        below_comfort_count += 1

    # 7. Count how many readings are above the comfort range.
    if temp > WARM_LIMIT:
        above_comfort_count += 1

# 8. Calculate the average temperature.
average_temp = total_temp / read_temp if read_temp > 0 else 0

# 9. Display a summary.
print("\nSummary:")
print(f"Total valid readings: {read_temp}")
print(f"Average temperature: {average_temp:.2f}")
print(f"Readings below comfort range: {below_comfort_count}")
print(f"Readings above comfort range: {above_comfort_count}")