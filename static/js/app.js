document.getElementById('getWeatherBtn').addEventListener('click', function () {
    const city = document.getElementById('city').value;
    if (!city) {
        alert('Bitte geben Sie eine Stadt ein');
        return;
    }

    fetch(`/wetter?stadt=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('weatherInfo').innerHTML = 'Stadt nicht gefunden!';
            } else {
                document.getElementById('weatherInfo').innerHTML = `
                            <p>Temperatur: ${data.temperature}°C</p>
                            <p>Minimale Temperatur: ${data.min_temperature}°C</p>
                            <p>Maximale Temperatur: ${data.max_temperature}°C</p>
                            <p>Windgeschwindigkeit: ${data.wind} m/s</p>
                            <p>Luftfeuchtigkeit: ${data.luftfeuchtigkeit}%</p>
                            <p>Sonnenaufgang: ${new Date(data.sonnenaufgang).toLocaleTimeString()}</p>
                            <p>Sonnenuntergang: ${new Date(data.sonnenuntergang).toLocaleTimeString()}</p>
                        `;
            }
        })
        .catch(error => {
            document.getElementById('weatherInfo').innerHTML = 'Fehler beim Abrufen der Daten';
        });
});