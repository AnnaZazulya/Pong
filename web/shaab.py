from flask import Flask, json, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list, title='News', username='Аня')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
