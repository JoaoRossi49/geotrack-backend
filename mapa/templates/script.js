//<script>
//var markers = [
//    {lat: 51.5074, lng: -0.1278, popupText: 'London'},
//    {lat: 40.7128, lng: -74.0060, popupText: 'New York'},
//];
//
//markers.forEach(function(marker) {
//    L.marker([marker.lat, marker.lng]).addTo(map)
//        .bindPopup(marker.popupText);
//});
//</script>

document.getElementById('atualizarBtn').addEventListener('click', function() {
    fazerChamadaAPI();
});

function fazerChamadaAPI() {
    // URL da API coordenadas
    const apiUrl = 'http://127.0.0.1:8000/api/coordenadas/last';
    const xhr = new XMLHttpRequest();
    xhr.open('GET', apiUrl, true);
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
        const response = JSON.parse(xhr.responseText);
        atualizarMapa(response);
        } else {
        console.error('A requisição falhou. Status da resposta:', xhr.status);
        }
    };
    xhr.onerror = function() {
        console.error('Erro de rede ao tentar fazer a requisição.');
    };
    xhr.send();
}
function atualizarMapa(coordenadas) {
    markers.forEach(function(marker) {
        map.removeLayer(marker);
    });
    markers = [];
    coordenadas.forEach(function(coordenada) {
        var marker = L.marker([coordenada.latitude, coordenada.longitude]).addTo(map);
        marker.bindPopup(coordenada.popupText);
        markers.push(marker);
    });
}