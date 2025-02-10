import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import tkinter as tk

sonar_data = pd.read_csv(r"C:\Users\ASIF IRFAN\Desktop\projects\sonar.csv", header=None)

X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, Y_train)

def predict_sample():
    try:
        input_data_str = entry.get()

        input_data = [float(i) for i in input_data_str.split(",")]

        if len(input_data) != 60:
            raise ValueError("Please enter exactly 60 values.")

        input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

        input_data_scaled = scaler.transform(input_data_as_numpy_array)

        prediction = model.predict(input_data_scaled)

        if prediction[0] == 'R':
            result_text = 'Prediction: The object is a Rock'
        else:
            result_text = 'Prediction: The object is a Mine'

        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Invalid Input: Please enter exactly 60 numeric values separated by commas.")

root = tk.Tk()
root.title("Sonar Object Prediction")
root.geometry("600x400")
root.configure(bg="#f0f0f0")  

frame = tk.Frame(root, bg="blue")
frame.pack(padx=20, pady=20, fill="both", expand=True)

label = tk.Label(frame, text="Sonar Object Prediction System", font=("Times New Roman", 12), bg="white")
label.grid(row=0, column=0, columnspan=1, pady=10)

label = tk.Label(frame, text="Enter the row values (comma separated):", font=("Times New Roman", 12), bg="yellow")
label.grid(row=1, column=0, columnspan=1, pady=10)

entry = tk.Entry(frame, width=80, font=("Times New Roman", 12), bg="#fff", fg="#000", bd=2, relief="solid")
entry.grid(row=2, column=0, columnspan=2, pady=10)

predict_button = tk.Button(frame, text="Predict", command=predict_sample, font=("Times New Roman", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", bd=3)
predict_button.grid(row=3, column=0, columnspan=1, pady=20)

result_label = tk.Label(frame, text="Prediction: ", font=("Times New Roman", 14),bg="red", width=30, height=2, anchor="w")
result_label.grid(row=4, column=0, columnspan=1, pady=10)

root.mainloop()
