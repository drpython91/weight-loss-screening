from eligibility import (
    evaluate_patient,
    ELIGIBLE,
    NOT_ELIGIBLE,
    CONTRAINDICATED,
    NEEDS_PHYSICIAN_REVIEW,
    NO_CLEAR_BARRIER
)


def base_patient():

    return {
        "bmi": 32,

        "diabetes": False,
        "hypertension": False,
        "dyslipidemia": False,
        "cardiovascular": False,
        "sleep_apnea": False,

        "pregnancy": False,
        "planning_pregnancy": False,

        "mtc": False,
        "men2": False,

        "gastroparesis": False,
        "pancreatitis": False,
        "gallbladder": False,
        "other_glp1": False
    }


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
    assert result["semaglutide"]["status"] is None


def test_mtc():

    patient = base_patient()

    patient["mtc"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == CONTRAINDICATED
    assert result["tirzepatide"]["status"] == CONTRAINDICATED
    assert result["liraglutide"]["status"] == CONTRAINDICATED


def test_men2():

    patient = base_patient()

    patient["men2"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == CONTRAINDICATED
    assert result["tirzepatide"]["status"] == CONTRAINDICATED
    assert result["liraglutide"]["status"] == CONTRAINDICATED


def test_pregnancy():

    patient = base_patient()

    patient["pregnancy"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW
    assert result["tirzepatide"]["status"] == NEEDS_PHYSICIAN_REVIEW
    assert result["liraglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_planning_pregnancy():

    patient = base_patient()

    patient["planning_pregnancy"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_unknown():

    patient = base_patient()

    patient["pancreatitis"] = None

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_gastroparesis():

    patient = base_patient()

    patient["gastroparesis"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW


def test_other_glp1():

    patient = base_patient()

    patient["other_glp1"] = True

    result = evaluate_patient(patient)

    assert result["semaglutide"]["status"] == NEEDS_PHYSICIAN_REVIEW