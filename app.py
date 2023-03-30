from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Palm Puzzle Ventures", page_icon="🤓", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#Load Assets
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2imlehvj.json")
project_image_1 = Image.open("images/True Love.png")
project_image_2 = Image.open("images/Divine Help.png")
project_image_3 = Image.open("images/Youth Fellowship Program (Worship Experience) 1.png")
project_image_4 = Image.open("images/Human Rights.png")
project_image_5 = Image.open("images/We Glow Cropped.png")
project_image_6 = Image.open("images/For Peacceful Elections 1.png")


#Header Section
with st.container():
    st.subheader("Hello, Welcome To Palm Puzzle Ventures 👋")
    st.title("We are your one-stop-hub for all things design.")
    st.write("We aim to be the first option in your mind when you think of solving your design issues, whether for individuals, businesses of all sizes and governments.")
    st.write("[Learn More](https://instagram.com/palmpuzzle_graphics)")


#Services
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Do")
        st.write("##")
        st.write(
            """
            Palm Puzzle Ventures is an outfit set up to address the need for quality designs, both for prints and online distribution, not leaving out the creation of highly appealing and responsive websites.
            """
        )
        st.write("[Take a look at our catalogue to see what we are known for](https://instagram.com/palmpuzzle_graphics)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#Projects
with st.container():
    st.write("---")
    st.header("Our Projects")
    st.write("##")
    image_column_1, image_column_2, image_column_3 = st.columns(3)
    with image_column_1:
        st.image(project_image_1)
    with image_column_2:
        st.image(project_image_2)
    with image_column_3:
        st.image(project_image_3)
with st.container():
    #st.write("---")
    #st.write("##")
    image_column_1, image_column_2, image_column_3 = st.columns(3)
    with image_column_1:
        st.image(project_image_4)
    with image_column_2:
        st.image(project_image_5)
    with image_column_3:
        st.image(project_image_6)


#Contact Us
with st.container():
    st.write("---")
    st.header("Send Us A Message")

    contact_form = """
    <form action="https://formsubmit.co/75a2a1f9e41d497cd8395d4f87a39bfb" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email Address" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

