import streamlit as st

st.set_page_config(page_title="Mental Health Depression Detector", layout="centered")

st.title("🧠 Mental Health Depression Detection")
st.markdown("Please fill out the form below to assess depression severity and get personalized recommendations.")

with st.form("mental_health_form"):
    st.markdown("### Demographic Information")
    age = st.slider("Age", 10, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    occupation = st.text_input("Occupation")
    location = st.text_input("Location")
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
    education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "Doctorate", "Other"])

    st.markdown("### Symptom Ratings (1 = None, 5 = Severe)")
    symptoms = {
        "Sleep Issue": st.slider("Sleep Issue", 1, 5),
        "Appetite Issue": st.slider("Appetite Issue", 1, 5),
        "Lack of Interest": st.slider("Lack of Interest", 1, 5),
        "Fatigue": st.slider("Fatigue", 1, 5),
        "Worthlessness": st.slider("Feelings of Worthlessness", 1, 5),
        "Concentration Issue": st.slider("Concentration Issue", 1, 5),
        "Agitation": st.slider("Agitation", 1, 5),
        "Suicidal Ideation": st.slider("Suicidal Ideation", 1, 5),
        "Sleep Disturbance": st.slider("Sleep Disturbance", 1, 5),
        "Aggression": st.slider("Aggression", 1, 5),
        "Panic Attacks": st.slider("Panic Attacks", 1, 5),
        "Hopelessness": st.slider("Hopelessness", 1, 5),
        "Restlessness": st.slider("Restlessness", 1, 5),
        "Low Energy": st.slider("Low Energy", 1, 5)
    }

    submit = st.form_submit_button("Predict Depression Severity")

if submit:
    total_score = sum(symptoms.values())
    if total_score < 35:
        severity = "Mild"
    elif total_score < 55:
        severity = "Moderate"
    else:
        severity = "Severe"

    st.subheader(f"🩺 Depression Severity: **{severity}**")
    st.markdown("### Recommendations:")

    if symptoms["Sleep Issue"] >= 4 or symptoms["Sleep Disturbance"] >= 4:
        st.write("- Establish a regular sleep routine. Limit caffeine and screen time before bed.")
    if symptoms["Suicidal Ideation"] >= 4:
        st.write("- Seek emergency mental health support or call a crisis hotline immediately.")
    if symptoms["Fatigue"] >= 4 or symptoms["Low Energy"] >= 4:
        st.write("- Light exercise and hydration can help restore energy.")
    if symptoms["Hopelessness"] >= 4 or symptoms["Worthlessness"] >= 4:
        st.write("- Talk to a counselor or therapist. Journaling may also help process emotions.")
    if symptoms["Panic Attacks"] >= 4:
        st.write("- Try deep breathing exercises and avoid caffeine.")
    if symptoms["Aggression"] >= 4:
        st.write("- Practice anger management techniques or speak to a therapist.")
    if symptoms["Appetite Issue"] >= 4:
        st.write("- Eat small meals regularly; consult a dietitian if needed.")
    if symptoms["Lack of Interest"] >= 4:
        st.write("- Start with small enjoyable activities, even if motivation is low.")
    if symptoms["Restlessness"] >= 4:
        st.write("- Try grounding techniques or engage in structured tasks.")
    if symptoms["Concentration Issue"] >= 4:
        st.write("- Use lists, reminders, and reduce multitasking.")

    st.write("- General Tip: Mindfulness, CBT techniques, and social support are very beneficial.")
