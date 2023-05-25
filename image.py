from base64 import b64decode
import datetime
import openai
from openai.error import InvalidRequestError
import os

API_KEY = 'YOUR_API_KEY'

SIZES = ('1024x1024', '512x512', '256x256')

openai.api_key = API_KEY

def generate_image(prompt, num_image=1, size='256x256'):
    """
    params:
        prompt (str):
        num_image (int):
        size (str):
    """
    try:
        images = []
        response = openai.Image.create(
            prompt=prompt,
            n=num_image,
            size=size,
            response_format='b64_json'
        )
        for image in response['data']:
            images.append(image.b64_json)

        # setting up image directory
        BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
        IMG_DIR = os.path.join(BASE_DIR, 'images')
        if not os.path.exists(IMG_DIR):
            os.makedirs(IMG_DIR)
        image_path = os.path.join(IMG_DIR, f'{prompt}.jpg')
            
        with open(image_path, 'wb') as f:
            f.write(b64decode(images[0]))

        return image_path
    except InvalidRequestError as e:
        print(e)

