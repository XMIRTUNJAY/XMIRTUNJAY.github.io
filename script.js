const revealElements = document.querySelectorAll('.reveal');
const bars = document.querySelectorAll('.bar i');
const themeToggle = document.getElementById('themeToggle');
const year = document.getElementById('year');

if (year) year.textContent = new Date().getFullYear();

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
        if (entry.target.id === 'skills') {
          bars.forEach((bar) => {
            bar.style.width = bar.dataset.width || '0%';
          });
        }
      }
    });
  },
  { threshold: 0.2 }
);

revealElements.forEach((el) => revealObserver.observe(el));

const savedTheme = localStorage.getItem('portfolioTheme');
if (savedTheme === 'light') {
  document.body.classList.add('light');
  document.documentElement.classList.remove('dark');
  if (themeToggle) themeToggle.textContent = 'Dark';
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const isLight = document.body.classList.toggle('light');
    document.documentElement.classList.toggle('dark', !isLight);
    localStorage.setItem('portfolioTheme', isLight ? 'light' : 'dark');
    themeToggle.textContent = isLight ? 'Dark' : 'Light';
  });
}
