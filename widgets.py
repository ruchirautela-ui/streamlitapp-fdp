import streamlit as st
name=st.text_input("Enter your name")
st.write("My name is ", name)
comments=st.text_area("Enter your comments")
st.write("comments ", comments)
app=st.date_input("Enter the date")
st.write("date is ", app)
if st.button("Add"):
    Total=89+99+12
    st.write("Total is ", Total)

show_result=st.checkbox("Show Result")
if show_result:
    st.write("Result :pass")

gender=st.radio('select your gender ',['female','male','other'])
st.write("you selected: ", gender)

city=st.selectbox('select your city',['New Delhi','Mumbai','Pune','Gurgaon'])
st.write("your city is: ", city)

hobbies=st.multiselect('select hobbies',['reading','traveling','swimming','coding'])
st.write("your hobbies are: ", hobbies)
