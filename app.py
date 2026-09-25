import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("AI Nutrition Recommendation System")
st.write("Student Profile → Machine Learning → Recommendation")

data = pd.read_csv("students.csv")

# Fix empty values
data["food_preference"] = data["food_preference"].fillna("Vegetarian")
data["allergy"] = data["allergy"].fillna("None")
data["activity"] = data["activity"].fillna("Medium")

X = pd.get_dummies(
    data[["age", "food_preference", "allergy", "activity"]]
)

y = data["activity"].map({
    "High": "Protein-rich snack",
    "Medium": "Balanced snack",
    "Low": "Fruit + healthy snack"
})

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)


# ---------- Individual Student ----------
st.header("Student Profile")

student_name = st.selectbox(
    "Select Student",
    data["student"].tolist()
)

selected_student = data[
    data["student"] == student_name
].iloc[0]

age = int(selected_student["age"])
food_preference = str(selected_student["food_preference"])
allergy = str(selected_student["allergy"])
activity = str(selected_student["activity"])

st.write("Age:", age)
st.write("Food Preference:", food_preference)
st.write("Allergy:", allergy)
st.write("Activity Level:", activity)

if st.button("Get AI Recommendation"):

    new_student = pd.DataFrame([{
        "age": age,
        "food_preference": food_preference,
        "allergy": allergy,
        "activity": activity
    }])

    new_student = pd.get_dummies(new_student)

    new_student = new_student.reindex(
        columns=X.columns,
        fill_value=False
    )

    prediction = model.predict(new_student)[0]

    st.header("Student Report")

    st.write("Student:", student_name)
    st.write("Age:", age)
    st.write("Food Preference:", food_preference)
    st.write("Allergy:", allergy)
    st.write("Activity Level:", activity)

    if allergy != "None":
        st.warning(
            "Allergy Alert: Avoid foods containing "
            + str(allergy)
        )

    st.success(
        "AI Recommendation: " + str(prediction)
    )

    st.info(
        "This is an educational AI/ML demonstration, "
        "not a medical or clinical nutrition diagnosis."
    )


# ---------- 3 Students Comparison ----------
st.header("3 Students Comparison")

recommendations = []

for _, row in data.iterrows():

    student_data = pd.DataFrame([{
        "age": int(row["age"]),
        "food_preference": str(row["food_preference"]),
        "allergy": str(row["allergy"]),
        "activity": str(row["activity"])
    }])

    student_data = pd.get_dummies(student_data)

    student_data = student_data.reindex(
        columns=X.columns,
        fill_value=False
    )

    recommendation = model.predict(student_data)[0]

    recommendations.append(recommendation)


comparison = data.copy()

comparison["AI Recommendation"] = recommendations

st.dataframe(
    comparison[
        [
            "student",
            "age",
            "food_preference",
            "allergy",
            "activity",
            "AI Recommendation"
        ]
    ],
    use_container_width=True
)