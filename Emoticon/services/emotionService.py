
from ..modules import analyzeImage,GmailSender
from ..configuration import configHelper
class EmotionService:

    def __init__(self) -> None:
        self.config = configHelper().getConfig()

    def checkEmotion(self,imagePath):
        gmail_sender = GmailSender()
        emotion = analyzeImage(imagePath)
        if self.checkNegativeEmotion(emotion):
            senderMail = self.config["senderEmails"]
            receiverEmails = self.config["receiverEmails"]
            subject = self.config["subject"]
            body = f"{self.config['emailBody']} The detected emotion is {emotion}"
            for receiver_email in receiverEmails:
                message = gmail_sender.create_message(senderMail, receiver_email, subject, body)
                gmail_sender.send_message("me", message)
            return "Leave is automatically approved"
        return "Leave application sent for manual approval"


    def checkNegativeEmotion(self,emotion):
        positiveEmotions = ("happy","surprise","neutral")
        if emotion not in positiveEmotions:
            return True
        return False

