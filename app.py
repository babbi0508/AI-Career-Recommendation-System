import streamlit as st

# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="AI Career Recommendation System",
    page_icon="🎯",
    layout="centered"
)


# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
}

.title {
    text-align: center;
    color: #1e3a8a;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 17px;
    margin-bottom: 30px;
}

.form-box {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.08);
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 12px;
    border: none;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# TITLE
# ==============================

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


# ==============================
# FORM
# ==============================

st.markdown(
    '<div class="form-box">',
    unsafe_allow_html=True
)

name = st.text_input(
    "👤 Enter your name"
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


# ==============================
# RECOMMENDATION BUTTON
# ==============================

if st.button("🔍 Recommend Career"):

    # Check required fields
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


        # ==============================
        # AI / MACHINE LEARNING
        # ==============================

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
                "Your Python skills and interest in "
                "AI or Machine Learning match this career."
            )


        # ==============================
        # DATA SCIENTIST
        # ==============================

        elif (
            "python" in skills_lower
            and (
                "data science" in interests_lower
                or "data" in interests_lower
                or "analytics" in interests_lower
            )
        ):

            career = "📊 Data Scientist"

            reason = (
                "Your Python skills and interest in "
                "data match a Data Science career."
            )


        # ==============================
        # WEB DEVELOPER
        # ==============================

        elif (
            "html" in skills_lower
            or "css" in skills_lower
            or "javascript" in skills_lower
            or "web" in interests_lower
        ):

            career = "🌐 Web Developer"

            reason = (
                "Your skills or interests are related "
                "to Web Development."
            )


        # ==============================
        # SOFTWARE DEVELOPER
        # ==============================

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


        # ==============================
        # DATABASE DEVELOPER
        # ==============================

        elif (
            "sql" in skills_lower
            or "database" in interests_lower
        ):

            career = "🗄️ Database Developer"

            reason = (
                "Your SQL or database interest matches "
                "Database Development."
            )


        # ==============================
        # CYBER SECURITY
        # ==============================

        elif (
            "cyber" in interests_lower
            or "security" in interests_lower
            or "networking" in skills_lower
        ):

            career = "🔐 Cyber Security Analyst"

            reason = (
                "Your interests or networking skills "
                "can be useful for Cyber Security."
            )


        # ==============================
        # DEFAULT CAREER
        # ==============================

        else:

            career = "💻 Software Developer"

            reason = (
                "Software Development is a broad career "
                "option based on the information provided."
            )


        # ==============================
        # RESULT
        # ==============================

        st.success(
            "✅ Career analysis completed!"
        )

        st.subheader(
            "🎯 Recommended Career"
        )

        st.info(
            career
        )

        st.write(
            reason
        )


        # ==============================
        # LEARNING PATH
        # ==============================

        st.subheader(
            "🚀 Suggested Learning Path"
        )

        st.write(
            "1️⃣ Learn programming fundamentals"
        )

        st.write(
            "2️⃣ Learn Data Structures and Algorithms"
        )

        st.write(
            "3️⃣ Learn career-specific technologies"
        )

        st.write(
            "4️⃣ Build real-world projects"
        )

        st.write(
            "5️⃣ Create a strong resume"
        )

        st.write(
            "6️⃣ Build your GitHub profile"
        )

        st.write(
            "7️⃣ Practice technical interviews"
        )

        st.write(
            "8️⃣ Apply for suitable jobs"
        )


        # ==============================
        # PROFILE
        # ==============================

        st.subheader(
            "📋 Your Profile"
        )

        st.write(
            "👤 Name:",
            name
        )

        st.write(
            "🎓 Education:",
            education
        )

        st.write(
            "💻 Skills:",
            skills
        )

        st.write(
            "❤️ Interests:",
            interests
        )

        st.write(
            "📚 Experience:",
            experience
        )


# ==============================
# CLOSE FORM
# ==============================

st.markdown(
    "</div>",
    unsafe_allow_html=True
)