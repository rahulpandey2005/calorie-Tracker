#Fit_MAN

import numpy as np
import pandas as pd



data = {
    "Age": [25, 30, 35, 40, 28],
    "Height_cm": [170, 165, 180, 175, 160],
    "Weight_kg": [65, 72, 85, 78, 55],
    "Calories_Intake": [2200, 2500, 2800, 2600, 2000],
    "Calories_Burned": [2100, 2300, 2600, 2400, 1900],
    "Resting_Heart_Rate": [72, 78, 85, 90, 70],
    "Steps": [8000, 6000, 5000, 4000, 10000]
}

df = pd.DataFrame(data)



df["Height_m"] = df["Height_cm"] / 100
df["BMI"] = df["Weight_kg"] / (df["Height_m"] ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["BMI_Category"] = df["BMI"].apply(bmi_category)



df["Calorie_Balance"] = df["Calories_Intake"] - df["Calories_Burned"]

df["Calorie_Status"] = np.where(
    df["Calorie_Balance"] > 0,
    "Calorie Surplus",
    "Calorie Deficit"
)



def heart_rate_status(hr):
    if hr < 60:
        return "Low"
    elif hr <= 100:
        return "Normal"
    else:
        return "High"

df["Heart_Rate_Status"] = df["Resting_Heart_Rate"].apply(heart_rate_status)



def activity_level(steps):
    if steps < 5000:
        return "Sedentary"
    elif steps < 8000:
        return "Moderately Active"
    else:
        return "Active"

df["Activity_Level"] = df["Steps"].apply(activity_level)



summary = {
    "Average BMI": round(df["BMI"].mean(), 2),
    "Most Common BMI Category": df["BMI_Category"].mode()[0],
    "Average Heart Rate": round(df["Resting_Heart_Rate"].mean(), 2),
    "Average Daily Steps": int(df["Steps"].mean()),
    "People in Calorie Surplus": int((df["Calorie_Status"] == "Calorie Surplus").sum()),
    "People in Calorie Deficit": int((df["Calorie_Status"] == "Calorie Deficit").sum())
}

summary_df = pd.DataFrame(summary, index=["Health Summary"])



print("\n--- Health Data Analysis ---\n")
print(df)

print("\n--- Overall Health Summary ---\n")
print(summary_df)
