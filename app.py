import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Nutrition Recommendation System",
    layout="wide"
)

st.title("🥗 AI Nutrition Recommendation System")
st.write("Student Profile → Daily Health Data → AI Recommendation")


# ---------------- AI RECOMMENDATION ----------------
def get_ai_recommendation(activity, wellbeing, allergy):

    # Allergy safety first
    if allergy == "Milk":
        if activity == "High":
            return "Sprouts + Dal + Fruit (Milk avoided)"
        else:
            return "Fruit + Sprouts + Dal (Milk avoided)"

    if allergy == "Nuts":
        if activity == "High":
            return "Paneer + Roti + Fruit (Nuts avoided)"
        else:
            return "Dal + Rice + Fruit (Nuts avoided)"

    # Activity + Well-being based recommendation
    if activity == "High":
        if wellbeing == "Average":
            return "Protein-rich Snack + Fruit"
        else:
            return "Paneer + Roti + Fruit"

    if activity == "Medium":
        if wellbeing == "Average":
            return "Dal + Rice + Fruit"
        else:
            return "Dal + Roti + Fruit"

    if activity == "Low":
        if wellbeing == "Average":
            return "Fruit + Milk"
        else:
            return "Sprouts + Fruit"

    return "Balanced Nutritious Meal"


# ---------------- 25 STUDENT RECORDS ----------------
data = [
    ["S001", "Jit", "Day 1", "High", "Vegetarian", "None", "Good"],
    ["S001", "Jit", "Day 2", "Medium", "Vegetarian", "None", "Average"],
    ["S001", "Jit", "Day 3", "High", "Vegetarian", "Nuts", "Good"],
    ["S001", "Jit", "Day 4", "Low", "Vegetarian", "None", "Very Good"],
    ["S001", "Jit", "Day 5", "Medium", "Vegetarian", "None", "Good"],

    ["S002", "Yash", "Day 1", "Medium", "Vegetarian", "Milk", "Good"],
    ["S002", "Yash", "Day 2", "High", "Vegetarian", "None", "Very Good"],
    ["S002", "Yash", "Day 3", "Low", "Vegetarian", "None", "Average"],
    ["S002", "Yash", "Day 4", "Medium", "Vegetarian", "Nuts", "Good"],
    ["S002", "Yash", "Day 5", "High", "Vegetarian", "None", "Good"],

    ["S003", "Dipali", "Day 1", "Low", "Vegetarian", "None", "Average"],
    ["S003", "Dipali", "Day 2", "Medium", "Vegetarian", "None", "Good"],
    ["S003", "Dipali", "Day 3", "High", "Vegetarian", "Milk", "Good"],
    ["S003", "Dipali", "Day 4", "Medium", "Vegetarian", "None", "Very Good"],
    ["S003", "Dipali", "Day 5", "Low", "Vegetarian", "None", "Good"],

    ["S004", "Urvika", "Day 1", "High", "Vegetarian", "None", "Very Good"],
    ["S004", "Urvika", "Day 2", "Low", "Vegetarian", "Nuts", "Average"],
    ["S004", "Urvika", "Day 3", "Medium", "Vegetarian", "None", "Good"],
    ["S004", "Urvika", "Day 4", "High", "Vegetarian", "None", "Good"],
    ["S004", "Urvika", "Day 5", "Medium", "Vegetarian", "Milk", "Very Good"],

    ["S005", "Jatin", "Day 1", "Medium", "Vegetarian", "None", "Good"],
    ["S005", "Jatin", "Day 2", "High", "Vegetarian", "None", "Average"],
    ["S005", "Jatin", "Day 3", "Low", "Vegetarian", "Milk", "Good"],
    ["S005", "Jatin", "Day 4", "Medium", "Vegetarian", "None", "Very Good"],
    ["S005", "Jatin", "Day 5", "High", "Vegetarian", "Nuts", "Good"],
]

df = pd.DataFrame(
    data,
    columns=[
        "Student Code",
        "Student",
        "Day",
        "Activity",
        "Food Preference",
        "Allergy",
        "Well-being"
    ]
)

df["AI Recommendation"] = df.apply(
    lambda row: get_ai_recommendation(
        row["Activity"],
        row["Well-being"],
        row["Allergy"]
    ),
    axis=1
)


# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "🏠 AI Dashboard",
        "👨‍🎓 Student Profile",
        "📅 5-Day Student Data",
        "🤖 Live AI Recommendation",
        "📊 Daily AI History",
        "⚠️ Allergy Safety",
        "👥 Student Comparison"
    ]
)


# ---------------- DASHBOARD ----------------
if page == "🏠 AI Dashboard":

    st.header("🏠 AI Nutrition Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", "5")
    col2.metric("Total Records", "25")
    col3.metric("Days Recorded", "5")
    col4.metric(
        "Allergy Records",
        str(len(df[df["Allergy"] != "None"]))
    )

    st.subheader("🔍 How the System Works")

    st.write(
        "Daily student information is collected for Activity, "
        "Well-being, Food Preference and Allergy."
    )

    st.write(
        "The AI decision system analyses these inputs and provides "
        "a suitable nutrition recommendation."
    )

    st.subheader("📋 Complete Student Data")
    st.dataframe(df, use_container_width=True)


# ---------------- STUDENT PROFILE ----------------
elif page == "👨‍🎓 Student Profile":

    st.header("👨‍🎓 Student 5-Day Profile")

    student = st.selectbox(
        "Select Student",
        df["Student"].unique()
    )

    student_data = df[df["Student"] == student]

    st.subheader(f"📅 {student} - 5 Day Report")

    st.dataframe(
        student_data,
        use_container_width=True
    )


# ---------------- 5 DAY DATA ----------------
elif page == "📅 5-Day Student Data":

    st.header("📅 5-Day Student Data")

    st.dataframe(
        df,
        use_container_width=True
    )


# ---------------- LIVE AI ----------------
elif page == "🤖 Live AI Recommendation":

    st.header("🤖 Live AI Nutrition Recommendation")

    st.write(
        "Enter today's student information and get an AI-based recommendation."
    )

    col1, col2 = st.columns(2)

    with col1:

        student = st.selectbox(
            "Student",
            ["Jit", "Yash", "Dipali", "Urvika", "Jatin"]
        )

        activity = st.selectbox(
            "Activity Level",
            ["Low", "Medium", "High"]
        )

        food_preference = st.selectbox(
            "Food Preference",
            ["Vegetarian"]
        )

    with col2:

        wellbeing = st.selectbox(
            "Well-being",
            ["Average", "Good", "Very Good"]
        )

        allergy = st.selectbox(
            "Allergy",
            ["None", "Milk", "Nuts"]
        )

    if st.button("🤖 Generate AI Recommendation"):

        recommendation = get_ai_recommendation(
            activity,
            wellbeing,
            allergy
        )

        st.success(
            f"🥗 AI Recommendation for {student}: {recommendation}"
        )

        if allergy != "None":

            st.warning(
                f"⚠️ Allergy Alert: {allergy} allergy detected. "
                f"The recommendation avoids the selected allergen."
            )

        st.info(
            "AI considers Activity + Well-being + Allergy "
            "to generate a safer nutrition recommendation."
        )


# ---------------- DAILY HISTORY ----------------
elif page == "📊 Daily AI History":

    st.header("📊 Daily AI Recommendation History")

    student = st.selectbox(
        "Select Student",
        df["Student"].unique()
    )

    history = df[df["Student"] == student]

    st.dataframe(
        history[
            [
                "Day",
                "Activity",
                "Food Preference",
                "Allergy",
                "Well-being",
                "AI Recommendation"
            ]
        ],
        use_container_width=True
    )


# ---------------- ALLERGY SAFETY ----------------
elif page == "⚠️ Allergy Safety":

    st.header("⚠️ Allergy Safety System")

    allergy_data = df[df["Allergy"] != "None"]

    if len(allergy_data) > 0:

        st.warning(
            "The system identifies students with food allergies "
            "and avoids the selected allergen in recommendations."
        )

        st.dataframe(
            allergy_data[
                [
                    "Student",
                    "Day",
                    "Allergy",
                    "Activity",
                    "Well-being",
                    "AI Recommendation"
                ]
            ],
            use_container_width=True
        )

    else:
        st.success("No allergy records found.")


# ---------------- COMPARISON ----------------
elif page == "👥 Student Comparison":

    st.header("👥 Student Comparison")

    comparison = pd.pivot_table(
        df,
        index="Student",
        columns="Day",
        values="AI Recommendation",
        aggfunc="first"
    )

    st.subheader("📊 Student-wise Daily Recommendations")

    st.dataframe(
        comparison,
        use_container_width=True
    )

    st.subheader("🥗 Recommendation Overview")

    st.dataframe(
        df[
            [
                "Student",
                "Day",
                "Activity",
                "Well-being",
                "Allergy",
                "AI Recommendation"
            ]
        ],
        use_container_width=True
    )
