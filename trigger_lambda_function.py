import json
import boto3
import random


def lambda_handler(event, context):

    QA = [
        "Question ทอดหมูยังไงไม่ให้ติดกระทะ? \nAnswer ทอดในหม้อ",
        "Question ประตูกลัวอะไร? \nAnswer กลัวไฟ เพราะมีประตูหนีไฟ",
        "Question ชมรมดนตรีไทยกลัวชมรมอะไร \nAnswer จิ๊กซอว์",
        "Question ถ้าคุณเล่นบาสนานมาก แล้วเพื่อนไปตาม จะเกิดอะไรขึ้น? \nAnswer ชูตาสใส่เพื่อน เพราะเพื่อนเป็นห่วง",
        "Question ปีอะไรมีหลายสี \nAnswer ปีโป้",
        "Question Why don't scientists trust atoms? \nAnswer Because they make up everything.", "Life is short, smile while you still have teeth.",
        "I'm not arguing, I'm just explaining why I'm right.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "I'm not lazy, I'm just on energy-saving mode.",
        "I'm not great at the advice, can I interest you in a sarcastic comment?",
        "I don't always have a sarcastic comment, but when I do, I still don't.",
        "I tried to start a hot air balloon business, but it never took off.",
        "I have a photographic memory, but I always forget to put in the memory card.",
        "I used to play piano by ear, but now I use my hands."]

    notification = random.randint(0, len(QA)-1)
    client = boto3.client('sns')
    response = client.publish(
        TargetArn="arn:aws:sns:ap-northeast-1:502983918849:Test-101",
        Message=QA[notification],
        Subject='This is just a JOKE.',
    )
