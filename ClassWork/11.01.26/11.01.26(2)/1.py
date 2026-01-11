seconds_one = int(input("Час в секундах: "))

total_seconds = 24 * 3600
seconds_left = total_seconds - seconds_one

hours = seconds_left // 3600
minutes = (seconds_left % 3600) // 60
seconds = (seconds_left % 60)

print(f"До полночи осталось: {hours} часов {minutes} минут {seconds} секунд")