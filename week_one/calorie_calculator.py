''' 
Calories = ((Age x 0.2757) + (Weight x 0.03295) + 
            (Heart Rate x 1.0781) — 75.4991) x Time / 8.368
'''

def calculate_calories_burned(age: int, weight: int, heart_rate: int, time: float) -> float:
    return ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368