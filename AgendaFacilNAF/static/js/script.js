document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');
    let horariosContainer = document.getElementById('horarios-container');
    let btnConfirmar = document.getElementById('btn-confirmar');
    let horariosDiv = document.querySelector('.horarios');

    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'pt-br',
        selectable: true,
        dateClick: function (info) {
            let selectedDate = info.dateStr;
            document.getElementById('selected-date').value = selectedDate;

            // Esconde botão de confirmar até escolher horário
            btnConfirmar.style.display = 'none';

            // Limpa horários antigos
            horariosDiv.innerHTML = '';

            // Requisição AJAX para obter horários disponíveis
            fetch(`/horarios_disponiveis/?data=${selectedDate}`)
                .then(response => response.json())
                .then(data => {
                    if (data.length === 0) {
                        horariosDiv.innerHTML = '<p>Nenhum horário disponível no momento.</p>';
                    } else {
                        data.forEach(item => {
                            let btn = document.createElement('button');
                            btn.type = 'button';
                            btn.className = 'botao-horario';
                            btn.setAttribute('data-time', item.hora);
                            btn.textContent = item.label;
                            btn.onclick = function () { setSelectedTime(this, selectedDate); };
                            horariosDiv.appendChild(btn);
                        });
                    }
                    horariosContainer.style.display = 'block';
                })
                .catch(err => {
                    console.error('Erro ao carregar horários:', err);
                    horariosDiv.innerHTML = '<p>Erro ao carregar horários.</p>';
                    horariosContainer.style.display = 'block';
                });
        }
    });

    calendar.render();
});

// Função chamada ao clicar em um botão de horário
function setSelectedTime(button, dia) {
    let hora = button.getAttribute("data-time");

    // Preenche os inputs hidden do formulário
    document.getElementById("selected-time").value = hora;

    // 'dia' já vem no formato YYYY-MM-DD, não precisa formatar para DD/MM/YYYY
    document.getElementById("selected-date").value = dia;

    // Marca visualmente o horário selecionado
    document.querySelectorAll(".botao-horario").forEach(btn => {
        btn.classList.remove("selecionado");
    });
    button.classList.add("selecionado");

    // Mostra o botão de confirmar
    document.getElementById("btn-confirmar").style.display = "block";
}
