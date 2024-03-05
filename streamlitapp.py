import streamlit as st
from src.cnn_classifier.pipeline.prediction import PredictionPipeline
import os

def main():
    st.title("Kidney Tumor Identification")
    os.makedirs("temp", exist_ok=True)
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        temp_location = f"temp/{uploaded_file.name}"
        col1,col2=st.columns((2))
        with open(temp_location, "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Create PredictionPipeline instance and get prediction
        pipeline = PredictionPipeline(temp_location)
        prediction = pipeline.predict()

        # Display the uploaded image
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Display the prediction
        with col2:
            st.subheader("Prediction:")

            st.write(f"{prediction['image']}")

if __name__ == "__main__":
    main()