from flask import Flask, request, render_template, session, jsonify
from user_functions import stem_and_vectorize_products_based_on_metadata, generate_recs, get_sample_product

app = Flask(__name__)
app.secret_key = 'any random string' 


@app.route('/nlp', methods=['GET', 'POST'])
def nlppage():
    nlp = ''
    num_results = 0
    recommended_products = []
    if request.method == 'POST' and 'searchwords' in request.form:
        search_words = request.form.get('searchwords')
        num_results, recommended_products = stem_and_vectorize_products_based_on_metadata(search_words)
    return render_template('nlp.html',
                           nlp=nlp, 
                           num_results=num_results,
                           recommended_products=recommended_products) 

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template('index.html')



@app.route('/svd', methods=['GET', 'POST'])
def svdpage():
    svd_recs = ''
    num_results = 0
    session['n_left_to_rate'] = None
    if request.method == 'POST' and 'num_to_rate' in request.form:
        session['rate_aisle'] = request.form.get('rate_aisle')
        session['n_to_rate'] = float(request.form.get('num_to_rate'))
        session['rec_aisle'] = request.form.get('rec_aisle')
        session['n_to_rec'] = float(request.form.get('num_to_rec'))
        session['percent_diverse'] = float(request.form.get('diversity_index'))
        session['prod_name'], session['prod_aisle'], session['prod_id'] = get_sample_product(session['rate_aisle'])
        session['n_left_to_rate'] = session['n_to_rate'] - 1
        session['ratings_list'] = []
        return render_template('rating.html')
    else:
        return render_template('svd.html',
                            svd_recs=svd_recs,
                            num_results=num_results)

@app.route('/rating', methods=['GET', 'POST'])
def ratingpage():
    if session['n_to_rate'] is None:
        return render_template('svd.html',
                               svd_recs='',
                               num_results=0)
    
    if session['n_left_to_rate'] == 0:
        num_results, svd_recs = generate_recs(session['ratings_list'], session['n_to_rec'], session['percent_diverse'], rec_aisle=session['rec_aisle'])
        return render_template('svd.html',
                               svd_recs=svd_recs,
                               num_results=num_results)
    elif 'rate_product' in request.form:
        rating = float(request.form.get('rate_product'))
        session['ratings_list'].append([session['prod_id'], rating])
        session['n_left_to_rate'] -= 1
        session['prod_name'], session['prod_aisle'], session['prod_id'] = get_sample_product(session['rate_aisle'])
        return render_template('rating.html')
    else:
        return render_template('rating.html') 

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    search_words = request.form.get('search_words')
    num_results, recommended_products = stem_and_vectorize_products_based_on_metadata(search_words)
    return jsonify({'num_results': num_results, 'product_names': recommended_products})

@app.route('/update_recommendations', methods=['POST'])
def update_recommendations():
    selected_product = request.form.get('selected_product')
    num_results, updated_recommended_products = stem_and_vectorize_products_based_on_metadata(selected_product)
    return jsonify({'num_results': num_results, 'product_names': updated_recommended_products})

if __name__ == "__main__":
    app.run(debug=True)
