import pickle

geometrymodel = pickle.load(open('geometrymodel','rb'))
geometryvectorizer = pickle.load(open('geometryvectorizer','rb'))
text = 'lightweight shock resistant material'
geometrymodel.predict(geometryvectorizer.transform([text]))
