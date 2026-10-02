def yes_no(question):
    while True:
        answer = input(f"{question} (بله/خیر): ").strip()

        if answer in ["بله", "خیر"]:
            return answer == "بله"

        print("لطفاً فقط «بله» یا «خیر» وارد کنید.")


def get_patient_data():

    patient = {}

    print("=" * 50)
    print("      پرسشنامه ارزیابی درمان کاهش وزن")
    print("=" * 50)

    print("\nلطفاً اطلاعات را با دقت وارد کنید.\n")

    # اطلاعات پایه
    patient["age"] = int(input("سن: "))

    patient["sex"] = input("جنسیت (زن/مرد): ").strip()

    patient["height"] = float(input("قد (سانتی‌متر): "))
    patient["weight"] = float(input("وزن (کیلوگرم): "))

    # محاسبه BMI
    height_m = patient["height"] / 100
    patient["bmi"] = patient["weight"] / (height_m ** 2)

    print(f"\nشاخص توده بدنی (BMI) شما: {patient['bmi']:.1f}")

    # بیماری‌های همراه
    print("\n--- بیماری‌های زمینه‌ای ---")

    patient["diabetes"] = yes_no(
        "آیا به دیابت نوع ۲ مبتلا هستید؟"
    )

    patient["hypertension"] = yes_no(
        "آیا فشار خون بالا دارید؟"
    )

    patient["dyslipidemia"] = yes_no(
        "آیا چربی خون بالا دارید؟"
    )

    patient["cardiovascular_disease"] = yes_no(
        "آیا بیماری قلبی یا عروقی دارید؟"
    )

    patient["sleep_apnea"] = yes_no(
        "آیا آپنه خواب (وقفه تنفسی هنگام خواب) دارید؟"
    )

    # موارد مهم پزشکی
    print("\n--- سابقه پزشکی ---")

    patient["pregnancy"] = yes_no(
        "آیا در حال حاضر باردار هستید؟"
    )

    patient["planning_pregnancy"] = yes_no(
        "آیا قصد بارداری دارید؟"
    )

    patient["pancreatitis"] = yes_no(
        "آیا تاکنون دچار التهاب لوزالمعده (پانکراتیت) شده‌اید؟"
    )

    patient["gallbladder"] = yes_no(
        "آیا بیماری یا سنگ کیسه صفرا دارید؟"
    )

    patient["gastroparesis"] = yes_no(
        "آیا دچار تخلیه بسیار کند معده (گاستروپارزی شدید) هستید؟"
    )

    patient["mtc"] = yes_no(
        "آیا خودتان یا یکی از اعضای خانواده‌تان سرطان مدولاری تیروئید داشته‌اید؟"
    )

    patient["men2"] = yes_no(
        "آیا به سندرم MEN2 مبتلا هستید؟"
    )

    # داروهای فعلی
    print("\n--- داروهای مصرفی ---")

    patient["insulin"] = yes_no(
        "آیا انسولین مصرف می‌کنید؟"
    )

    patient["sulfonylurea"] = yes_no(
        "آیا داروهایی مانند گلی‌بنکلامید، گلیمپیرید یا گلی‌کلازید مصرف می‌کنید؟"
    )

    patient["other_glp1"] = yes_no(
        "آیا در حال حاضر آمپول یا داروی دیگری برای کاهش وزن/دیابت از گروه GLP-1 مصرف می‌کنید؟"
    )

    return patient