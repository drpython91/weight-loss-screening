import pytest

from eligibility import (
    evaluate_patient,
    check_bmi_eligibility,
    ELIGIBLE,
    NOT_ELIGIBLE,
    NEEDS_PHYSICIAN_REVIEW,
    NO_CLEAR_BARRIER,
    CONTRAINDICATED
)


def base_patient():
    """
    A completely healthy patient with no unknown answers.
    """

    return {
        "age": 40,
        "weight": 90,
        "height": 170,
        "bmi": 31,

        # Weight-related comorbidities
        "diabetes": False,
        "hypertension": False,
        "dyslipidemia": False,
        "cardiovascular": False,
        "sleep_apnea": False,

        # Pregnancy
        "pregnancy": False,
        "planning_pregnancy": False,

        # Contraindications
        "mtc": False,
        "men2": False,
        "hypersensitivity": False,

        # Physician review
        "gastroparesis": False,
        "pancreatitis": False,
        "gallbladder": False,
        "other_glp1": False
    }


# =========================================================
# BMI TESTS
# =========================================================

def test_bmi_30_or_more():

    patient = base_patient()
    patient["bmi"] = 30

    result = evaluate_patient(patient)

    assert result["semaglutide"]["eligibility"] == ELIGIBLE
    assert result["semaglutide"]["status"] == NO_CLEAR_BARRIER


def test_bmi_27_to_30_with_comorbidity():

    patient = base_patient()

    patient["bmi"] = 28
    patient["hypertension"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["eligibility"] == ELIGIBLE
    assert result["semaglutide"]["status"] == NO_CLEAR_BARRIER


def test_bmi_27_to_30_without_comorbidity():

    patient = base_patient()

    patient["bmi"] = 28

    result = evaluate_patient(patient)

    assert result["semaglutide"]["eligibility"] == NEEDS_PHYSICIAN_REVIEW
    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_bmi_less_than_27():

    patient = base_patient()

    patient["bmi"] = 25

    result = evaluate_patient(patient)

    assert result["semaglutide"]["eligibility"] == NOT_ELIGIBLE
    assert result["semaglutide"]["status"] == NOT_ELIGIBLE


# =========================================================
# CONTRAINDICATION TESTS
# =========================================================

def test_mtc():

    patient = base_patient()

    patient["mtc"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == CONTRAINDICATED


def test_men2():

    patient = base_patient()

    patient["men2"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == CONTRAINDICATED


def test_hypersensitivity():

    patient = base_patient()

    patient["hypersensitivity"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == CONTRAINDICATED


def test_pregnancy():

    patient = base_patient()

    patient["pregnancy"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == CONTRAINDICATED


# =========================================================
# PHYSICIAN REVIEW TESTS
# =========================================================

def test_planning_pregnancy():

    patient = base_patient()

    patient["planning_pregnancy"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_pancreatitis():

    patient = base_patient()

    patient["pancreatitis"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_gallbladder():

    patient = base_patient()

    patient["gallbladder"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_other_glp1():

    patient = base_patient()

    patient["other_glp1"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


# =========================================================
# UNKNOWN ANSWERS
# =========================================================

def test_unknown_mtc():

    patient = base_patient()

    patient["mtc"] = None

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_unknown_pregnancy():

    patient = base_patient()

    patient["pregnancy"] = None

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW