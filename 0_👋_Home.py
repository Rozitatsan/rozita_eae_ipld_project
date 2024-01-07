
import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Rozita's Portfolio",
    page_icon="📊",
)




# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** <Your Name>")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Welcome! My name is Rozita
         </h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "thinking.png"  
     # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "I am currently a Master's Student at EAE Business School, currently enrolled in Big Data & Analytics and pursuing the understanding of the financial and technological side of the business world :)"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")



# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 Engrossed in the pursuit of my Master's degree within the distinguished halls of EAE Business School, delving into the intricate domain of big data and analytics.

- 🛩️ Having successfully navigated the academic seas, having earned my bachelor's degree in Business Management. Throughout my studies, I delved into the multifaceted realms of business strategy, organizational behavior, and financial management, sculpting a foundation of comprehensive knowledge in the intricate landscape of business management.

- ❤️ I love to read, paint, and dance. Books take me to different worlds, painting lets me express my creativity, and dancing is my way of enjoying the rhythm of life.

- 🤖 I am presently engrossed in multiple personal projects, with a particular emphasis on advancing my proficiency in Python. This endeavor holds significant importance to me, as I aspire to translate these enhanced skills into tangible and impactful real-world applications.


- 📫 How to reach me:[Email] (rozitatsangaris@gmail.com) [LinkedIn](https://www.linkedin.com/in/rozita-tsangari-79a1961b9/) [Instagram](https://www.instagram.com/rozitatsan/)

- 🏠 Living in Barcelona but with roots all over the world
""")



