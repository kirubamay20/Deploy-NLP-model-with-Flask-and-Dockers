import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import kmeans
from stemming.porter2 import stem
from flask import Flask, request, make_response, send
from io import BytesIO
import time
import zipfile

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
  
@app.route('/cluster', methods=['POST'])  
  
  
def cluster():
  data = pd.read_csv(request.files['dataset'])
  unstructure = 'text'
  if 'col' in request.args:
    unstructure = requests.args.get('cols')
  no_of_clusters = 2
  if 'no_of_clusters' in request.args:
    no_of_clusters = request.args.get('no_of_clusters')
   
  data=data.fillna('NULL')
  data['clean_sum'] = data[unstructure].apply(clean_text)
  
  vectorizer= CountVectorizer(analyzer='word', stop_words='english')
  #Doc1-> He is a lazy boy. she is also lazy
  #Doc2-> He is a lazy person.
  #       He she lazy boy person
  #Doc1   1   1   2    1   0
  #Doc2   1   0   1    0   1
  
  counts = vectorizer.fit_transform(data['clean_sum'])
  
  kmeans=KMeans(n_clusters= no_of_clusters)
  data['cluster_num'] = kmeans.fit_predict(counts)
  data= data.drop(['clean_sum'],axis=1)
  
  output=BytesIO()
  writer=pd.ExcelWriter(output, engine='xlswriter')]
  data.to_excel(writer, sheet_name='Clusters', encoding='utf-8', index=Flase)
  
  memory_file = BytesIO()
  with zipfile.ZipFile(memory_file, 'w') as zf:
    
  
    names=['cluster_output.xlsx', 'file2', 'file3']
    files=[output1, output2, output3]
    for i in range(len(files)):
       data=zipfile.ZipInfo(names[i])
       data.date_time=time.localtimes(times.times())[:6]
       data.compress_type = zipfile.ZIP.DEFLATED
      zf.writestr(data, files[i].getvalue())
  memory_file.seek(0)
  
  
  
  return 'commit'

  
  
  if __name__ == '__main__':
    app.run(host='0.0.0.0')
                                
                                   

