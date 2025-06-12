import os
import time
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, render_template, request
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# import tensorflow as tf
# import cv2
# import os
import google.generativeai as genai
import PIL.Image

# Konfigurasi gemini API key
genai.configure(api_key="AIzaSyC2txHOmdTwi0hE12XkalNd7hK-SpFe4Fk")

# Load model 
model = load_model('model/model.h5')

app = Flask(__name__)
CORS(app)  # agar bisa diakses dari frontend lokal

@app.route('/')
def index():
    return render_template('webTrash.html')

# # melihat output prediksi
# import numpy as np
# from PIL import Image

# img = Image.open("static/uploads/th_1.jpeg").resize((224, 224))  # atau ukuran input model kamu
# img_array = np.array(img) / 255.0
# img_array = np.expand_dims(img_array, axis=0)

# prediction = model.predict(img_array)
# print("Hasil prediksi model:", prediction)
# # END

def get_pengolahan(jenis):
    if jenis.lower() == "organik":
        return "Sampah organik dapat diolah menjadi kompos atau pakan ternak."
    elif jenis.lower() == "anorganik":
        return "Sampah anorganik sebaiknya dipilah dan didaur ulang atau disetor ke bank sampah."
    else:
        return "Jenis sampah tidak dikenali."

@app.route('/detect_trash', methods=['POST'])
def detect_trash():
    file = request.files['image']

    upload_folder = 'static/uploads'
    filename = secure_filename(file.filename)
    filename = f"{int(time.time())}_{filename}"  # contoh: 1718000000_nama_file.jpg
    save_path = os.path.join(upload_folder, filename)
    file.save(save_path)

    # Proses prediksi
    img = Image.open(file.stream).resize((224, 224))  # sesuaikan ukuran dengan model
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    jenis = "Organik" if prediction[0][0] > 0.5 else "Anorganik"  # sesuaikan dengan model kamu
    score = prediction[0][0]
    
    pengolahan = get_pengolahan(jenis)

    # Prompt ke Gemini
    prompt = f"""
    Gambar ini diklasifikasikan sebagai '{jenis}'.
    Berikan penjelasan tentang kenapa gambar ini termasuk '{jenis}'
    dan bagaimana sebaiknya pengolahannya secara ramah lingkungan.
    """

    # Generate content dari Gemini
    try:
        # Load model Gemini
        model_2 = genai.GenerativeModel("gemini-1.5-flash")

        file.stream.seek(0)
        img_pil = PIL.Image.open(file.stream)

        response = model_2.generate_content([prompt, img_pil])

        penjelasan_gemini = response.text if hasattr(response, 'text') else pengolahan
    except Exception as e:
        penjelasan_gemini = f"Terjaadi kesalahan saat memanggil Gemini API: {str(e)}"

    # Return respomse JSON
    return jsonify({
        "jenis_sampah": jenis,
        "path_gambar": save_path,
        # "pengolahan": pengolahan,
        # "persentase": f"{round(score * 100, 2)}%",
        "penjelasan_gemini": penjelasan_gemini
    })

if __name__ == '__main__':
    app.run(debug=True)