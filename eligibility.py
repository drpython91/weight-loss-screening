# eligibility.py

from drug_rules import (
    DRUG_RULES,
    REASONS,
    UNKNOWN_REASONS
)


# وضعیت ایمنی دارو
CONTRAINDICATED = "CONTRAINDICATED"
NEEDS_PHYSICIAN_REVIEW = "NEEDS_PHYSICIAN_REVIEW"
NO_CLEAR_BARRIER = "NO_CLEAR_BARRIER"

# وضعیت معیار اولیه ورود
ELIGIBLE = "ELIGIBLE"
NOT_ELIGIBLE = "NOT_ELIGIBLE"


def check_bmi_eligibility(patient):
    """
    بررسی معیار اولیه BMI برای ورود به ارزیابی درمان دارویی.

    BMI >= 30:
        واجد معیار اولیه

    BMI بین 27 و کمتر از 30:
        در صورت وجود حداقل یک کوموربیدیتی مرتبط با وزن،
        واجد معیار اولیه است.

    BMI بین 27 و کمتر از 30 بدون کوموربیدیتی:
        نیازمند ارزیابی پزشک

    BMI < 27:
        واجد معیار اولیه نیست.
    """

    bmi = patient.get("bmi")

    if bmi is None:
        return "UNKNOWN"

    # BMI >= 30
    if bmi >= 30:
        return ELIGIBLE

    # BMI < 27
    if bmi < 27:
        return NOT_ELIGIBLE

    # 27 <= BMI < 30
    comorbidities = [
        patient.get("diabetes"),
        patient.get("hypertension"),
        patient.get("dyslipidemia"),
        patient.get("cardiovascular"),
        patient.get("sleep_apnea")
    ]

    if any(value is True for value in comorbidities):
        return ELIGIBLE

    return NEEDS_PHYSICIAN_REVIEW


def evaluate_drug(drug, patient):
    """
    ارزیابی اولیه یک دارو.

    ابتدا معیار BMI بررسی می‌شود.
    سپس، در صورت امکان، ایمنی دارو بررسی می‌شود.
    """

    bmi_status = check_bmi_eligibility(patient)

    result = {
        "drug": drug,
        "eligibility": bmi_status,
        "status": None,
        "reasons": []
    }

    # BMI نامشخص
    if bmi_status == "UNKNOWN":

        result["status"] = NEEDS_PHYSICIAN_REVIEW

        result["reasons"].append(
            "BMI مشخص نیست."
        )

        return result

    # BMI کمتر از 27
    if bmi_status == NOT_ELIGIBLE:

        result["reasons"].append(
            "BMI کمتر از 27 است و معیار اولیه ورود به درمان دارویی وجود ندارد."
        )

        return result

    # BMI بین 27 و 30 بدون کوموربیدیتی
    if bmi_status == NEEDS_PHYSICIAN_REVIEW:

        result["status"] = NEEDS_PHYSICIAN_REVIEW

        result["reasons"].append(
            "BMI بین 27 و 30 است و بیماری همراه مرتبط با وزن شناسایی نشده است."
        )

        return result

    # --------------------------------
    # از اینجا به بعد بیمار واجد معیار اولیه است
    # --------------------------------

    rules = DRUG_RULES[drug]

    contraindications = []
    review_reasons = []

    # بررسی موارد منع مصرف
    for field in rules["contraindications"]:

        value = patient.get(field)

        if value is True:

            contraindications.append(
                REASONS[field]
            )

        elif value is None:

            review_reasons.append(
                UNKNOWN_REASONS[field]
            )

    # بررسی موارد نیازمند نظر پزشک
    for field in rules["physician_review"]:

        value = patient.get(field)

        if value is True:

            review_reasons.append(
                REASONS[field]
            )

        elif value is None:

            review_reasons.append(
                UNKNOWN_REASONS[field]
            )

    # اگر منع مصرف وجود داشته باشد
    if contraindications:

        result["status"] = CONTRAINDICATED

        result["reasons"].extend(
            contraindications
        )

        result["reasons"].extend(
            review_reasons
        )

        return result

    # اگر نیاز به نظر پزشک وجود داشته باشد
    if review_reasons:

        result["status"] = NEEDS_PHYSICIAN_REVIEW

        result["reasons"].extend(
            review_reasons
        )

        return result

    # هیچ مانع واضحی پیدا نشد
    result["status"] = NO_CLEAR_BARRIER

    return result


def check_semaglutide(patient):

    return evaluate_drug(
        "Semaglutide",
        patient
    )


def check_tirzepatide(patient):

    return evaluate_drug(
        "Tirzepatide",
        patient
    )


def check_liraglutide(patient):

    return evaluate_drug(
        "Liraglutide",
        patient
    )


def evaluate_patient(patient):

    return {
        "semaglutide": check_semaglutide(patient),
        "tirzepatide": check_tirzepatide(patient),
        "liraglutide": check_liraglutide(patient)
    }