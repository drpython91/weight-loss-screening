import json

import streamlit as st

from eligibility import evaluate_patient


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="غربالگری درمان کاهش وزن",
    page_icon="⚕️",
    layout="centered"
)


# -----------------------------
# RTL / Persian styling
# -----------------------------

st.markdown(
    """
    <style>

    .main {
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3, p, label {
        direction: rtl;
        text-align: right;
    }

    div[data-testid="stRadio"] {
        direction: rtl;
        text-align: right;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Load questions
# -----------------------------

def load_questions():

    with open(
        "questions.json",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data["questions"]


questions = load_questions()


# -----------------------------
# BMI calculation
# -----------------------------

def calculate_bmi(weight, height):

    height_m = height / 100

    return weight / (height_m ** 2)


# -----------------------------
# Page title
# -----------------------------

st.title("غربالگری اولیه درمان کاهش وزن")

st.write(
    "لطفاً اطلاعات زیر را وارد کنید."
)


# -----------------------------
# Patient data
# -----------------------------

patient = {}


for question in questions:

    question_id = question["id"]
    question_type = question["type"]

    # -------------------------
    # Number questions
    # -------------------------

    if question_type == "number":

        if question_id == "weight":

            patient[question_id] = st.number_input(
                question["question"],
                min_value=1.0,
                max_value=500.0,
                value=70.0,
                step=0.5
            )

        elif question_id == "height":

            patient[question_id] = st.number_input(
                question["question"],
                min_value=50.0,
                max_value=250.0,
                value=170.0,
                step=1.0
            )

        else:

            patient[question_id] = st.number_input(
                question["question"],
                min_value=0.0,
                step=1.0
            )

    # -------------------------
    # Boolean questions
    # -------------------------

    elif question_type == "boolean":

        options = question["options"]

        selected = st.radio(
            question["question"],
            options=list(options.keys()),
            format_func=lambda key: options[key],
            horizontal=True,
            key=question_id
        )

        if selected == "1":

            patient[question_id] = True

        elif selected == "2":

            patient[question_id] = False

        else:

            patient[question_id] = None


# -----------------------------
# Calculate BMI
# -----------------------------

weight = patient["weight"]
height = patient["height"]

bmi = calculate_bmi(
    weight,
    height
)

patient["bmi"] = bmi


# -----------------------------
# Display BMI
# -----------------------------

st.divider()

st.subheader("محاسبه BMI")

st.metric(
    "BMI",
    f"{bmi:.1f}"
)


# -----------------------------
# Evaluation button
# -----------------------------

if st.button(
    "شروع ارزیابی",
    type="primary"
):

    results = evaluate_patient(patient)

    st.divider()

    st.header("نتیجه غربالگری اولیه")


    # -------------------------
    # Results
    # -------------------------

    for result in results.values():

        st.subheader(
            result["drug"]
        )

        # ---------------------
        # Eligibility
        # ---------------------

        eligibility = result["eligibility"]

        if eligibility == "ELIGIBLE":

            st.success(
                "✓ واجد معیار اولیه"
            )

        elif eligibility == "NOT_ELIGIBLE":

            st.warning(
                "معیار اولیه ورود وجود ندارد."
            )

        elif eligibility == "NEEDS_PHYSICIAN_REVIEW":

            st.warning(
                "⚠ نیازمند بررسی پزشک"
            )


        # ---------------------
        # Safety status
        # ---------------------

        status = result["status"]

        if status == "CONTRAINDICATED":

            st.error(
                "✗ منع مصرف شناسایی شد"
            )

        elif status == "NEEDS_PHYSICIAN_REVIEW":

            st.warning(
                "⚠ نیازمند بررسی پزشک"
            )

        elif status == "NO_CLEAR_BARRIER":

            st.success(
                "✓ مانع واضحی در غربالگری اولیه پیدا نشد"
            )


        # ---------------------
        # Reasons
        # ---------------------

        if result["reasons"]:

            st.write("دلایل:")

            for reason in result["reasons"]:

                st.write(
                    f"• {reason}"
                )


        # ---------------------
        # Final note
        # ---------------------

        if status == "NO_CLEAR_BARRIER":

            st.info(
                "این نتیجه به معنی تجویز یا تأیید نهایی دارو نیست."
            )

        elif status == "NEEDS_PHYSICIAN_REVIEW":

            st.info(
                "تصمیم نهایی باید توسط پزشک گرفته شود."
            )

        elif status == "CONTRAINDICATED":

            st.info(
                "در غربالگری اولیه، منع مصرف شناسایی شده است."
            )

        st.divider()