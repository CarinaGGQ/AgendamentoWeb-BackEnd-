document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');
    let horariosContainer = document.getElementById('horarios-container');
    let btnConfirmar = document.getElementById('btn-confirmar');
    let horariosDiv = document.querySelector('.horarios');

    if (calendarEl) {
        let calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            locale: 'pt-br',
            selectable: true,
            contentHeight: 'auto',  // 🔹 altura automática
            expandRows: true,       // 🔹 força expandir para mostrar todas as semanas
            dateClick: function (info) {
                let selectedDate = info.dateStr;
                document.getElementById('selected-date').value = selectedDate;

                btnConfirmar.style.display = 'none';
                horariosDiv.innerHTML = '';

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

        // 🔹 renderiza
        setTimeout(() => {
            calendar.render();
            calendar.updateSize();
        }, 200);

        // 🔹 responsividade: mantém SEMPRE em mês
        window.addEventListener('resize', function () {
            if (calendarEl.offsetParent !== null) {
                calendar.changeView('dayGridMonth');
                calendar.updateSize();
            }
        });
    }
});

// Seleciona horário
function setSelectedTime(button, dia) {
    let hora = button.getAttribute("data-time");

    document.getElementById("selected-time").value = hora;
    document.getElementById("selected-date").value = dia;

    document.querySelectorAll(".botao-horario").forEach(btn => {
        btn.classList.remove("selecionado");
    });
    button.classList.add("selecionado");

    document.getElementById("btn-confirmar").style.display = "block";
}
