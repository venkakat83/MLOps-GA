import streamlit as st

st.title('Hello World')

sl = st.slider("Sepal Length(cm)", min_value= 4.0, max_value= 8.0, value= 6.0, step= 0.1)
pl = st.slider("Petal Length(cm)", min_value= 1.0, max_value= 7.0, value= 3.0, step= 0.1)
sw= st.slider("Sepal Width(cm)", min_value= 2.0, max_value= 5.0, value= 3.0, step= 0.1)
pw = st.slider("Petal Width(cm)", min_value= 0.1, max_value= 2.5, value= 1.0, step= 0.1)

if st.button('Predict'):
    input_data = [[sl, sw, pl, pw]]
    #prediction = model.predict(input_data)
    prediction = "Versicolor"
    st.write(f"Prediction: {prediction}") 

