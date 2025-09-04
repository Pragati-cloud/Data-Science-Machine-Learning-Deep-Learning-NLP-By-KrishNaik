import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['species'] = data.target
    return df, data.target_names

df, target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider('Sepal Length', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider('Sepal Width', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider('Petal Length', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider('Petal Width', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]  # 2D array for predict

species_images = {
    "setosa": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/500px-Irissetosa1.jpg",
    "versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
}

prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.title("Iris Species Prediction")
st.write(f"Predicted Species: {predicted_species}")
st.image(species_images[predicted_species], caption=predicted_species, use_container_width=True)