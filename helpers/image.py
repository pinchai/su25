from werkzeug.utils import secure_filename
import os
from PIL import Image

UPLOAD_DIR = os.path.join("static", "image")
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXT = {"png", "jpg", "jpeg", "gif"}


def allowed(name):
    return "." in name and name.rsplit(".", 1)[-1].lower() in ALLOWED_EXT


def upload_image(file, name=""):
    try:
        if file and allowed(file.filename):
            if name.strip() == "":
                filename = secure_filename(file.filename)
            else:
                filename = name.strip()
            file.save(os.path.join(UPLOAD_DIR, filename))

            assert False, os.path.join(UPLOAD_DIR, filename)
            org_path = os.path.join(UPLOAD_DIR, filename)


            image_obj = Image.open(org_path)

            resized = image_obj.copy()
            resized.thumbnail(200, 200)
            resized.save(UPLOAD_DIR,f"thum_{filename}")

            return filename
    except Exception as e:
        return f"error message: {e}"


def delete_file(filename):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        os.unlink(file_path)
        return f"Successfully deleted {filename}"
    return "File not found", 404
