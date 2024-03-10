from deepface import DeepFace

def analyzeImage(imagePath):
    result = DeepFace.analyze(img_path = imagePath, actions = ['emotion'])
    return result[0]["dominant_emotion"]