// Criação da página do Calendário

const modal = document.getElementById("calendário-container");

// Criação do Calendário
const date = new Date();

// Função que renderiza o calendário
const renderCalendar = () => {
  // Ajusta o primeiro dia do mês
  date.setDate(1);

  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate(); // Último dia do mês atual
  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate(); // Último dia do mês anterior
  const firstDayIndex = date.getDay(); // Índice do primeiro dia da semana
  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay(); // Índice do último dia da semana
  const prevDays = firstDayIndex; // Quantos dias do mês anterior mostrar

  const months = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
  ];

  // Atualiza o título do mês e do ano no calendário
  document.querySelector(".date h1").innerHTML = months[date.getMonth()];
  document.querySelector(".date p").innerHTML = date.getFullYear();

  let days = "";

  // Mostrar os dias do mês anterior, se houver espaço no início
  for (let x = prevLastDay - prevDays + 1; x <= prevLastDay; x++) {
    days += `<div class="prev-date">${x}</div>`; // Dias do mês anterior
  }

  // Mostrar os dias do mês atual
  for (let i = 1; i <= lastDay; i++) {
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();

    // Adiciona classes para os dias passados, o dia de hoje e outros dias
    if (
      date.getMonth() < currentMonth ||
      date.getFullYear() < currentYear ||
      (date.getMonth() === currentMonth && i < currentDate.getDate())
    ) {
      days += `<div class="passado">${i}</div>`;
    } else if (
      i === currentDate.getDate() &&
      date.getMonth() === currentMonth
    ) {
      days += `<div class="today">${i}</div>`;
    } else {
      days += `<div>${i}</div>`;
    }
  }

  // Atualiza os dias visíveis no mês
  monthDays.innerHTML = days;
};

// Impede a navegação para o ano anterior ou ano seguinte
document.querySelector(".prev").addEventListener("click", () => {
  // Restringe a navegação ao ano atual
  if (date.getFullYear() === new Date().getFullYear()) {
    // Somente altera o mês, não o ano
    if (date.getMonth() > 0) {
      date.setMonth(date.getMonth() - 1); // Vai para o mês anterior
      renderCalendar();
    }
  }
});

document.querySelector(".next").addEventListener("click", () => {
  // Restringe a navegação ao ano atual
  if (date.getFullYear() === new Date().getFullYear()) {
    // Somente altera o mês, não o ano
    if (date.getMonth() < 11) {
      date.setMonth(date.getMonth() + 1); // Vai para o mês seguinte
      renderCalendar();
    }
  }
});

// Adiciona um evento de clique ao calendário que verifica se o dia clicado é válido
document.querySelector(".days").addEventListener("click", function (e) {
  const clickedDay = e.target;
  const currentDate = new Date();
  const currentDay = currentDate.getDate();
  const currentMonth = currentDate.getMonth(); // Mês atual
  const currentYear = currentDate.getFullYear(); // Ano atual

  const clickedDayNumber = parseInt(clickedDay.innerText); // Número do dia clicado
  const clickedDayClass = clickedDay.classList; // Classes do dia clicado

  // Verifica se o dia clicado é do mês anterior ou de meses anteriores
  const isPreviousMonth = clickedDayClass.contains("prev-date");
  const isPastDay = clickedDayClass.contains("passado");

  // Se o dia clicado for do mês anterior ou um dia passado, não faz nada
  if (
    isPreviousMonth || // Verifica se o dia é do mês anterior
    isPastDay || // Verifica se o dia é passado no mês atual
    (currentYear === date.getFullYear() &&
      currentMonth === date.getMonth() &&
      clickedDayNumber < currentDay) // Verifica se o dia é anterior ao dia atual
  ) {
    // Se for um dia inválido (passado ou mês anterior), não faz nada
    return; // Aqui a função retorna e **não abre** a janela de horários
  }

  // Caso contrário, abre a janela de horários
  openModalHorario();
});

// Inicializa o calendário com o mês atual
renderCalendar();

// Função para abrir o modal de horários
function openModalHorario() {
  const modal = document.getElementById("horarios-container");

  modal.classList.add("abrir");

  modal.addEventListener("click", (e) => {
    if (e.target.id == "horarios-container" || e.target.id == "fechar") {
      modal.classList.remove("abrir");
    }
  });

  // Adiciona eventos de clique aos botões de horários
  const botoesHorario = document.querySelectorAll(".botao-horario");
  botoesHorario.forEach((botao) => {
    botao.addEventListener("click", () => {
      modal.classList.remove("abrir"); // Fecha o modal de horários
      openModalAgendamento(); // Abre o modal de confirmação de agendamento
    });
  });
}
//
// Evento de clique no horário escolhido abrir modal de confirmação de agendamento

// document
//   .querySelector(".botao-horario")
//   .addEventListener("click", function (e) {
//     const clickedHorario = e.target;
//     const clickedHorarioClass = clickedHorario.classList; // Classes do horario clicado
//     const isBotaoHorario = clickedHorarioClass.contains("botao-horario");

//     if (isBotaoHorario)
//       // Abre a janela de Confirmação de Agendamento
//       return openModalAgendamento();
//   });
// //

// // Função para abrir o modal de confirmação de agendamento
// function openModalAgendamento() {
//   const modal = document.getElementById("confirmação-container");
//   modal.classList.add("abrir");

//   modal.addEventListener("click", (e) => {
//     if (e.target.id == "confirmação-container" || e.target.id == "fechar") {
//       modal.classList.remove("abrir");
//       localStorage.fechaModal = "confirmação-container";
//     }
//   });
// }
