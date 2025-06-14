import streamlit as st
import json

# Load mock aid data
with open("data/mock_aid_listings.json") as f:
    aid_data = json.load(f)

st.set_page_config(page_title="Ode - Emergency Aid Dashboard", layout="centered")
st.title("🛟 Ode: One Dashboard for Emergency Help")
st.markdown("Get connected to **money**, **rides**, **shelter**, and **gig work** fast.")

# User inputs
location = st.text_input("📍 Enter your ZIP code or City", placeholder="e.g. 60601 or Chicago, IL")
selected_needs = st.multiselect(
    "What kind of help do you need right now?",
    ["💰 Money", "🚗 Ride", "🛏️ Shelter", "💼 Work"],
    default=["💰 Money", "🛏️ Shelter"]
)

# Display results
if st.button("🔍 Find Resources"):
    if not location:
        st.warning("Please enter a location to begin.")
    else:
        st.success(f"Showing help near: **{location}**")
        for category in selected_needs:
            st.subheader(category)
            for res in aid_data.get(category, []):
                st.markdown(f"""
                **{res['name']}**  
                📝 {res['description']}  
                🔗 [Visit]({res['link']})
                """)
else:
    st.info("Enter a location and select what you need, then click 'Find Resources'.")