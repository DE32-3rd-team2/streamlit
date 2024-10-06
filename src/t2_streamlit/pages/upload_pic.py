import streamlit as st
from mtcnn import MTCNN
from PIL import Image
import numpy as np
import requests
import io

def find_face(img):
    detector = MTCNN()
    
    img_np = np.array(img)
    faces = detector.detect_faces(img_np)
    return faces

def upload_img(img, name):
    url = "http://localhost:8022/uploadfile/"

    img_bytes = io.BytesIO()
    img.save(img_bytes, format='JPEG')
    img_bytes.seek(0)

    files = {"file": (name+'.jpeg', img_bytes, 'image/jpeg')}
    r = requests.post(url, files=files)
    return r

st.title('Upload Picture')
pic = st.file_uploader('img', type=['png', 'jpg', 'jpeg', 'webp'], label_visibility="hidden")

if pic is not None:
    image = Image.open(pic).convert("RGB")
    faces = find_face(image)

    if len(faces) == 0:
        st.error("No faces detected.")
    else:
        for i, face in enumerate(faces):
            x, y, w, h = face['box']
            
            face_crop = image.crop((x-15, y-15, x+w+15, y+h+15))
            st.image(face_crop, width=100)
            
            file_name = f"{pic.name.split('.')[-2]}({i+1})"
            r = upload_img(face_crop, file_name)
            st.write(r.json())
