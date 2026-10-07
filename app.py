import json
import streamlit as st

from eligibility import evaluate_patient


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="غربالگری درمان کاهش وزن",
    page_icon="⚕️",
    layout="centered"
)


# =========================================================
# RTL / PERSIAN STYLE
# =========================================================

st.markdown(
    """
    <style>

    .main {
        direction: rtl;
        text-align: right;
    }

    h1, h2, h3, h4, p, label {
        direction: rtl;
        text-align: right;
    }

    div[data-testid="stRadio"] {
        direction: rtl;
        text-align: right;
    }

    div[data-testid="stNumberInput"] {
        direction: rtl;
        text-align: right;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD QUESTIONS
# =========================================================

def load_questions():

    with open(
        "questions.json",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data["questions"]


questions = load_questions()


# =========================================================
# BMI CALCULATION
# =========================================================

def calculate_bmi(weight, height):

    height_m = height / 100

    return weight / (height_m ** 2)


# =========================================================
# PAGE TITLE
# =========================================================

st.title("غربالگری اولیه درمان کاهش وزن")

st.write(
    "لطفاً اطلاعات زیر را با دقت وارد کنید. "
    "این پرسشنامه فقط برای غربالگری اولیه است "
    "و جایگزین تشخیص یا تجویز پزشک نیست."
)


# =========================================================
# PATIENT DATA
# =========================================================

patient = {}


for question in questions:

    question_id = question["id"]

    question_type = question["type"]


    # -----------------------------------------------------
    # NUMBER QUESTIONS
    # -----------------------------------------------------

    if question_type == "number":

        if question_id == "age":

            patient[question_id] = st.number_input(
                question["question"],
                min_value=0,
                max_value=120,
                value=0,
                step=1
            )


        elif question_id == "weight":

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


    # -----------------------------------------------------
    # BOOLEAN QUESTIONS
    # -----------------------------------------------------

    elif question_type == "boolean":

        options = question["options"]

        selected = st.radio(
            question["question"],
            options=list(options.keys()),

            format_func=lambda key: options[key],

            horizontal=True,

            # IMPORTANT:
            # Default = "I don't know"
            index=2,

            key=question_id
        )


        if selected == "1":

            patient[question_id] = True

        elif selected == "2":

            patient[question_id] = False

        else:

            patient[question_id] = None


# =========================================================
# BMI
# =========================================================

weight = patient["weight"]

height = patient["height"]

bmi = calculate_bmi(
    weight,
    height
)

patient["bmi"] = bmi


# =========================================================
# BMI DISPLAY
# =========================================================

st.divider()

st.subheader("محاسبه شاخص توده بدنی (BMI)")

st.metric(
    "BMI",
    f"{bmi:.1f}"
)


# =========================================================
# BMI INTERPRETATION
# =========================================================

if bmi < 27:

    st.info(
        "BMI کمتر از 27 است."
    )

elif 27 <= bmi < 30:

    st.info(
        "BMI بین 27 تا 30 است؛ "
        "وجود بیماری‌های همراه مرتبط با وزن در تصمیم‌گیری اهمیت دارد."
    )

else:

    st.info(
        "BMI برابر یا بیشتر از 30 است."
    )


# =========================================================
# EVALUATION BUTTON
# =========================================================

if st.button(
    "شروع ارزیابی",
    type="primary"
):

    results = evaluate_patient(patient)


    # =====================================================
    # RESULTS
    # =====================================================

    st.divider()

    st.header(
        "نتیجه غربالگری اولیه"
    )


    for result in results.values():

        st.subheader(
            result["drug"]
        )


        # -------------------------------------------------
        # ELIGIBILITY
        # -------------------------------------------------

        eligibility = result["eligibility"]


        if eligibility == "ELIGIBLE":

            st.success(
                "✓ واجد معیار اولیه"
            )


        elif eligibility == "NOT_ELIGIBLE":

            st.warning(
                "معیار اولیه ورود به درمان دارویی وجود ندارد."
            )


        elif eligibility == "NEEDS_PHYSICIAN_REVIEW":

            st.warning(
                "⚠ نیازمند بررسی پزشک"
            )


        # -------------------------------------------------
        # SAFETY STATUS
        # -------------------------------------------------

        status = result["status"]


        if status == "CONTRAINDICATED":

            st.error(
                "✗ منع مصرف شناسایی شد"
            )


        elif status == "NOT_ELIGIBLE":

            st.warning(
                "معیار اولیه برای درمان دارویی کاهش وزن وجود ندارد."
            )


        elif status == "NEEDS_PHYSICIAN_REVIEW":

            st.warning(
                "⚠ نیازمند بررسی پزشک"
            )


        elif status == "NO_CLEAR_BARRIER":

            st.success(
                "✓ مانع واضحی در غربالگری اولیه پیدا نشد"
            )


        # -------------------------------------------------
        # REASONS
        # -------------------------------------------------

        if result["reasons"]:

            st.write(
                "**دلایل:**"
            )

            for reason in result["reasons"]:

                st.write(
                    f"• {reason}"
                )


        # -------------------------------------------------
        # FINAL MESSAGE
        # -------------------------------------------------

        if status == "NO_CLEAR_BARRIER":

            st.info(
                "این نتیجه به معنی تجویز یا تأیید نهایی دارو نیست. "
                "تصمیم نهایی باید توسط پزشک گرفته شود."
            )


        elif status == "NEEDS_PHYSICIAN_REVIEW":

            st.info(
                "اطلاعات موجود برای تصمیم‌گیری خودکار کافی نیست "
                "و بررسی پزشک لازم است."
            )


        elif status == "CONTRAINDICATED":

            st.info(
                "در غربالگری اولیه، یک یا چند مورد منع مصرف شناسایی شده است."
            )


        elif status == "NOT_ELIGIBLE":

            st.info(
                "بر اساس اطلاعات اولیه، معیار لازم برای ورود به درمان "
                "دارویی کاهش وزن وجود ندارد."
            )


        st.divider()


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "این ابزار برای غربالگری اولیه طراحی شده است و جایگزین "
    "ارزیابی، تشخیص و تجویز پزشک نیست."
)