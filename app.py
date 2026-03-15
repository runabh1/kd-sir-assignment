
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

class CatDogClassifier(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cat vs Dog Image Classifier")
        self.geometry("400x450")

        self.model = tf.keras.models.load_model("cats_dogs_model.h5", compile=False)
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        self.image_path = None
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

        self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=5)

        self.predict_button = tk.Button(self, text="Predict", command=self.predict_image)
        self.predict_button.pack(pady=5)

        self.result_label = tk.Label(self, text="Prediction: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if self.image_path:
            self.display_image()

    def display_image(self):
        if not self.image_path:
            return
        
        img = Image.open(self.image_path)
        img = img.resize((300, 300))
        self.photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.photo)

    def predict_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first.")
            return

        try:
            img = Image.open(self.image_path).convert('RGB').resize((150, 150))
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = self.model.predict(img_array)
            result = "Dog" if prediction[0][0] > 0.5 else "Cat"
            self.result_label.config(text=f"Prediction: {result}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = CatDogClassifier()
    app.mainloop()
