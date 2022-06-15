from flask import Flask, render_template
import os

project_root = os.path.dirname(__file__)

app = Flask(__name__)

PATH =  project_root  + "/great_expectations/uncommitted/data_docs/local_site/"

app=Flask(__name__,template_folder=PATH)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def home(path):
    return render_template(path)


if __name__ == '__main__':
    app.run(port=8050)