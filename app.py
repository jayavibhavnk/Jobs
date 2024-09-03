import streamlit as st
import time
from openai import OpenAI
client = OpenAI()

OPENAI_API_KEY = st.secrets.OPENAI_API_KEY

# Function to query OpenAI
def query_openai(query):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": query}
    ],
    n = 1
    )

    return(completion.choices[0].message.content)

# Function to create the initial prompt
def create_prompt_1(resume, extra_details, job_description, extra_fields, num_words):
    prompt = f"""
    You are an expert at crafting cover letters. You will be given my resume, information about me, and the job role and details about the job.
    Using the input provided, craft a cover letter that is simple and formal. Avoid using fancy English unless asked to. Focus on my work and how it relates to the job description.
    Here are your inputs:
    Resume: {resume}
    About Myself: {extra_details}
    Job Description: {job_description}
    Extra_Instructions: {extra_fields}
    Number of words: {num_words}
    """
    return prompt

# Function to create the modified prompt
def create_prompt_2(resume, extra_details, job_description, extra_fields, num_words, cover_letter, new_instruction):
    prompt = f"""
    You are an expert at crafting cover letters. You will be given my resume, information about me, and the job role and details about the job.
    Using the input provided, craft a cover letter that is simple and formal. Avoid using fancy English unless asked to. Focus on my work and how it relates to the job description.
    Try to write it like a human—simple English and to the point.
    Here are your inputs:
    Resume: {resume}
    About Myself: {extra_details}
    Job Description: {job_description}
    Extra_Instructions: {extra_fields}
    Number of words: {num_words}

    Here is the cover letter you generated using the previous instructions: {cover_letter}

    Now, using the new instruction: {new_instruction}

    Generate a new cover letter.
    """
    return prompt

# Set the title of the app
st.title("Jv's Cover Letter Editor")

# Step 1: Select the role
st.header("Step 1: Select Role")
role = st.radio(
    "Choose the type of role you're applying for:",
    ("Data Roles", "SDE Roles")
)

# Step 2: Load your resume
# st.header("Step 2: Loading your Resumes...")
resume1 = open('Jayavibhav_sde.txt', 'r').read()
resume2 = open('Jayavibhav_data.txt', 'r').read()

resume = resume1 if role == 'SDE Roles' else resume2

# if resume:
#     st.write("Loaded!")

# Step 3: Add extra details about yourself
# st.header("Step 3: Add Extra Details")
extra_details = open('extra_details.txt', 'r').read()

# Step 2: Job Description and Extra Fields
st.header("Step 2: Job Description and Extra Fields")
job_description = st.text_area("Job Description", height=200)
extra_fields = st.text_area("Any extra fields you want to include", height=100)

# Step 3: Customize the Cover Letter
st.header("Step 3: Customize Your Cover Letter")
num_words = st.slider("Desired number of words:", 100, 1000, 500)

# Initialize session state for storing the generated cover letter
if 'cover_letter' not in st.session_state:
    st.session_state['cover_letter'] = ''

# Step 6: Submit
if st.button("Submit"):
    with st.spinner("Processing... Please wait."):
        prompt = create_prompt_1(resume, extra_details, job_description, extra_fields, num_words)
        st.session_state.cover_letter = query_openai(prompt)

    st.success("Processing complete!")
    st.write(st.session_state.cover_letter)

    # Option to modify the cover letter
    modify = st.radio("Would you like to modify the cover letter?", ("No", "Yes"))

    if modify == "Yes":
        st.header("Modify Your Cover Letter")
        modification_text = st.text_area("Enter modifications to your cover letter:", height=200)

        if st.button("Submit Modifications"):
            with st.spinner("Applying modifications... Please wait."):
                prompt1 = create_prompt_2(resume, extra_details, job_description, extra_fields, num_words, st.session_state.cover_letter, modification_text)
                st.session_state.cover_letter = query_openai(prompt1)

            st.success("Modifications done!")
            st.write(st.session_state.cover_letter)
