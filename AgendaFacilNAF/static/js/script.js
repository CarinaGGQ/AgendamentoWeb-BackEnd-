// Variável global para data
const date = new Date();

// Função que renderiza o calendário
const renderCalendar = () => {
  date.setDate(1);

  const monthDays = document.querySelector(".days");
  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();
  const firstDayIndex = date.getDay();
  const currentDate = new Date();
  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth();
  const currentDay = currentDate.getDate();
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

  document.querySelector(".date h1").innerHTML = months[date.getMonth()];
  document.querySelector(".date p").innerHTML = date.getFullYear();

  let days = "";

  for (let i = 1; i <= lastDay; i++) {
    const isToday =
      i === currentDay &&
      date.getMonth() === currentMonth &&
      date.getFullYear() === currentYear;
    const isPastDay =
      date.getFullYear() < currentYear ||
      (date.getFullYear() === currentYear && date.getMonth() < currentMonth) ||
      (date.getFullYear() === currentYear &&
        date.getMonth() === currentMonth &&
        i < currentDay);

    days += `<div class="${isToday ? "today" : ""} ${
      isPastDay ? "passado" : ""
    }" data-date="${i}/${
      date.getMonth() + 1
    }/${date.getFullYear()}">${i}</div>`;
  }

  monthDays.innerHTML = days;

  // Adicionar eventos de clique aos dias
  document.querySelectorAll(".days div").forEach((day) => {
    const isPastDay = day.classList.contains("passado");

    // Bloqueia dias passados
    if (!isPastDay) {
      day.addEventListener("click", () => {
        const selectedDate = day.dataset.date;
        document.getElementById("selected-date").value = selectedDate;

        // Destaca o dia selecionado
        document
          .querySelectorAll(".days div")
          .forEach((d) => d.classList.remove("selected"));
        day.classList.add("selected");

        // Exibe o modal de horários
        openModalHorario();
      });
    }
  });
};

// Abre o modal de horários
const openModalHorario = () => {
  const modal = document.getElementById("horarios-container");
  modal.classList.add("abrir");

  modal.addEventListener("click", (e) => {
    if (e.target.id == "horarios-container") {
      modal.classList.remove("abrir");
    }
  });
};

// Define o horário selecionado
const setSelectedTime = (button) => {
  const selectedTime = button.dataset.time;
  document.getElementById("selected-time").value = selectedTime;
  // Submete o formulário com a data e horário selecionados
  document.getElementById("agendamento-form").submit();
};

// Navegação do calendário
document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});
document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

// Inicializa o calendário
renderCalendar();

// Valida o serviço selecionado antes de submeter o formulário
const validateForm = () => {
  const servico = document.querySelector('select[name="servico"]').value;

  if (!servico) {
    alert("Por favor, selecione um serviço antes de confirmar.");
    return false; // Impede o envio do formulário
  }

  return true;
};

// Converte data do formato DD/MM/YYYY para YYYY-MM-DD
const formatDateToISO = (date) => {
  const [day, month, year] = date.split("/");
  return `${year}-${month}-${day}`;
};

// Modifica o formulário na página de confirmação para corrigir o formato antes de submeter
document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", (event) => {
    const selectedDateInput = document.querySelector(
      'input[name="selected_date"]'
    );
    if (selectedDateInput) {
      const formattedDate = formatDateToISO(selectedDateInput.value);
      selectedDateInput.value = formattedDate; // Atualiza o valor antes do envio
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", (event) => {
    const nome = document.querySelector("#name").value.trim();
    const servico = document.querySelector("#servico").value.trim();
    const email = document.querySelector("#email").value.trim();
    const feedback = document.querySelector("#feedback").value.trim();

    if (!nome || !servico || !email || !feedback) {
      event.preventDefault(); // Impede o envio do formulário
      alert("Por favor, preencha todos os campos antes de enviar!");
    }
  });
});

// Navegação do calendário
document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});
document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

// Inicializa o calendário
renderCalendar();
