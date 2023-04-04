from flask import Flask, request, render_template, jsonify
from .noise_utils import add_noise
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    eeg_file = request.files['eeg-file']

    # Process the file, load the data and create a visualization
    # eeg_data = process_eeg_file(eeg_file)

    # Return the EEG data or visualization
    return eeg_data

@app.route('/add_noise', methods=['POST'])
def apply_noise():
    data = request.json['data']
    noise_type = request.json['noise_type']
    params = request.json['params']
    
    noisy_data = add_noise(data, noise_type, **params)
    
    return jsonify(noisy_data=noisy_data.tolist())

if __name__ == '__main__':
    app.run()