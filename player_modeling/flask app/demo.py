from flask import Flask,render_template,request
from data import get_notebook_files,load_about

app = Flask(__name__)
print(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/notebook/")
def notebook():
    if(not "notebook_name" in request.args.keys()):
        notebook_name=get_notebook_files()[0]
    else:
        notebook_name=request.args["notebook_name"]

    return render_template("notebook.html",notebooks_dir=get_notebook_files(),notebook_name=notebook_name)


@app.route("/sobre")
def sobre():
    about_files_urls=load_about()
    return render_template("sobre.html",about_files_urls=about_files_urls,size_files=len(about_files_urls))

if __name__ == "__main__":
    app.run(debug=True)