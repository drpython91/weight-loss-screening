from drug_rules import (
    DRUG_RULES,
    REASONS,
    UNKNOWN_REASONS
)

CONTRAINDICATED = "CONTRAINDICATED"
NEEDS_PHYSICIAN_REVIEW = "NEEDS_PHYSICIAN_REVIEW"
NO_CLEAR_BARRIER = "NO_CLEAR_BARRIER"

ELIGIBLE = "ELIGIBLE"
NOT_ELIGIBLE = "NOT_ELIGIBLE"


def check_bmi_eligibility(patient):
    """
    BMI >= 30:
        Eligible

    27 <= BMI < 30:
        Eligible if at least one weight-related comorbidity exists

    27 <= BMI < 30 without comorbidity:
        Physician review

    BMI < 27:
        Not eligible

    BMI missing:
        Unknown
    """

    bmi = patient.get("bmi")

    if bmi is None:
        return "UNKNOWN"

    if bmi >= 30:
        return ELIGIBLE

    if bmi < 27:
        return NOT_ELIGIBLE

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

    bmi_status = check_bmi_eligibility(patient)

    result = {
        "drug": drug,
        "eligibility": bmi_status,
        "status": None,
        "reasons": []
    }

    # BMI unknown
    if bmi_status == "UNKNOWN":

        result["status"] = NEEDS_PHYSICIAN_REVIEW

        result["reasons"].append(
            "BMI مشخص نیست."
        )

        return result

    # BMI < 27
    if bmi_status == NOT_ELIGIBLE:

        result["status"] = NOT_ELIGIBLE

        result["reasons"].append(
            "BMI کمتر از 27 است و معیار اولیه ورود به درمان دارویی کاهش وزن وجود ندارد."
        )

        return result

    # BMI 27-30 without comorbidity
    if bmi_status == NEEDS_PHYSICIAN_REVIEW:

        result["status"] = NEEDS_PHYSICIAN_REVIEW

        result["reasons"].append(
            "BMI بین 27 و 30 است و بیماری همراه مرتبط با وزن شناسایی نشده است."
        )

        return result

    # BMI eligible
    rules = DRUG_RULES[drug]

    contraindications = []
    review_reasons = []

    # Contraindications
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

    # Physician review
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

    # Any contraindication
    if contraindications:

        result["status"] = CONTRAINDICATED

        result["reasons"].extend(
            contraindications
        )

        result["reasons"].extend(
            review_reasons
        )

        return result

    # Physician review needed
    if review_reasons:

        result["status"] = NEEDS_PHYSICIAN_REVIEW

        result["reasons"].extend(
            review_reasons
        )

        return result

    # No clear barrier
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