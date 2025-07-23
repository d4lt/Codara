const noticias = [
    {
      titulo: "Curso de Letramento Digital",
      texto: "Inscrições abertas para o curso gratuito voltado a comunidades indígenas. Início em agosto!"
    },
    {
      titulo: "Workshop de Produção digital",
      texto: "Aprenda a produzir conteúdo digital básico com celular. Evento online no dia 25/07."
    },
    {
      titulo: "Bolsa para Jovens Líderes Indígenas",
      texto: "Iniciativa de capacitação e mentoria em tecnologia. Inscreva-se até 30/07."
    }
  ];
  
  const listaNoticias = document.getElementById("lista-noticias");
  
  noticias.forEach(n => {
    const card = document.createElement("div");
    card.className = "noticia-card";
    card.innerHTML = `<h3>${n.titulo}</h3><p>${n.texto}</p>`;
    listaNoticias.appendChild(card);
  });
  
  // Formulário
  document.getElementById('form-contato').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const nome = document.getElementById('nome da comunidade').value.trim();
    const email = document.getElementById('localização').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();
  
    if (nome && email && mensagem) {
      document.getElementById('mensagem-envio').textContent = "Mensagem enviada com sucesso!";
      this.reset();
    } else {
      document.getElementById('mensagem-envio').textContent = "Preencha todos os campos corretamente.";
    }
  });
  