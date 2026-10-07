def yes_no_unknown(question):
    while True:
        answer = input(
            f"{question} (بله/خیر/نمی‌دانم): "
        ).strip()

        if answer == "بله":
            return True

        if answer == "خیر":
            return False

        if answer == "نمی‌دانم":
            return None

        print("لطفاً فقط «بله»، «خیر» یا «نمی‌دانم» وارد کنید.")


def get_patient_data():

    patient = {}

    print("=" * 50)
    print("      پرسشنامه ارزیابی درمان کاهش وزن")
    print("=" * 50)

    print("\nلطفاً اطلاعات را با دقت وارد کنید.\n")

    # -------------------------
    # اطلاعات پایه
    # -------------------------

    patient["age"] = int(input("سن: "))

    patient["sex"] = input(
        "جنسیت (زن/مرد): "
    ).strip()

    patient["height"] = float(
        input("قد (سانتی‌متر): ")
    )

    patient["weight"] = float(
        input("وزن (کیلوگرم): ")
    )

    # محاسبه BMI
    height_m = patient["height"] / 100

    patient["bmi"] = (
        patient["weight"] / (height_m ** 2)
    )

    print(
        f"\nشاخص توده بدنی (BMI): "
        f"{patient['bmi']:.1f}"
    )

    # -------------------------
    # بیماری‌های همراه
    # -------------------------

    print("\n--- بیماری‌های زمینه‌ای ---")

    patient["diabetes"] = yes_no_unknown(
        "آیا به دیابت نوع ۲ مبتلا هستید؟"
    )

    patient["hypertension"] = yes_no_unknown(
        "آیا فشار خون بالا دارید؟"
    )

    patient["dyslipidemia"] = yes_no_unknown(
        "آیا چربی خون بالا دارید؟"
    )

    patient["cardiovascular"] = yes_no_unknown(
        "آیا بیماری قلبی یا عروقی دارید؟"
    )

    patient["sleep_apnea"] = yes_no_unknown(
        "آیا آپنه خواب (وقفه تنفسی هنگام خواب) دارید؟"
    )

    # -------------------------
    # بارداری
    # -------------------------

    print("\n--- بارداری ---")

    patient["pregnancy"] = yes_no_unknown(
        "آیا در حال حاضر باردار هستید؟"
    )

    patient["planning_pregnancy"] = yes_no_unknown(
        "آیا قصد بارداری دارید؟"
    )

    # -------------------------
    # سابقه پزشکی
    # -------------------------

    print("\n--- سابقه پزشکی ---")

    patient["mtc"] = yes_no_unknown(
        "آیا خودتان یا یکی از اعضای خانواده‌تان "
        "سابقه سرطان مدولاری تیروئید (MTC) داشته‌اید؟"
    )

    patient["men2"] = yes_no_unknown(
        "آیا سابقه سندرم MEN2 دارید؟"
    )

    patient["pancreatitis"] = yes_no_unknown(
        "آیا تاکنون به پانکراتیت "
        "(التهاب لوزالمعده) مبتلا شده‌اید؟"
    )

    patient["gallbladder"] = yes_no_unknown(
        "آیا سابقه سنگ یا بیماری کیسه صفرا دارید؟"
    )

    patient["gastroparesis"] = yes_no_unknown(
        "آیا به‌طور مکرر علائمی مانند "
        "پری طولانی‌مدت بعد از غذا، سیری زودرس، "
        "تهوع، استفراغ غذای هضم‌نشده یا احساس ماندن "
        "غذا در معده دارید؟"
    )

    patient["hypersensitivity"] = yes_no_unknown(
        "آیا تاکنون به یکی از این داروها یا "
        "ترکیبات آن‌ها واکنش حساسیتی شدید داشته‌اید؟"
    )

    # -------------------------
    # داروهای مصرفی
    # -------------------------

    print("\n--- داروهای مصرفی ---")

    patient["insulin"] = yes_no_unknown(
        "آیا انسولین مصرف می‌کنید؟"
    )

    patient["sulfonylurea"] = yes_no_unknown(
        "آیا داروهایی مانند گلی‌بنکلامید، "
        "گلیمپیرید یا گلی‌کلازید مصرف می‌کنید؟"
    )

    patient["other_glp1"] = yes_no_unknown(
        "آیا در حال حاضر آمپول یا داروی دیگری "
        "از گروه GLP-1 یا داروی مشابه برای کاهش "
        "وزن یا دیابت مصرف می‌کنید؟"
    )

    return patient