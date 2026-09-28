import streamlit as st

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="AI Career Recommendation System",
    page_icon="🎯",
    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* Main page */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #f8fafc);
}

/* Main content width */
.block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Main title */
.title {
    text-align: center;
    color: #1e3a8a !important;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #475569 !important;
    font-size: 18px;
    margin-bottom: 30px;
}

/* All normal text */
.stApp p {
    color: #1f2937 !important;
}

/* Labels */
.stApp label {
    color: #1e293b !important;
    font-weight: 600 !important;
}

/* Input boxes */
.stTextInput input {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 2px solid #cbd5e1 !important;
    border-radius: 10px !important;
}

/* Input placeholder */
.stTextInput input::placeholder {
    color: #64748b !important;
}

/* Select box */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 2px solid #cbd5e1 !important;
    border-radius: 10px !important;
}

/* Text inside select box */
.stSelectbox div[data-baseweb="select"] span {
    color: #111827 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed) !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 13px !important;
    margin-top: 15px;
}

/* Button hover */
.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8, #6d28d9) !important;
    color: white !important;
}

/* Headings */
.stApp h1,
.stApp h2,
.stApp h3 {
    color: #1e293b !important;
}

/* Success message */
div[data-testid="stAlert"] {
    color: #1f2937 !important;
}

/* Info result box */
div[data-testid="stAlert"] p {
    color: #1f2937 !important;
}

/* Result text */
.result-box {
    background: white;
    padding: 25px;
    border-radius: 15px;
    margin-top: 25px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    border-left: 6px solid #2563eb;
}

/* Learning path */
.learning-box {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

/* Learning path text */
.learning-box p {
    color: #334155 !important;
    font-size: 16px;
}

/* Profile */
.profile-box {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

.profile-box p {
    color: #334155 !important;
    font-size: 16px;
}

/* Divider */
hr {
    border: none;
    border-top: 2px solid #cbd5e1;
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    '<div class="title">🎯 AI Career Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover the right career based on your skills and interests'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# =========================
# USER INPUT
# =========================

name = st.text_input(
    "👤 Enter your name",
    placeholder="Enter your name"
)

education = st.selectbox(
    "🎓 Select your education",
    [
        "B.Tech / B.E",
        "B.Sc",
        "BCA",
        "MCA",
        "M.Tech",
        "Other"
    ]
)

skills = st.text_input(
    "💻 Enter your skills",
    placeholder="Example: Python, SQL, HTML"
)

interests = st.text_input(
    "❤️ Enter your interests",
    placeholder="Example: AI, Data Science, Web Development"
)

experience = st.selectbox(
    "📚 Select your experience level",
    [
        "Fresher",
        "Beginner",
        "Intermediate",
        "Experienced"
    ]
)


# =========================
# BUTTON
# =========================

if st.button("🔍 Recommend Career"):

    if (
        name.strip() == ""
        or skills.strip() == ""
        or interests.strip() == ""
    ):

        st.error(
            "❌ Please enter your name, skills and interests."
        )

    else:

        skills_lower = skills.lower()
        interests_lower = interests.lower()

        # =========================
        # CAREER RECOMMENDATION
        # =========================

        if (
            "python" in skills_lower
            and (
                "ai" in interests_lower
                or "machine learning" in interests_lower
                or "artificial intelligence" in interests_lower
            )
        ):

            career = "🤖 AI / Machine Learning Engineer"

            reason = (
                "Your Python skills and interest in AI or "
                "Machine Learning match this career."
            )

        elif (
            "python" in skills_lower
            and (
                "data" in interests_lower
                or "data science" in interests_lower
                or "analytics" in interests_lower
            )
        ):

            career = "📊 Data Scientist"

            reason = (
                "Your Python skills and interest in data "
                "match a Data Science career."
            )

        elif (
            "html" in skills_lower
            or "css" in skills_lower
            or "javascript" in skills_lower
            or "web" in interests_lower
        ):

            career = "🌐 Web Developer"

            reason = (
                "Your skills and interests match "
                "Web Development."
            )

        elif (
            "java" in skills_lower
            or "software" in interests_lower
            or "development" in interests_lower
        ):

            career = "💻 Software Developer"

            reason = (
                "Your programming skills and development "
                "interest match Software Development."
            )

        elif (
            "sql" in skills_lower
            or "database" in interests_lower
        ):

            career = "🗄️ Database Developer"

            reason = (
                "Your SQL or database interest matches "
                "Database Development."
            )

        elif (
            "cyber" in interests_lower
            or "security" in interests_lower
            or "networking" in skills_lower
        ):

            career = "🔐 Cyber Security Analyst"

            reason = (
                "Your interests or networking skills can "
                "be useful for Cyber Security."
            )

        else:

            career = "💻 Software Developer"

            reason = (
                "Software Development is a broad career "
                "option based on the information provided."
            )


        # =========================
        # RESULT
        # =========================

        st.success("✅ Career analysis completed!")

        st.markdown(
            f"""
            <div class="result-box">

            <h2 style="color:#1e3a8a !important;">
            🎯 Recommended Career
            </h2>

            <h3 style="color:#2563eb !important;">
            {career}
            </h3>

            <p style="color:#334155 !important;">
            {reason}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        # =========================
        # LEARNING PATH
        # =========================

        st.markdown(
            """
            <div class="learning-box">

            <h2 style="color:#1e3a8a !important;">
            🚀 Suggested Learning Path
            </h2>

            <p>1️⃣ Learn programming fundamentals</p>

            <p>2️⃣ Learn Data Structures and Algorithms</p>

            <p>3️⃣ Learn career-specific technologies</p>

            <p>4️⃣ Build real-world projects</p>

            <p>5️⃣ Create a strong resume</p>

            <p>6️⃣ Build your GitHub profile</p>

            <p>7️⃣ Practice technical interviews</p>

            <p>8️⃣ Apply for suitable jobs</p>

            </div>
            """,
            unsafe_allow_html=True
        )


        # =========================
        # USER PROFILE
        # =========================

        st.markdown(
            f"""
            <div class="profile-box">

            <h2 style="color:#1e3a8a !important;">
            📋 Your Profile
            </h2>

            <p>👤 <b>Name:</b> {name}</p>

            <p>🎓 <b>Education:</b> {education}</p>

            <p>💻 <b>Skills:</b> {skills}</p>

            <p>❤️ <b>Interests:</b> {interests}</p>

            <p>📚 <b>Experience:</b> {experience}</p>

            </div>
            """,
            unsafe_allow_html=True
        )
