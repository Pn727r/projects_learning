# # import cv2
# # import face_recognition 
# # known_face_encodings = []
# # known_face_names = []


# # image2 = face_recognition.load_image_file("parth.png")
# # encoding2 = face_recognition.face_encodings(image2)[0]
# # known_face_encodings.append(encoding2)
# # known_face_names.append("Parth")

# # video_capture = cv2.VideoCapture(0)

# # while True:
# #     # Capture frame-by-frame
# #     ret, frame = video_capture.read()
    
# #     # Convert the frame from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
# #     rgb_frame = frame[:, :, ::-1]
    
# #     # Find all the faces and their encodings in the frame
# #     face_locations = face_recognition.face_locations(rgb_frame)
# #     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

# #     # Loop through each face in this frame of video
# #     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
# #         # See if the face is a match for the known face(s)
# #         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

# #         # If a match was found in known_face_encodings, just use the first one.
# #         # We can update this to show multiple matches later
# #         name = "Unknown"
# #         if True in matches:
# #             first_match_index = matches.index(True)
# #             name = known_face_names[first_match_index]

# #         # Draw a box around the face
# #         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

# #         # Draw a label with a name below the face
# #         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 255), cv2.FILLED)
# #         font = cv2.FONT_HERSHEY_DUPLEX
# #         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

# #     # Display the resulting image
# #     cv2.imshow('Video', frame)

# #     # Hit 'q' on the keyboard to quit!
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break




import pyrebase 
import face_recognition
import cv2
import numpy as np
import datetime 

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

known_faces = []
known_names = []
status = "IN"

firebase = pyrebase.initialize_app(config)
db = firebase.database()


known_image1 = face_recognition.load_image_file("parth.jpg")
known_face_encoding1 = face_recognition.face_encodings(known_image1)[0]
known_faces.append(known_face_encoding1)
known_names.append("parth")

known_image2 = face_recognition.load_image_file("shruti.jpg")
known_face_encoding2 = face_recognition.face_encodings(known_image2)[0]
known_faces.append(known_face_encoding2)
known_names.append("Shruti")


known_image3 = face_recognition.load_image_file("unnati.jpg")
known_face_encoding3 = face_recognition.face_encodings(known_image3)[0]
known_faces.append(known_face_encoding3)
known_names.append("Unnati")

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if status == "IN":
            face_distances = face_recognition.face_distance(known_faces, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]
                if name not in attendance_record:
                    attendance_record[name] = {
                        "date": datetime.date.today().strftime("%d-%m-%Y"),
                        "employee_name": name,
                        "time_in": formatted_time,
                    }
                    db.child("attendance_records").push(attendance_record[name])

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 255, 0), 1)
        cv2.putText(frame, status, (right - 20, bottom - 6), font, 0.5, (0, 255, 0), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()




import pyrebase
import openai

config = {
    "apiKey": "AIzaSyCAZxIYy94VAE54Q8mmQE623unhakad1t8",
    "authDomain": "homeease-c5c0b.firebaseapp.com",
    "databaseURL": "https://homeease-c5c0b-default-rtdb.firebaseio.com",
    "storageBucket": "homeease-c5c0b.appspot.com"
}



openai.api_key = "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"


# Initialize the Pyrebase app
firebase = pyrebase.initialize_app(config)

# Get the database reference
db = firebase.database()

# Define a function to answer questions from the database using OpenAI API
def answer_question(question):
    # Get the answer from the database
    answer = db.child(question).get()

    # If the answer is not found, return a default answer
    if answer is None:
        answer = "I couldn't find an answer to your question."
    else:
        # Use OpenAI API to generate a detailed response
        prompt = f"Question: {question}\nAnswer: {answer}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()

    # Return the answer
    return answer

# Get the user's prompt
user_prompt = input("What would you like to know? ")

# Ask OpenAI to answer the question from the database
answer = answer_question(user_prompt)

# Print the answer to the user
print(answer)



import random 
temp = ""
original = ["A","B","C"]
first_choice = False 

for i in range(10):
    if first_choice == False :
        choice = random.choice(original)
        temp = choice
        original.remove(choice)
        print(choice) 
        first_choice = True  
    else :
        choice = random.choice(original)
        print(choice)
        original.remove(choice)
        original.append(temp)
        temp = choice


for i in range(6):
    print(f"{'* '*i: ^10}")

