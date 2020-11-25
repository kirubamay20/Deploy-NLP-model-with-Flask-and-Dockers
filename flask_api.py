from flask import Flask, request, make_response, send

app= Flask(__name__)

def cleanse_text(text):
  if text:
    clean=''.join(text.split())
  else:
    return text
