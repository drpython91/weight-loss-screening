import json

from eligibility import evaluate_patient


def load_questions():

    with open("questions.json", encoding="utf-8") as file:
        data = json.load(file)

    return data["questions"]


def ask_question(question):

    print()
    print(question["question"])

    for key, value in question["options"].items():
        print(f"{key}. {value}")

    while True:

        answer = input("انتخاب شما: ").strip()

        if answer in question["options"]:
            return answer

        print("انتخاب نامعتبر است. دوباره وارد کنید.")


def convert_answer(answer):

    if answer == "1":
        return True

    if answer == "2":
        return False

    if answer == "3":
        return None

    return None


def ask_number(question):

    while True:

        answer = input(
            f'{question["question"]} '
        ).strip()

        try:
            value = float(answer)

            if value <= 0:
                print("لطفاً یک عدد بزرگ‌تر از صفر وارد کنید.")
                continue

            return value

        except ValueError:
            print("لطفاً یک عدد معتبر وارد کنید.")


def calculate_bmi(weight, height):

    height_m = height / 100

    return weight / (height_m ** 2)


def build_patient(questions):

    patient = {}

    for question in questions:

        question_type = question["type"]

        if question_type == "number":

            patient[question["id"]] = ask_number(
                question
            )

        elif question_type == "boolean":

            answer = ask_question(question)

            patient[question["id"]] = convert_answer(
                answer
            )

    # محاسبه BMI از وزن و قد
    weight = patient["weight"]
    height = patient["height"]

    patient["bmi"] = calculate_bmi(
        weight,
        height
    )

    return patient


def print_results(results):

    print()
    print("=" * 60)
    print("نتیجه غربالگری اولیه")
    print("=" * 60)

    for result in results.values():

        print()
        print("-" * 60)

        print(f"دارو: {result['drug']}")

        print()
        print("معیار ورود:")

        eligibility = result["eligibility"]

        if eligibility == "ELIGIBLE":
            print("✓ واجد معیار اولیه")

        elif eligibility == "NOT_ELIGIBLE":
            print("✗ معیار اولیه وجود ندارد")

        elif eligibility == "NEEDS_PHYSICIAN_REVIEW":
            print("⚠ نیازمند بررسی پزشک")

        print()
        print("وضعیت ایمنی:")

        status = result["status"]

        if status == "CONTRAINDICATED":
            print("✗ CONTRAINDICATED")

        elif status == "NEEDS_PHYSICIAN_REVIEW":
            print("⚠ NEEDS_PHYSICIAN_REVIEW")

        elif status == "NO_CLEAR_BARRIER":
            print("✓ NO_CLEAR_BARRIER")

        elif status is None:
            print("— در این مرحله تصمیم‌گیری نمی‌شود")

        if result["reasons"]:

            print()
            print("دلایل:")

            for reason in result["reasons"]:
                print(f"- {reason}")

        print()

        if status == "NO_CLEAR_BARRIER":

            print(
                "توجه: این نتیجه به معنی تجویز یا تأیید نهایی دارو نیست."
            )

        elif status == "NEEDS_PHYSICIAN_REVIEW":

            print(
                "توجه: تصمیم نهایی باید توسط پزشک گرفته شود."
            )

        elif status == "CONTRAINDICATED":

            print(
                "توجه: در غربالگری اولیه، منع مصرف شناسایی شده است."
            )

        elif status is None:

            print(
                "توجه: بیمار در این مرحله وارد ارزیابی ایمنی دارو نشده است."
            )

    print()
    print("=" * 60)


def main():

    questions = load_questions()

    patient = build_patient(questions)

    print()
    print(f"سن: {patient['age']} سال")
    print(f"وزن: {patient['weight']} کیلوگرم")
    print(f"قد: {patient['height']} سانتی‌متر")
    print(f"BMI: {patient['bmi']:.1f}")

    results = evaluate_patient(patient)

    print_results(results)


if __name__ == "__main__":
    main()