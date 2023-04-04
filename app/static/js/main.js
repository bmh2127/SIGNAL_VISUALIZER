let plot;

async function displayEEGData(data, samplingRate) {
    const eegDisplay = document.getElementById('eeg-display');
    const time = Array.from({ length: data.length }, (_, i) => i / samplingRate);

    const trace = {
        x: time,
        y: data,
        mode: 'lines',
        line: { color: '#3f8dff' }
    };

    const layout = {
        title: 'EEG Data',
        xaxis: { title: 'Time (s)' },
        yaxis: { title: 'Amplitude' },
        margin: { t: 30, l: 50, r: 10, b: 50 }
    };

    if (!plot) {
        plot = await Plotly.newPlot(eegDisplay, [trace], layout);
    } else {
        await Plotly.update(eegDisplay, { x: [time], y: [data] });
    }
}

const addNoiseToData = async (data, noiseType, params) => {
    const response = await fetch('/add_noise', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data, noise_type: noiseType, params })
    });

    const result = await response.json();
    return result.noisy_data;
};

document.getElementById('zoom-in').addEventListener('click', () => {
    Plotly.relayout('eeg-display', { 'xaxis.range': (range) => [range[0] * 1.25, range[1] * 0.75] });
});

document.getElementById('zoom-out').addEventListener('click', () => {
    Plotly.relayout('eeg-display', { 'xaxis.range': (range) => [range[0] * 0.75, range[1] * 1.25] });
});

document.getElementById('pan-left').addEventListener('click', () => {
    Plotly.relayout('eeg-display', { 'xaxis.range': (range) => [range[0] * 0.9, range[1] * 0.9] });
});

document.getElementById('pan-right').addEventListener('click', () => {
    Plotly.relayout('eeg-display', { 'xaxis.range': (range) => [range[0] * 1.1, range[1] * 1.1] });
});