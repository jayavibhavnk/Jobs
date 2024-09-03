import streamlit as st

# Set the title of the app
st.title("Cover Letter Editor")

# Step 1: Select the role
st.header("Step 1: Select Role")
role = st.radio(
    "Choose the type of role you're applying for:",
    ("Data Roles", "SDE Roles")
)

# Step 2: Upload your resume
st.header("Step 2: Upload Your Resumes")
st.write("Please upload your resumes in text format.")

resume1 = st.text_area("Resume 1", height=300)
resume2 = st.text_area("Resume 2", height=300)

# Step 3: Add extra details about yourself
st.header("Step 3: Add Extra Details")
extra_details = st.text_area("Additional details about yourself, your work, projects, etc.", height=200)

# Step 4: Job Description and Extra Fields
st.header("Step 4: Job Description and Extra Fields")
job_description = st.text_area("Job Description", height=200)
extra_fields = st.text_area("Any extra fields you want to include", height=100)

# Step 5: Customize the Cover Letter
st.header("Step 5: Customize Your Cover Letter")
num_words = st.slider("Desired number of words:", 100, 1000, 500)
tone = st.selectbox("Select the tone of the cover letter:", ["Formal", "Informal", "Neutral", "Enthusiastic"])

# Step 6: Submit
if st.button("Submit"):
    st.success("Cover letter customization options have been submitted. Processing will be handled separately.")
