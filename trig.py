import streamlit as st
import math
from random import choice

# Page setup
st.set_page_config(page_title="TrigPrep", page_icon="📐", layout="centered")

# Reference values for common angles (in degrees)
SINE_VALUES = {
    0: 0.0,
    30: 0.5,
    45: math.sqrt(2) / 2,
    60: math.sqrt(3) / 2,
    90: 1.0,
}

COSINE_VALUES = {
    0: 1.0,
    30: math.sqrt(3) / 2,
    45: math.sqrt(2) / 2,
    60: 0.5,
    90: 0.0,
}

# Do not include 90° for tangent (undefined)
TANGENT_VALUES = {
    0: 0.0,
    30: 1 / math.sqrt(3),
    45: 1.0,
    60: math.sqrt(3),
}

TRIG_VALUES = {
    "Sine": SINE_VALUES,
    "Cosine": COSINE_VALUES,
    "Tangent": TANGENT_VALUES,
}

TRIG_LATEX = {"Sine": "\\sin", "Cosine": "\\cos", "Tangent": "\\tan"}


def ensure_session_defaults(function_name: str, num_questions: int, decimals: int) -> None:
    if "started" not in st.session_state:
        st.session_state.started = False
    if "mode" not in st.session_state:
        st.session_state.mode = function_name
    if "num_questions" not in st.session_state:
        st.session_state.num_questions = num_questions
    if "decimals" not in st.session_state:
        st.session_state.decimals = decimals
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "current_angle" not in st.session_state:
        st.session_state.current_angle = choice(list(TRIG_VALUES[function_name].keys()))
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "last_correct" not in st.session_state:
        st.session_state.last_correct = False


def reset_quiz(function_name: str, num_questions: int, decimals: int) -> None:
    st.session_state.started = True
    st.session_state.mode = function_name
    st.session_state.num_questions = num_questions
    st.session_state.decimals = decimals
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.current_angle = choice(list(TRIG_VALUES[function_name].keys()))
    st.session_state.submitted = False
    st.session_state.last_correct = False
    st.session_state.answer_input = 0.0


def next_question() -> None:
    st.session_state.question_index += 1
    if st.session_state.question_index < st.session_state.num_questions:
        st.session_state.current_angle = choice(list(TRIG_VALUES[st.session_state.mode].keys()))
        st.session_state.submitted = False
        st.session_state.last_correct = False
        st.session_state.answer_input = 0.0


def check_answer(user_answer: float, correct_value: float, decimals: int) -> bool:
    # Accept answers within 10^(-decimals)
    tolerance = 10 ** (-decimals)
    return math.isclose(float(user_answer), float(correct_value), rel_tol=0.0, abs_tol=tolerance)


# Sidebar controls
st.sidebar.title("Practice Options")
function_name = st.sidebar.selectbox("Choose a function:", list(TRIG_VALUES.keys()))
num_questions = st.sidebar.slider("Number of questions", min_value=1, max_value=20, value=5)
decimals = st.sidebar.slider("Answer tolerance (decimal places)", min_value=0, max_value=5, value=3)

ensure_session_defaults(function_name, num_questions, decimals)

start_reset = st.sidebar.button("Start / Reset", use_container_width=True)
if start_reset:
    reset_quiz(function_name, num_questions, decimals)


# Main UI
st.title("📐 Trigonometry Practice")
st.caption("Practice common trig ratios with instant feedback.")

if not st.session_state.started:
    st.markdown(
        "Use the options in the sidebar to pick a trig function, number of questions, and tolerance."
    )
else:
    total = st.session_state.num_questions
    index = st.session_state.question_index
    score = st.session_state.score
    progress = int((index / total) * 100) if total > 0 else 0

    st.progress(progress)
    st.write(f"Question {min(index + 1, total)} of {total} • Score: {score}")

    if index >= total:
        st.subheader("All done!")
        st.success(f"Your score: {score} / {total} ({round(100 * score / total, 1)}%)")
        if st.button("Play again", type="primary"):
            reset_quiz(function_name, num_questions, decimals)
    else:
        angle = st.session_state.current_angle
        values = TRIG_VALUES[st.session_state.mode]
        correct_value = values[angle]
        latex_name = TRIG_LATEX[st.session_state.mode]

        st.latex(f"{latex_name}({angle}^\\circ) = ")

        # Answer input
        st.number_input(
            "Your answer (decimal number)",
            key="answer_input",
            step=0.01,
            format="%f",
        )

        if not st.session_state.submitted:
            if st.button("Submit answer", type="primary"):
                is_correct = check_answer(st.session_state.answer_input, correct_value, st.session_state.decimals)
                st.session_state.last_correct = is_correct
                if is_correct:
                    st.session_state.score += 1
                st.session_state.submitted = True

        else:
            if st.session_state.last_correct:
                st.success("Correct!")
            else:
                st.error(f"Not quite. Correct value ≈ {round(correct_value, st.session_state.decimals)}")

            if st.button("Next question"):
                next_question()


with st.expander("Reference table for common angles"):
    rows = []
    for angle in sorted({*SINE_VALUES.keys(), *COSINE_VALUES.keys(), *TANGENT_VALUES.keys()}):
        sine_val = SINE_VALUES.get(angle, "-")
        cosine_val = COSINE_VALUES.get(angle, "-")
        tangent_val = TANGENT_VALUES.get(angle, "-")
        rows.append(
            {
                "Angle (°)": angle,
                "sin": None if sine_val == "-" else round(float(sine_val), 5),
                "cos": None if cosine_val == "-" else round(float(cosine_val), 5),
                "tan": "undefined" if tangent_val == "-" else (round(float(tangent_val), 5)),
            }
        )
    st.table(rows)

