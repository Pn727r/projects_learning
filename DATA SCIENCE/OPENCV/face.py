# import cv2
# import face_recognition
# import os
# import tkinter as tk
# from tkinter import Entry, Button

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Employee Registration and Attendance")

# # Initialize known_face_encodings and known_face_names
# known_face_encodings = []
# known_face_names = []

# def add_employee():
#     employee_name = entry_employee_name.get()
#     if not employee_name:
#         return

#     employee_folder = os.path.join("employee_faces", employee_name)
#     os.makedirs(employee_folder, exist_ok=True)

#     cap = cv2.VideoCapture(0)

#     num_captures = 0
#     while num_captures < 20:
#         ret, frame = cap.read()
#         if ret:
#             face_locations = face_recognition.face_locations(frame)
#             if len(face_locations) == 1:
#                 num_captures += 1
#                 image_name = f"{employee_name}_{num_captures}.jpg"
#                 image_path = os.path.join(employee_folder, image_name)
#                 cv2.imwrite(image_path, frame)

#     # Release the webcam
#     cap.release()

#     # Update known_face_encodings and known_face_names
#     employee_images = [face_recognition.load_image_file(os.path.join(employee_folder, f"{employee_name}_{i}.jpg")) for i in range(1, 21)]
#     employee_encodings = [face_recognition.face_encodings(image)[0] for image in employee_images]
#     known_face_encodings.append(employee_encodings)
#     known_face_names.append(employee_name)

#     # Inform the user that employee photos are captured
#     result_label.config(text=f"Employee {employee_name} registered!")

# # Function to perform face recognition and mark attendance
# def scan_employee():
#     # Initialize the webcam
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()

#         # Find faces in the frame
#         face_locations = face_recognition.face_locations(frame)
#         face_encodings = face_recognition.face_encodings(frame, face_locations)

#         for face_location in face_locations:
#             top, right, bottom, left = face_location
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#         # Display the frame
#         cv2.imshow('Video', frame)

#         # Quit when the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the webcam
#     cap.release()
#     cv2.destroyAllWindows()

# # Create an input field for employee name
# label_employee_name = tk.Label(root, text="Employee Name:")
# label_employee_name.pack()
# entry_employee_name = Entry(root)
# entry_employee_name.pack()

# # Create a button to add an employee
# button_add_employee = Button(root, text="Add Employee", command=add_employee)
# button_add_employee.pack()

# # Create a button to scan and mark attendance
# button_scan_employee = Button(root, text="Scan Attendance", command=scan_employee)
# button_scan_employee.pack()

# # Create a label for displaying registration/attendance status
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Start the Tkinter main loop
# root.mainloop()



from tkinter import messagebox
import cv2
import pyrebase
import face_recognition
import os
import tkinter as tk
import datetime
from tkinter import Entry, Button

config = {
    "apiKey": "AIzaSyCAZxIYy94VAE54Q8mmQE623unhakad1t8",
    "authDomain": "homeease-c5c0b.firebaseapp.com",
    "databaseURL": "https://homeease-c5c0b-default-rtdb.firebaseio.com",
    "storageBucket": "homeease-c5c0b.appspot.com"
}

current_time = datetime.datetime.now().time()
formatted_time = current_time.strftime("%I:%M %p")

attendance_record = {
    "date": datetime.date.today().strftime("%d-%m-%Y"),
    "employee_name": "" ,
    "time_in": "",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
          
num_captures = 0 
root = tk.Tk()
root.title("Employee Registration and Attendance")

# Initialize known_face_encodings and known_face_names
known_face_encodings = []
known_face_names = []

# Function to capture and save employee photos
def add_employee():
    employee_name = entry_employee_name.get()
    if not employee_name:
        return

    employee_faces_folder = "employee_faces"
    os.makedirs(employee_faces_folder, exist_ok=True)

    cap = cv2.VideoCapture(0)

    num_captures = 0

    while num_captures < 25:
        ret, frame = cap.read()
        if not ret:
            break

        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) > 0:
            top, right, bottom, left = face_locations[0]
            face_image = frame[top:bottom, left:right]
            image_name = f"{employee_name}_{num_captures + 1}.jpg"
            image_path = os.path.join(employee_faces_folder, image_name)
            cv2.imwrite(image_path, face_image)
            num_captures += 1

        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or num_captures >= 25:
            break

    cap.release()
    cv2.destroyAllWindows()

    messagebox.showinfo("Face Scanned !")

    # result_label.config(text=f"{num_captures} faces saved for {employee_name} in employee_faces folder!")

def scan_employee():
    employee_faces_folder = "employee_faces"

    if not os.path.exists(employee_faces_folder) or not os.listdir(employee_faces_folder):
        messagebox.showinfo("Info", "No employee faces found in 'employee_faces' folder.")
        return

    known_face_encodings = []
    known_face_names = []

    # Load known face encodings and names from employee_faces folder
    for root, _, files in os.walk(employee_faces_folder):
        for file in files:
            if file.endswith(".jpg"):
                employee_name = file.split("_")[0]
                image_path = os.path.join(root, file)
                face_image = face_recognition.load_image_file(image_path)
                face_encodings = face_recognition.face_encodings(face_image)
                
                if len(face_encodings) > 0:
                    known_face_encodings.append(face_encodings[0])
                    known_face_names.append(employee_name)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Find all face locations in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each detected face in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                if name not in attendance_record:
                    attendance_record[name] = {
                        "date": datetime.date.today().strftime("%d-%m-%Y"),
                        "employee_name": name,
                        "time_in": formatted_time,
                        "time_out": "",
                    }
                    db.child("attendance_records").push(attendance_record[name])

            # Draw a green box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)

            # Label the face with the employee's name
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.putText(frame, "IN", (right , top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


label_employee_name = tk.Label(root, text="Employee Name:")
label_employee_name.pack()
entry_employee_name = Entry(root)
entry_employee_name.pack()

button_add_employee = Button(root, text="Add Employee", command=add_employee)
button_add_employee.pack()

button_scan_employee = Button(root, text="Scan Attendance", command=scan_employee)
button_scan_employee.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
