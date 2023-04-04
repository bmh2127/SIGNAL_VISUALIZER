import numpy as np
from scipy import signal

def add_gaussian_noise(data, mean=0, std=1):
    noise = np.random.normal(mean, std, data.shape)
    return data + noise

def add_power_line_interference(data, freq=60, amplitude=1, sampling_rate=1000):
    t = np.arange(0, len(data)/sampling_rate, 1/sampling_rate)
    interference = amplitude * np.sin(2 * np.pi * freq * t)
    return data + interference

def add_muscle_artifacts(data, freq_range=(20, 100), amplitude=1, sampling_rate=1000):
    t = np.arange(0, len(data)/sampling_rate, 1/sampling_rate)
    freq = np.random.uniform(freq_range[0], freq_range[1])
    artifact = amplitude * np.sin(2 * np.pi * freq * t)
    return data + artifact

def add_eye_movement_artifacts(data, amplitude=1, num_artifacts=1, sampling_rate=1000):
    num_samples = len(data)
    artifact = np.zeros(num_samples)

    for _ in range(num_artifacts):
        start = np.random.randint(0, num_samples)
        duration = np.random.randint(sampling_rate // 10, sampling_rate // 2)
        end = min(start + duration, num_samples)
        artifact[start:end] = amplitude

    return data + artifact

def add_noise(data, noise_type, **kwargs):
    if noise_type == 'gaussian':
        return add_gaussian_noise(data, **kwargs)
    elif noise_type == 'power_line_interference':
        return add_power_line_interference(data, **kwargs)
    elif noise_type == 'muscle_artifacts':
        return add_muscle_artifacts(data, **kwargs)
    elif noise_type == 'eye_movement_artifacts':
        return add_eye_movement_artifacts(data, **kwargs)
    else:
        raise ValueError(f"Unknown noise type: {noise_type}")
