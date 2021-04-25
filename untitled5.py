from clarifai.rest import ClarifaiApp
app1=ClarifaiApp(api_key='e56af53f775c4f98ac8c4694a6ce093d')
model = app1.public_models.general_model
response = model.predict_by_url(url='https://st.depositphotos.com/1102480/1589/i/950/depositphotos_15890699-stock-photo-big-hamburger.jpg')
print(type(response))

concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
"""
    key=list(concepts.keys())
    print(concepts[5])
    X=[['healthy',1-concepts[5]['value']],['unhealthy', concepts[5]['value']]]
    data=pd.DataFrame(X, columns=['Type','Value'])
    fig, ax = plt.subplots(figsize=[10,6])
    labels = data['Type']
    plt.pie(x=data['Value'], autopct="%.1f%%", labels=labels, pctdistance=0.5)
    #plt.show()
    img=BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

"""