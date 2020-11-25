from stemming.porter2 import stem
from flask import Flask, request, make_response, send

app= Flask(__name__)

def cleanse_text(text):
  if text:
    #removing whitespace
    clean=''.join(text.split())
    #stemming process on each word
    stem_text = [stem(word) for word in clean.split()]
    
    return''.join(stem_text)
  else:
    return text
  
def cluster():
  data = pd.read_csv(request.files['dataset'])
  unstructure = 'text'
  if 'col' in request.args:
    unstructure = requests.args.get('cols')
  no_of_clusters = 2
  if 'no_of_clusters' in request.args:
    no_of_clusters = request.args.get('no_of_clusters')
    
                                
                                   

