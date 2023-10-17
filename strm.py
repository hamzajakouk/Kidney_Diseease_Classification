import streamlit as st
from PIL import Image
from src.cnnClassifier.pipeline.prediction import PredictionPipeline # Import your PredictionPipeline class
import os

# Instantiate the PredictionPipeline with a filename (you can change this as needed)


st.title("Cancer Prediction App")

st.write("Upload an image for cancer prediction:")
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
predect = PredictionPipeline(filename=uploaded_image)
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Save the uploaded image temporarily to a file
        temp_image_filename = "temp_image.jpg"
        image.save(temp_image_filename)

        # Initialize the PredictionPipeline with the temporary image file

        # Make a prediction
        prediction_result = predect.predict()

        # Display the prediction result
        if prediction_result == "Tumor":
            st.error("Cancer detected.")
        else:
            st.success("No Cancer detected.")

        # Remove the temporary image file
        os.remove(temp_image_filename)

# You can add more content and style to improve the user interface.
