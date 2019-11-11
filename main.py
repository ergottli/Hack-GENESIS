from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from flask import send_file
import subprocess

app = Flask(__name__)

cur_file = os.path.dirname(os.path.realpath(__file__))

app.config["IMAGE_UPLOADS"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')
app.config["MOLECULES"] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static', 'molecules')
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]


def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route('/download_file/<string:molname>', methods=['GET', 'POST'])
def download(molname):
    print(" in download: " + molname)
    downloads = os.path.join(app.root_path, app.config['MOLECULES'], molname)
    if os.path.exists(downloads):
        norm_downloads = os.path.normpath(downloads)
        res = send_file(norm_downloads, as_attachment=True)
        # TODO удаление mol-файла после выдачи
        # os.remove(norm_downloads)
    else:
        res = "There is no file\n"
    return res


def receive_recog_files(pathfile, filename):
    molname = os.path.splitext(filename)[0] + "_1.mol"
    pngname = os.path.splitext(filename)[0] + "_1.png"
    smilesname = os.path.splitext(filename)[0] + "_sm_1.txt"
    # path's for mol files
    molfile = os.path.join(app.config["MOLECULES"], molname)
    pngfile = os.path.join(app.config["MOLECULES"], pngname)
    # path's for smiles files
    smiles_file = os.path.join(app.config["MOLECULES"], smilesname)
    # recognize with imago, create mol and smiles files
    subprocess.run(["./imago_console", pathfile, "-o", molfile], check=True)
    subprocess.run(["chmod", "+x", molfile], check=True)
    subprocess.run([os.path.join(os.path.dirname(os.path.realpath(__file__)), "open-babel", "bin", "obabel"), "-imol", molfile,
         "-osmiles", "-O", smiles_file], check=True)
    subprocess.run([os.path.join(os.path.dirname(os.path.realpath(__file__)), "open-babel", "bin", "obabel"), molfile,
        "-O", pngfile], check=True)
    return molname, pngname, smilesname, smiles_file


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/result", methods=['GET', 'POST'])
def result():
    return render_template("result.html")


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("Неверное имя")
                return render_template("upload_error.html")
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                pathfile = os.path.join(app.config["IMAGE_UPLOADS"], filename)
                molname, pngname, smilesname, smilesfile = receive_recog_files(pathfile, filename)
                print("Изображение сохранено")
                text = open(smilesfile, "r").read()
                return render_template("result.html", molname=molname, pngname=pngname, smilesname=text)
                # return render_template("viewer.html", molname=molname)
            else:
                print("Неверное расширение")
                return render_template("upload_error.html")
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/viewer/<string:molname>", methods=['GET', 'POST'])
def viewer(molname):
    return render_template("viewer.html", molname=molname)


@app.route("/water")
def water():
    return render_template("water.html")


@app.route("/isopropanol")
def isopropanol():
    return render_template("isopropanol.html")


@app.route("/oxytocin")
def oxytocine():
    return render_template("oxytocin.html")


@app.route("/cyanogen")
def cyanogen():
    return render_template("cyanogen.html")


@app.route("/isoliquiritigenin")
def Isoliquiritigenin():
    return render_template("isoliquiritigenin.html")


if __name__ == "__main__":
    app.run(debug=True)
