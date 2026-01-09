


# BMI Calculation
def calculate_bmi(weight, height):
    bmi = weight / np.square(height)
    return round(bmi, 2)




def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_message(bmi):
    if bmi < 18.5:
        return "You are underweight. Focus on calorie surplus, strength training, and proper sleep."
    elif bmi < 25:
        return "Your weight is normal. Maintain your lifestyle with balanced diet and regular exercise."
    elif bmi < 30:
        return "You are overweight. A calorie deficit with daily activity will help."
    else:
        return "You are obese. Consult a professional and prioritize consistent low-impact workouts."

def calorie_message(calories):
    if calories < 1800:
        return "Your calorie needs are low. Avoid skipping meals."
    elif calories < 2200:
        return "Your calorie needs are moderate. Maintain a balanced diet."
    elif calories < 2600:
        return "You have high energy needs. Fuel your body properly."
    else:
        return "You have very high calorie needs. Eat enough to support your activity level."        


#maintance calories 
def maintenance_calories(age, weight, height, gender, activity):
    # Calculate BMR
    height_cm = height * 100
    if gender == "male":
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161

  
    if activity == 1:
        return bmr * 1.2
    elif activity == 2:
        return bmr * 1.375
    elif activity == 3:
        return bmr * 1.55
    elif activity == 4:
        return bmr * 1.725
    else:
        return bmr * 1.9


#User Details
print("----- USER DETAILS -----")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter gender (male/female): ").lower()
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

print("1. Sedentary")
print("2. Light")
print("3. Moderate")
print("4. Active")
print("5. Very Active")

activity = int(input("Choose activity level (1-5): "))


bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print("\n----- BMI & BMR REPORT -----")
print(f"Name: {name}")
print(f"BMI: {bmi}")
print(f"Category: {category}")
bmi_msg = bmi_message(bmi)
print("BMI Advice:", bmi_msg)


calories = maintenance_calories(age, weight, height, gender, activity)
print("\nYour maintenance calories are:", int(calories), "kcal/day")
cal_msg = calorie_message(calories)
print("Calorie Advice:", cal_msg)

#Workout Trackin

print("\n----- WORKOUT TRACKER -----")
days = int(input("Enter number of days to track workout: "))

workout_data = {
    "Day": [],
    "Workout_Minutes": [],
    "Calories_Burned": []
}

for day in range(1, days + 1):
    print(f"\nDay {day}")
    minutes = int(input("Workout minutes: "))
    calories = int(input("Calories burned: "))

    workout_data["Day"].append(day)
    workout_data["Workout_Minutes"].append(minutes)
    workout_data["Calories_Burned"].append(calories)



# csv DataFrame
df = pd.DataFrame(workout_data)
df.to_csv("workout_data.csv", index=False)

print("\nWorkout data saved successfully!")
print(df)




# Graph visualization
plt.figure(figsize=(10, 5))

plt.plot(df["Day"], df["Workout_Minutes"],
         marker='o', linewidth=2, label="Workout Minutes")

plt.plot(df["Day"], df["Calories_Burned"],
         marker='s', linewidth=2, label="Calories Burned")

plt.xlabel("Day")
plt.ylabel("Value")
plt.title("Workout Progress Analysis")
plt.legend()
plt.grid(True)
plt.show()