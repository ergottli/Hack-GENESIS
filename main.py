from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename
from flask import send_file
import subprocess
import shutil

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


@app.route('/download_file', methods=['GET', 'POST'])
def download():
    downloads = os.path.join(app.root_path, app.config['MOLECULES'], "molecule.mol")
    if os.path.exists(downloads):
        norm_downloads = os.path.normpath(downloads)
        res = send_file(norm_downloads, as_attachment=True)
        # TODO удаление mol-файла после выдачи
        # os.remove(norm_downloads)
    else:
        res = "There is no file\n"
    return res


def receive_recog_files(pathfile, filename):
    molname_1 = os.path.splitext(filename)[0] + "_1.mol"
    molname_2 =  os.path.splitext(filename)[0] + "_2.mol"
    pngname_1 = os.path.splitext(filename)[0] + "_1.png"
    smilesname_1 = os.path.splitext(filename)[0] + "_sm_1.txt"
    # path's for mol files
    molfile_1 = os.path.join(app.config["MOLECULES"], molname_1)
    molfile_2 = os.path.join(app.config["MOLECULES"], molname_2)
    pngfile_1 = os.path.join(app.config["MOLECULES"], pngname_1)
    # path's for smiles files
    smiles_file_1 = os.path.join(app.config["MOLECULES"], smilesname_1)
    smiles_file_2 = os.path.join(app.config["MOLECULES"], os.path.splitext(filename)[0] + "_sm_2.txt")
    # recognize with imago, create mol and smiles files
    subprocess.run(["./imago_console", pathfile, "-o", molfile_1], check=True)
    subprocess.run(["chmod", "+x", molfile_1], check=True)
    subprocess.run([os.path.join(os.path.dirname(os.path.realpath(__file__)), "open-babel", "bin", "obabel"), "-imol", molfile_1,
         "-osmiles", "-O", smiles_file_1], check=True)
    subprocess.run([os.path.join(os.path.dirname(os.path.realpath(__file__)), "open-babel", "bin", "obabel"), molfile_1,
        "-O", pngfile_1], check=True)
    print(molfile_1 + "\n" + pngfile_1)
    # recognize with open-babel, create mol and smiles files TODO если не получится сконверить в png, удалить нахер кусок код и папку imagemagic
    #subprocess.run([os.path.join(os.path.dirname(os.path.realpath(__file__)), "open-babel", "bin", "obabel"), pathfile_png,
    #     "-omol", "-O", molfile_2], check=True)
    #subprocess.run(["chmod", "+x", molfile_2], check=True)
    #subprocess.run([os.path.join(os.path.dirname(os.path.realpath(__file__)), "open-babel", "bin", "obabel"), "-imol", molfile_2,
    #     "-osmiles", "-O", smiles_file_2], check=True)
    return molname_1, pngname_1, smilesname_1


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


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
                # TODO если не получится сконвертить в png, удалить этот кусок кода
                #pathfile_png = os.path.join(app.config["IMAGE_UPLOADS"], os.path.splitext(filename)[0] + ".png")
                #subprocess.run([os.path.join(cur_file, "imagemagic", "bin", "mogrify"), "-format", "jpg",pathfile, pathfile_png], check=True)
                #print("pathfile_png " + pathfile_png)
                #if os.path.exists(os.path.join(cur_file, os.path.splitext(filename)[0] + ".png")):
                #    shutil.move(os.path.join(cur_file, os.path.join(cur_file, os.path.splitext(filename)[0] + ".png")), pathfile_png)
                # png_f = [i for i in os.listdir(os.path.dirname(os.path.realpath(__file__))) if "png" in i]
                # for i in png_f:
                #     shutil.move(os.path.join(cur_file, i), os.path.join(app.config['MOLECULES'], i))
                molname_1, pngname_1, smilesname_1 = receive_recog_files(pathfile, filename)
                print("Изображение сохранено")
                # TODO Удаление загруженного файла
                # os.remove(pathfile)
                return render_template("viewer.html", molname=molname_1)
            else:
                print("Неверное расширение")
                return render_template("upload_error.html")
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/viewer")
def viewer():
    return render_template("viewer.html")


@app.route("/water")
def water():
    return render_template("water.html")


@app.route("/isopropanol")
def isopropanol():
    return render_template("isopropanol.html")


if __name__ == "__main__":
    app.run(debug=True)
