import streamlit as st
from openai import OpenAI

# ---- Planet Fitness Equipment List ----
PF_EQUIPMENT = {
    "Cardio": [
        "Treadmill",
        "Elliptical",
        "Stationary Bike",
        "Stair Climber",
        "Rowing Machine",
    ],
    "Strength Machines": [
        "Smith Machine",
        "Cable Machine",
        "Chest Press Machine",
        "Shoulder Press Machine",
        "Lat Pulldown Machine",
        "Seated Cable Row",
        "Leg Press Machine",
        "Leg Curl Machine",
        "Leg Extension Machine",
        "Hip Abductor / Adductor Machine",
        "Pec Deck / Fly Machine",
        "Assisted Pull-up / Dip Machine",
        "Ab Crunch Machine",
        "Back Extension Machine",
    ],
    "Free Weights": [
        "Dumbbells (up to 75 lbs)",
        "EZ Curl Bar",
    ],
    "Other": [
        "Resistance Bands",
        "Medicine Ball",
        "Stability Ball",
    ],
}

# ---- Streamlit UI ----
st.title("💪 AI Workout Generator")
st.write("Get a personalized workout using equipment available at Planet Fitness.")

api_key = st.text_input("OpenAI API Key", type="password", placeholder="sk-...")

time = st.number_input("How many minutes can you work out?", min_value=5, max_value=60, value=30)
level = st.selectbox("Select your fitness level", ["Beginner", "Intermediate", "Advanced"])

st.subheader("Select Available Equipment")
st.caption("Choose the machines / equipment you want to use today.")

selected_equipment = []
for category, items in PF_EQUIPMENT.items():
    st.markdown(f"**{category}**")
    cols = st.columns(2)
    for i, item in enumerate(items):
        if cols[i % 2].checkbox(item, key=item):
            selected_equipment.append(item)

if st.button("Generate Workout"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not selected_equipment:
        st.warning("Please select at least one piece of equipment.")
    else:
        equipment_list = ", ".join(selected_equipment)
        prompt = (
            f"Create a {time}-minute {level} workout using only the following Planet Fitness equipment: "
            f"{equipment_list}. "
            f"Include a warm-up, main exercises with sets/reps or duration, and a cool-down. "
            f"Do not suggest any equipment not in the list."
        )

        with st.spinner("Generating your workout..."):
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )

        workout_plan = response.choices[0].message.content
        st.subheader("Your Workout Plan")
        st.write(workout_plan)
