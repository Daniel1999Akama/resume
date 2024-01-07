from pathlib import Path
import streamlit as st
from PIL import Image

#----Path settings---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "101.jpg"

#----General settings---

page_title = "Digital CV | Daniel Akama Nyamweya"
page_icon = ":wave"
name = "Daniel Akama Nyamweya"
Description = """
Competent Data scientist and IT professional looking to aid businesses in improving their
services through insightful data related projects resulting in actionable recommendations. 
"""
email = "danielakama23@gmail.com"
social_media = {
    "Linkedin": "https://www.linkedin.com/in/danielakamanyamweya/",
    "Github": "https://github.com/Daniel1999Akama/"
}

projects = {
    "🏆Twitter Sentiment Analysis - twitter data analysis":"https://github.com/Daniel1999Akama/moringa_phase4_project",
    "🏆Customer Churn Analysis - model that predicts likelihood of customer churn":"https://github.com/Daniel1999Akama/moringa_phase3_project",
    "🏆Swahili news classifier - swahili news classification":"https://github.com/Daniel1999Akama/News-Classification"
}

st.set_page_config(page_title=page_title, page_icon=page_icon)


#---load CSS, PDF and profile pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#---- Hero section---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(name)
    st.write(Description)
    st.download_button(
        label=" 📜 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", email)


#---social links---
st.write("#")
cols = st.columns(len(social_media))
for i, (platform, link) in enumerate(social_media.items()):
    cols[i].write(f"[{platform}]({link})")


#--------Experience and qualifications---

st.write("#")
st.subheader("Experience and Qualifications")
st.write(
    """
    - ✅ 3 years experience extracting actionable insights from data
    - ✅ Strong hands on experience and knowledge in python and excel
    - ✅ Good understanding of statistical principles and their respective applications.
    - ✅ Excellent team-player and displaying strong sense of initiative on tasks.
    """
)


#--- Skills---

st.write("#")
st.subheader("Hard skills")
st.write(
    """
    - 🧑🏾‍💻 Programming: Python(Scikit-learn, Pandas), SQL
    - 📊 Data Visualization: PowerBi, Ms Excel, Plotly
    - 📔 Modeling: Machine learning (Supervised and unsupervised models)
    - 🚪 Databases: MongoDB, SQLite, MySQL 
    """
)

#----Work history---

st.write("#")
st.subheader("Work History")
st.write("---")

#---Job1---
st.write("🖥️", "**ICT Attache | National Construction Authority**")
st.write("05/2022 - 08/2022")
st.write(
    """
    - > Carrying out preventive maintenance on office ICT equipments. This involved
    ensuring the ICT equipment was properly functioning.
    - > Assisting with software installations and configurations.
    - > Setting up computer workstations.
    - > Troubleshooting system and network problems, diagnosing and solving hardware and software
    faults.
    - > Provided basic user support to other departments.
""")


#----Projects and accomplishments---
st.write("#")
st.subheader("Projects and accomplishments")
st.write("---")
for project, link in projects.items():
    st.write(f"[{project}]({link})")






