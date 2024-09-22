age = int(input("\nEnter your age: "))


def calculate_max_heartbeat_rate(age):
    heartbeat_rate = 200 - age
    minimum_heart_rate = heartbeat_rate * 0.50
    maximum_heart_rate = heartbeat_rate * 0.85

    return minimum_heart_rate, maximum_heart_rate, heartbeat_rate

hbr, min_heartbeat_rate, max_heartbeat_rate = calculate_max_heartbeat_rate(age)

print(f"\nMaximum Heartbeat Rate: {hbr} bpm")
print(f"\nHeartbeat Rate Range: {min_heartbeat_rate:.2f} - {max_heartbeat_rate:.2f} bpm")