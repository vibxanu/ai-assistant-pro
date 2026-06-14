import streamlit as st
from summaries import summarize
from quiz_generator import generate_quiz
from question_generator import generate_questions
from planner import generate_plan
from io import BytesIO
from reportlab.pdfgen import canvas
import re

# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    return re.sub(r'[^\x00-\x7F]+', '', str(text))

# ---------------- PAGE ----------------
st.set_page_config(page_title="AI Assistant Pro", layout="wide")

st.markdown("""
<style>

/* ---------------- BACKGROUND ---------------- */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0b1220);
    color: white;
    transition: all 0.5s ease-in-out;
}
h2 {
    margin-bottom: 0px;
}
/* ---------------- HEADINGS ---------------- */
h1, h2, h3 {
    color: #38bdf8 !important;
    font-weight: 700;
    text-shadow: 0px 0px 10px rgba(56,189,248,0.4);
    transition: 0.3s ease-in-out;
}

/* ---------------- INPUT ---------------- */
div[data-baseweb="input"] input {
    background-color: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    transition: 0.3s ease-in-out;
}

div[data-baseweb="input"] input:focus {
    border: 1px solid #38bdf8 !important;
    box-shadow: 0px 0px 12px rgba(56,189,248,0.4);
    transform: scale(1.01);
}

/* ---------------- BUTTONS ---------------- */
.stButton button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    transition: all 0.3s ease-in-out;
    border: none;
}

.stButton button:hover {
    transform: translateY(-2px) scale(1.05);
    box-shadow: 0px 8px 20px rgba(56,189,248,0.3);
}

/* ---------------- SIDEBAR ---------------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1220, #111827);
    padding: 10px;
    transition: all 0.4s ease-in-out;
}

/* Sidebar headings with ICON STYLE */
section[data-testid="stSidebar"] h1 {
    font-size: 18px !important;
    color: #38bdf8 !important;
    text-align: left !important;
}

section[data-testid="stSidebar"] h2 {
    font-size: 15px !important;
    color: #60a5fa !important;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Study Planner ICON */
section[data-testid="stSidebar"] h2:contains("Study Planner")::before {
    content: "📚 ";
}

/* History ICON */
section[data-testid="stSidebar"] h2:contains("History")::before {
    content: "🕘 ";
}

/* Sidebar buttons (history items) */
section[data-testid="stSidebar"] .stButton button {
    width: 100%;
    padding: 6px 10px !important;
    font-size: 12px !important;
    border-radius: 8px !important;
    margin-bottom: 5px !important;
    background: rgba(56,189,248,0.12);
    border: 1px solid rgba(56,189,248,0.25);
    color: white;
    transition: all 0.3s ease-in-out;
}

/* Sidebar hover animation */
section[data-testid="stSidebar"] .stButton button:hover {
    background: rgba(56,189,248,0.35);
    transform: translateX(5px);
}

/* ---------------- SUCCESS BOX ---------------- */
.stSuccess {
    background-color: rgba(34,197,94,0.15) !important;
    border-left: 5px solid #22c55e;
    transition: 0.3s;
}

/* ---------------- RADIO ---------------- */
div[role="radiogroup"] label {
    background-color: rgba(255,255,255,0.05);
    padding: 6px;
    border-radius: 8px;
    transition: 0.2s;
}

div[role="radiogroup"] label:hover {
    background-color: rgba(56,189,248,0.2);
    transform: scale(1.02);
}

/* ---------------- DOWNLOAD BUTTON ---------------- */
.stDownloadButton button {
    background: linear-gradient(90deg, #10b981, #38bdf8);
    color: white;
    border-radius: 10px;
    transition: 0.3s ease-in-out;
}

.stDownloadButton button:hover {
    transform: scale(1.05);
}

/* ---------------- PAGE ANIMATION ---------------- */
.block-container {
    animation: fadeIn 0.6s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ---------------- REMOVE FOOTER ---------------- */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
# ---------------- STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "show_result" not in st.session_state:
    st.session_state.show_result = False

if "active_topic" not in st.session_state:
    st.session_state.active_topic = ""

if "show_mcq" not in st.session_state:
    st.session_state.show_mcq = False

if "show_q" not in st.session_state:
    st.session_state.show_q = False

if "score" not in st.session_state:
    st.session_state.score = 0
# ---------------- HEADER ----------------

col1, col2 = st.columns([1, 6])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=70)

with col2:
    st.markdown("## 🤖 AI Assistant Pro")
    

# ---------------- INPUT ----------------
st.markdown("<br><br>", unsafe_allow_html=True)
user_input = st.text_input("Enter your topic")

# ---------------- GENERATE ----------------
if st.button("Generate") and user_input:
    st.session_state.active_topic = user_input
    st.session_state.show_result = True
    st.session_state.show_mcq = False
    st.session_state.show_q = False
    st.session_state.score = 0

    st.session_state.summary = summarize(user_input)
    st.session_state.mcq = generate_quiz(user_input)
    st.session_state.questions = generate_questions(user_input)
    st.session_state.plan = generate_plan(user_input)

    if user_input not in st.session_state.history:
        st.session_state.history.append(user_input)

# ---------------- OUTPUT ----------------

if st.session_state.show_result:

    st.markdown("## Answer")
    st.success(st.session_state.summary)

    # ---------------- SEPARATOR LINE ----------------
    st.markdown("---")

    # ---------------- BUTTON ROW ----------------
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("MCQs"):
            st.session_state.show_mcq = True
            st.session_state.show_q = False

    with col2:
        if st.button("Questions"):
            st.session_state.show_q = True
            st.session_state.show_mcq = False

    # ---------------- PDF ----------------
    with col3:
        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 800, "AI Assistant Pro Report")

        p.setFont("Helvetica", 12)
        p.drawString(100, 770, f"Topic: {st.session_state.active_topic}")

        summary = clean_text(st.session_state.summary)

        p.setFont("Helvetica-Bold", 12)
        p.drawString(100, 740, "Summary:")

        p.setFont("Helvetica", 10)
        p.drawString(100, 720, summary[:200])

        p.setFont("Helvetica-Bold", 12)
        p.drawString(100, 690, f"Score: {st.session_state.score}/{len(st.session_state.mcq)}")

        # MCQs
        y = 660
        p.setFont("Helvetica-Bold", 12)
        p.drawString(100, y, "MCQs:")
        y -= 20

        for i, q in enumerate(st.session_state.mcq, start=1):
            p.setFont("Helvetica", 9)
            p.drawString(100, y, f"{i}. {q['q']}")
            y -= 15

        # Questions
        y -= 10
        p.setFont("Helvetica-Bold", 12)
        p.drawString(100, y, "Questions:")
        y -= 20

        for i, q in enumerate(st.session_state.questions, start=1):
            p.setFont("Helvetica", 9)
            p.drawString(100, y, f"{i}. {q}")
            y -= 15

        # Footer
        p.setFont("Helvetica-Bold", 10)
        p.drawString(100, 50, "AI Assistant Pro | Study Planner System")

        p.save()
        buffer.seek(0)

        st.download_button(
            "Download Report",
            buffer,
            file_name="AI_Assistant_Report.pdf",
            mime="application/pdf"
        )

# ---------------- MCQs ----------------
if st.session_state.show_mcq:
    st.markdown("### MCQs")

    score = 0

    for i, q in enumerate(st.session_state.mcq, start=1):
        st.write(f"{i}. {q['q']}")

        selected = st.radio("Select option:", q["options"], key=f"mcq_{i}")

        if selected == q["ans"]:
            score += 1

    if st.button("Submit Quiz"):
        st.session_state.score = score
        st.success(f"Score: {score}/{len(st.session_state.mcq)}")

# ---------------- QUESTIONS ----------------
if st.session_state.show_q:
    st.markdown("### Questions")

    for i, q in enumerate(st.session_state.questions, start=1):
        st.write(f"{i}. {q}")

# ---------------- SIDEBAR ----------------

col1, col2 = st.sidebar.columns([1, 4])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=45
    )

with col2:
    st.markdown("## Study Planner")
st.sidebar.markdown(" ")
if st.sidebar.button("📖 View Plan"):
    for i, p in enumerate(st.session_state.plan, start=1):
        st.sidebar.write(f"📌 {i}. {p}")

st.sidebar.markdown("---")

col1, col2 = st.sidebar.columns([1, 4])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2921/2921222.png",
        width=40
    )

with col2:
    st.markdown("## History")




for h in reversed(st.session_state.history[-10:]):
    if st.sidebar.button(f"📘 {h}"):
        st.session_state.active_topic = h
        st.session_state.show_result = True
        st.session_state.summary = summarize(h)
        st.session_state.mcq = generate_quiz(h)
        st.session_state.questions = generate_questions(h)
        st.session_state.plan = generate_plan(h)