from flask import Flask, render_template           	# import flask
Myapp = Flask(__name__)             # create an app instance

@Myapp.route('/')
def hello():                      		# call method hello
    return "Hello World!"         	    # which returns "hello world"

@Myapp.route('/dynamicurl/<varible_name>/')
def dynamic(varible_name):
    return f"Hello {varible_name}"

@Myapp.route('/data')
def data():
    columns=['Shows','Imdb Ratings']
    items = ['Breaking Bad ',' Dark','Peaky Blinders','Narcos','Stranger Things']
    values=[9.4,8.8,8.8,8.8,8.7]
    zipped_values = zip(items, values)
    row_data = list(zipped_values)

    return render_template("index.html",columns=columns,row_data=row_data,zip=zip)


if __name__ == "__main__":       # on running python app.py
    Myapp.run(debug=True)       # run the flask app