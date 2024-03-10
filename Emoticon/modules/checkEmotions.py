from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from deepface import DeepFace

def analyze_emotion(image):
    # Save the uploaded image temporarily
    img_name = default_storage.save('temp_image.png', ContentFile(image.read()))
    img_path = default_storage.path(img_name)
    
    # Analyze the emotion of the uploaded image
    face_analysis = DeepFace.analyze(img_path=img_path)
    
    # Get the dominant emotion from the analysis
    dominant_emotion = face_analysis['dominant_emotion']
    
    return dominant_emotion