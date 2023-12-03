from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder='web', static_folder='web/css/')

cosineSimilarity_data = pd.read_csv('cosine_similarity.csv')
books_data = pd.read_csv('books_data.csv')

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/index',)
def index():
    return "Hello World!"

@app.route('/books_recommendations', methods=['POST'])
def books_recommendations():
    title = request.form.get('book_title')
    similarity_data=cosineSimilarity_data
    items=books_data[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-L']]
    k=5
    print(type(title))
    try:
        # take data using argpartition to partition indirectly from the axis that given    
        # Change dataframe into numpy
        # Range(start, stop, step)
        index = similarity_data.loc[:,title].to_numpy().argpartition(
            range(-1, -k, -1))
        # print(similarity_data.sort_values(by = [title], ascending=False)[1:6])
        # print(similarity_data.columns[index[-1:-(k+2):-1]])
        #Take the bigest similarity data from avaliable index
        closest = similarity_data.columns[index[-1:-(k+2):-1]]

        # Drop book title therefore book title that we type does not appear
        closest = closest.drop(title, errors='ignore')
        scores = similarity_data[closest].iloc[0].tolist()
        # print(similarity_data[closest].iloc[0])
        scores = {'Scores': scores}
        scores = pd.DataFrame(scores)


        # return similarity_data.nlargest(5, 'The Notebook')
        recommendation= pd.DataFrame(closest, columns=['Book-Title']).merge(items).head(k)
        recommendation = recommendation.join(scores)
        
        # json_response = {'book_1': recommendation['Book-Title'][0],
        #                 'book_author_1': recommendation['Book-Author'][0]}
        book_year = recommendation['Year-Of-Publication'].astype(str)

        json_response = {}
        for index in range(k):
            json_response.update({'books_{}'.format(index+1) : 
                {'books_recommendation' : recommendation['Book-Title'][index], 
                'book_author': recommendation['Book-Author'][index],
                'book_year':book_year[index],
                'book_publisher': recommendation['Publisher'][index],
                'book_image_url': recommendation['Image-URL-L'][index],
                'book_score': recommendation['Scores'][index]}})

        return jsonify(json_response)

    except Exception as e:
        print(e)
        return 'No Recommendations for this Book'

if __name__ == "__main__":
    # app.run(host="localhost", debug=True)
    app.run(debug=True, host="0.0.0.0")