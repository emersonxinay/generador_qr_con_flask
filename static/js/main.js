
document.addEventListener('DOMContentLoaded', function () {
  const body = document.body;
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');

  // Cargar tema desde localStorage si está almacenado
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    setTheme(savedTheme);
  }

  // Evento de cambio del interruptor de modo nocturno/diurno
  themeToggle.addEventListener('change', function () {
    const theme = this.checked ? 'dark' : 'light';
    setTheme(theme);
    // Almacenar el estado del tema en localStorage
    localStorage.setItem('theme', theme);
  });

  // Evento de clic en el ícono de noche y día
  themeIcon.addEventListener('click', function () {
    const currentTheme = body.classList.contains('dark') ? 'light' : 'dark';
    setTheme(currentTheme);
    // Almacenar el estado del tema en localStorage
    localStorage.setItem('theme', currentTheme);
  });

  function setTheme(theme) {
    body.classList.remove('dark', 'light');
    body.classList.add(theme);
    themeIcon.innerHTML = theme === 'dark' ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
    themeToggle.checked = theme === 'dark';
  }
});