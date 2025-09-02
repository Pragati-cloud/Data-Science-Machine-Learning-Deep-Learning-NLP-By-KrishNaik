import streamlit as st

st.title("Enter your name to get greeted")
name = st.text_input("Name:")
if st.button("Greet Me"):
    st.write(f"Hello, {name}! Welcome to this Streamlit app.")

st.title("Submit your scores to see if you pass or fail")
science = st.number_input("Science Score:", min_value=0, max_value=100)
maths = st.number_input("Maths Score:", min_value=0, max_value=100)
c = st.number_input("C Score:", min_value=0, max_value=100)
data = st.number_input("Data Score:", min_value=0, max_value=100)
if st.button("Submit Scores"):
    total_score = (science + maths + c + data) / 4
    if total_score >= 50:
        st.success(f"Congratulations! You passed with an average score of {total_score}.")
    else:
        st.error(f"Unfortunately, you failed with an average score of {total_score}.")


st.title("Data")
data = st.file_uploader("Upload a CSV file", type=["jpg", "png", "jpeg"])
if data is not None:
    st.image(data)

options = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox('Choose your fav language',options)
st.write("You selected:", choice)