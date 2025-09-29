# 🖥️ Projeto MVP Back-End - Agendamento para o NAF

## 📖 Sobre o Projeto

Este é um **MVP (Minimum Viable Product)** de agendamento web responsivo, desenvolvido como projeto final da faculdade.

O grupo desse projeto é formado por apenas 1 pessoa: Carina Guida Graça Quintella.

O objetivo principal é criar uma solução digital que permita o agendamento eficiente e conveniente de atendimentos do **Núcleo de Apoio Fiscal e Contábil (NAF)** da **UNIFESO**.

### 🎯 O Desafio

O desafio consiste em desenvolver um website que simplifique o processo de agendamento para os cidadãos que necessitam de assistência com suas declarações de **Imposto de Renda** e outros serviços oferecidos pelo NAF.

### 🗓️ Planejamento

O planejamento foi realizado utilizando uma planilha no Excel baseada na metodologia **Kanban**, detalhando as funcionalidades e requisitos a serem implementados semanalmente.

### 🛠️ Ferramentas Utilizadas

- **Framework**: Django
- **Biblioteca**: FullCalendar
- **Editor de Código**: Visual Studio Code
- **Linguagens Front-End**: HTML, CSS e JavaScript
- **Linguagens Back-End**: Python

---

## 👥 Atores Envolvidos

- **Estudantes e Professores da Unifeso**: Responsáveis pelos atendimentos no NAF. Os estudantes atuarão sob supervisão de professores.
- **População Local e Regiões Próximas**: Cidadãos que buscam assistência fiscal e contábil. Eles poderão acessar o site, visualizar horários disponíveis e agendar atendimentos.
- **Administração do NAF**: Gerenciará o sistema de agendamento e supervisionará a distribuição eficiente dos atendimentos.

---

## 🛡️ Objetivo Geral

Desenvolver uma ferramenta digital para que a população local e de regiões próximas possa agendar serviços do NAF, com foco principal na declaração do **Imposto de Renda**.

---

## Objetivos Específicos / Requisitos

### **Requisitos Funcionais** (em ordem decrescente de prioridade)

- **[RF01]**: O sistema deve apresentar horários disponíveis e permitir o agendamento presencial dos serviços do NAF.
- **[RF02]**: Administradores do NAF devem configurar a disponibilidade de atendimentos e horários de funcionamento.
- **[RF03]**: Professores e estudantes devem visualizar e acessar dados relevantes dos serviços prestados.
- **[RF04]**: O sistema deve registrar dados do usuário (nome, e-mail e serviço solicitado) para validação do agendamento.
- **[RF05]**: O sistema deve permitir feedback dos usuários:
  - **[RF05.1]**: Feedback na própria página.
  - **[RF05.2]**: Notificação automática por e-mail com link para avaliação, enviada 2 horas após o atendimento.
- **[RF06]**: Notificações automáticas por e-mail para confirmar e lembrar os usuários sobre os agendamentos.

### **Requisitos Não-Funcionais** (em ordem decrescente de prioridade)

- **[RNF01]**: Conformidade com a **RGPD** (Regulamento Geral de Proteção de Dados).
- **[RNF02]**: Garantir a segurança e privacidade das informações dos usuários.
- **[RNF03]**: Alta disponibilidade do sistema (24/7), com manutenções programadas e rápidas.
- **[RNF04]**: Suporte a múltiplos usuários simultaneamente.
- **[RNF05]**: Interface amigável, responsiva para todos os tamanhos de tela, intuitiva e com design atraente.
- **[RNF06]**: Tempo de resposta inferior a 5 segundos.

---

## 💻 Tecnologias Utilizadas

- **HTML, CSS e JavaScript** (Front-End)
- **Python e Django** (Back-End)

---

## 🚀 Instruções para Executar o MVP

1. Para executar a página localmente se deve copiar todos os códigos e usá-los no editor de códigos de sua preferência ou clonar o repositório;

2. Deve-se instalar o Django (pip install Django);

3. Criar um superuser;

4. Adicionar nos grupos do Django admin: Alunos, Professores e Administradores;

5. Criar usuários para estes grupos;

6. Criar os serviços.

---

## 🏁 Conclusão

Como este projeto é um **MVP**, produto mínimo viável, muitas funcionalidades podem ser incrementadas para transformar o sistema em uma solução completa para uso real. Com base na viabilidade e no interesse do público-alvo, espera-se refinar e expandir o projeto futuramente.
