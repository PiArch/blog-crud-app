from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/assets"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

posts = []

def get_post(post_id):
    return next((p for p in posts if p["id"] == post_id), None)

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        image = request.files.get("image")
        image_name = image.filename if image and image.filename else None

        if image_name:
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        post = {
            "id": len(posts) + 1,
            "title": request.form["title"],
            "author": request.form["author"],
            "content": request.form["content"],
            "image": image_name,
            "created": datetime.now(),
            "updated": datetime.now()
        }
        posts.append(post)
        return redirect(url_for("index"))

    return render_template("add-edit.html", post=None)

@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = get_post(post_id)

    if request.method == "POST":
        image = request.files.get("image")

        if image and image.filename:
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
            post["image"] = image.filename

        post["title"] = request.form["title"]
        post["author"] = request.form["author"]
        post["content"] = request.form["content"]
        post["updated"] = datetime.now()

        return redirect(url_for("index"))

    return render_template("add-edit.html", post=post)

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return redirect(url_for("index"))

@app.route("/view/<int:post_id>")
def view_post(post_id):
    post = get_post(post_id)
    return render_template("view.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
