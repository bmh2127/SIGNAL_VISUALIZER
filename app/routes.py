from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from .eeg_processing import load_eeg_data
from .noise_utils import add_noise
import os

app = Flask(__name__)

@app.route('/upload_eeg', methods=['POST'])
def upload_eeg():
    if request.method == 'POST':
        eeg_file = request.files['file']
        filename = secure_filename(eeg_file.filename)
        file_path = os.path.join('temp', filename)
        eeg_file.save(file_path)

        data, sampling_rate = load_eeg_data(file_path)
        os.remove(file_path)  # Clean up the temporary file

        return jsonify({'data': data.tolist(), 'sampling_rate': sampling_rate})

@app.route('/add_noise', methods=['POST'])
def apply_noise():
    data = request.json['data']
    noise_type = request.json['noise_type']
    params = request.json['params']
    
    noisy_data = add_noise(data, noise_type, **params)
    
    return jsonify(noisy_data=noisy_data.tolist())

if __name__ == '__main__':
    app.run()