def calculate_bmi(weight, height):
    if weight > 0 and height > 0:
        bmi = weight / (height / 100) ** 2
        return bmi
    else:
        return None

def main():
    print("BMI Calculator")
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (e.g., 70): "))
            height = float(input("Enter your height in centimeters (e.g., 175): "))
            bmi = calculate_bmi(weight, height)
            if bmi is not None:
                print(f"Your BMI is: {bmi:.2f}")
                if bmi < 18.5:
                    print("You are underweight.")
                elif bmi < 25:
                    print("You are normal weight.")
                elif bmi < 30:
                    print("You are overweight.")
                else:
                    print("You are obese.")
                break
            else:
                print("Invalid input. Please make sure weight and height are positive values.")
        except ValueError:
            print("Invalid input. Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
