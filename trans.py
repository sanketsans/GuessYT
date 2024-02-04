from deep_translator import GoogleTranslator
from openai import OpenAI

to_translate = 'Why'
translated = GoogleTranslator(source='auto', target='it').translate(to_translate)

client = OpenAI()
response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)