# Cat vs Dog Image Classifier

This is a simple UI built with Tkinter that classifies images as either a "Cat" or a "Dog" using a pre-trained machine learning model.

## Prerequisites

Before running the application, make sure you have Python installed, along with the required libraries.

You can install the dependencies using pip:
```bash
pip install tensorflow pillow numpy h5py
```

## Running the Application

To start the UI, simply run the `app.py` script:
```bash
python app.py
```

## How to Use

1. Click on the **Upload Image** button to select an image from your computer. (Accepts `.jpg`, `.jpeg`, and `.png` files)
2. The UI will display a preview of the image you selected.
3. Click the **Predict** button to run the classification model.
4. The result ("Cat" or "Dog") will be displayed at the bottom of the window!

---

## Code Explanation (For Beginners)

Here is a simple breakdown of how the `app.py` code works:

### 1. The Imports (The Tools We Need)
```python
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
```
Before we start, we need some 'libraries' (pre-written code):
- **tkinter:** This lets us build the visible window with buttons and text.
- **PIL (Pillow):** This handles loading and showing the images on the screen.
- **numpy:** This helps us turn the images into numbers so the model can read them.
- **tensorflow:** This runs our machine learning model.

### 2. Setting Up the Window
```python
class CatDogClassifier(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cat vs Dog Image Classifier")
        self.geometry("400x450")
```
This sets up a pop-up window named "Cat vs Dog Image Classifier" and makes it 400 pixels wide and 450 pixels tall.

### 3. Loading the 'Brain'
```python
self.model = tf.keras.models.load_model("cats_dogs_model.h5")
```
We load in our `cats_dogs_model.h5` file. Think of this as the "brain". It's been shown thousands of pictures of cats and dogs already and knows what to look for!

### 4. Making Buttons
```python
self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
self.predict_button = tk.Button(self, text="Predict", command=self.predict_image)
```
These lines create the buttons you see on the screen. When you click them, they run specific 'commands' (functions) inside our code.

### 5. Uploading and Showing the Image
```python
    def upload_image(self):
        # ... Lets you pick a file from your computer ...
    
    def display_image(self):
        # ... Resizes the image and shows it on the window ...
```
When you click 'Upload', it brings up a file browser. Once you select a file, it resizes the image to a specific dimension so it neatly fits in our window!

### 6. Predicting "Cat" or "Dog"
```python
    def predict_image(self):
        # ... Convert image into numbers ...
        prediction = self.model.predict(img_array)
        result = "Dog" if prediction[0][0] > 0.5 else "Cat"
```
When you click **Predict**:
1. We resize your image to `150x150` pixels because that's exactly what our "brain" expects!
2. We turn your image into an array of numbers (`np.array`). Models only understand numbers, not pictures!
3. We ask the model to `.predict()`. It spits out a number between `0` and `1`. 
4. If the number is closer to `1`, it thinks it's a **Dog**. If it's closer to `0`, it thinks it's a **Cat**. We display the result on the screen!
