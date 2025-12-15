let chartInstance = null;
let dadosGlobais = [];

document.addEventListener('DOMContentLoaded', () => {
    carregarDados();
});

// --- FUNÇÃO DO MODAL (NOVA) ---
function fecharModal() {
    const modal = document.getElementById('intro-modal');
    modal.style.display = 'none'; // Esconde o modal ao clicar
}

// Busca dados do Python
async function carregarDados() {
    try {
        const response = await fetch('/api/dados');
        dadosGlobais = await response.json();
        
        criarListaLateral(dadosGlobais);
        
        if(dadosGlobais.length > 0) {
            atualizarDashboard(dadosGlobais[0]);
        }
    } catch (error) {
        console.error("Erro ao carregar dados:", error);
    }
}

// Cria a lista lateral
function criarListaLateral(dados) {
    const lista = document.getElementById('lista-profissoes');
    lista.innerHTML = '';

    dados.forEach(item => {
        const div = document.createElement('div');
        div.className = 'profissao-item';
        div.innerText = item.nome;
        
        div.addEventListener('click', () => {
            document.querySelectorAll('.profissao-item').forEach(d => d.classList.remove('active'));
            div.classList.add('active');
            
            atualizarDashboard(item);
        });

        lista.appendChild(div);
    });
}

// Atualiza a tela principal
function atualizarDashboard(item) {
    // Textos Básicos
    document.getElementById('titulo-profissao').innerText = item.nome;
    document.getElementById('desc-profissao').innerText = item.descricao;
    
    // Card Linha 1
    document.getElementById('info-salario').innerText = item.salario_medio;
    document.getElementById('info-crescimento').innerText = item.crescimento;
    document.getElementById('info-ativos').innerText = item.profissionais_ativos;
    document.getElementById('info-estresse').innerText = item.nivel_estresse;

    // Card Linha 2
    document.getElementById('info-futuro').innerText = item.perspectiva_10_anos;
    document.getElementById('info-formados').innerText = item.formados_ano.toLocaleString('pt-BR');
    document.getElementById('info-demanda').innerText = item.demanda_anual.toLocaleString('pt-BR');

    // --- CÁLCULO DE GAP ---
    const gap = item.demanda_anual - item.formados_ano;
    const elementoGap = document.getElementById('info-gap');

    if (gap > 0) {
        // Déficit
        elementoGap.innerText = `DÉFICIT (Faltam ${gap.toLocaleString('pt-BR')})`;
        elementoGap.style.color = "#00f3ff"; 
    } else if (gap < 0) {
        // Saturado
        const sobra = Math.abs(gap);
        elementoGap.innerText = `SATURADO (Sobram ${sobra.toLocaleString('pt-BR')})`;
        elementoGap.style.color = "#ff4444"; 
    } else {
        elementoGap.innerText = "EQUILIBRADO";
        elementoGap.style.color = "#fff";
    }

    atualizarGrafico(item);
}

// Gera o Gráfico
function atualizarGrafico(item) {
    const ctx = document.getElementById('meuGrafico').getContext('2d');

    if (chartInstance) {
        chartInstance.destroy();
    }

    const salarioBase = parseFloat(item.salario_medio.replace('R$ ', '').replace('.', ''));
    
    const dadosSalariais = [
        salarioBase * 0.6, // Jr
        salarioBase,       // Pleno
        salarioBase * 1.4, // Senior
        salarioBase * 1.8  // Especialista
    ];

    chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Júnior', 'Pleno', 'Sênior', 'Especialista'],
            datasets: [{
                label: 'Evolução Salarial',
                data: dadosSalariais,
                borderColor: '#00f3ff',
                backgroundColor: 'rgba(0, 243, 255, 0.1)',
                borderWidth: 2,
                pointBackgroundColor: '#fff',
                pointRadius: 5,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    ticks: { color: '#9494a0' },
                    grid: { color: '#333' }
                },
                x: {
                    ticks: { color: '#9494a0' },
                    grid: { display: false }
                }
            }
        }
    });
}