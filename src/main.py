from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main_page.html')

@app.route('/post')
def quote_post():
    return render_template('post_page.html')

@app.route('/post_quote', methods=['POST'])
def add_quote():
    with open("templates/main_page.html", 'a', encoding='utf-8') as f:
        f.write(f'<h1>{request.form['PostText']}. {request.form['Selector']}. Автор цитаты: {request.form['Author']}</h1>\n')
    return redirect('/')

app.run(debug=True)
# def get_quotes():
#     with open("main_page.html") as f:
#         return f.readlines()

