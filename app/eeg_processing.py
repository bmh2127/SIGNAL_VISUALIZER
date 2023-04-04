import mne

def load_eeg_data(file_path):
    # Load the EEG data
    raw = mne.io.read_raw(file_path, preload=True)

    # Process the data (e.g., filtering, epoching, etc.)
    # Here you can apply any preprocessing steps required for your use case.
    # For example, you can filter the data:
    raw.filter(l_freq=1, h_freq=50)

    # Extract the data and sampling rate
    data = raw.get_data()
    sampling_rate = raw.info['sfreq']

    return data, sampling_rate
