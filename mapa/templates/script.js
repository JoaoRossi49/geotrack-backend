document.getElementById('atualizarBtn').addEventListener('click', function() {
    fazerChamadaAPI();
});

function fazerChamadaAPI() {
    // URL da API que você deseja chamar
    const apiUrl = 'http://127.0.0.1:8000/api/lastCoordenada';

    // Fazendo a chamada GET usando XMLHttpRequest
    const xhr = new XMLHttpRequest();
    xhr.open('GET', apiUrl, true);

    // Função de retorno de chamada quando a requisição estiver concluída
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            // Se a requisição foi bem-sucedida
            const response = JSON.parse(xhr.responseText);
            document.getElementById('resultado').innerHTML = JSON.stringify(response);
        } else {
            // Se a requisição falhou
            console.error('A requisição falhou. Status da resposta:', xhr.status);
        }
    };

    // Função de retorno de chamada para tratamento de erro
    xhr.onerror = function() {
        console.error('Erro de rede ao tentar fazer a requisição.');
    };

    // Enviando a requisição
    xhr.send();
}
