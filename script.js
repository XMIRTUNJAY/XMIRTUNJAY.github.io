document.documentElement.classList.add('js-enabled');

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
      }
    });
  },
  { threshold: 0.15 }
);

document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

const yearNode = document.getElementById('year');
if (yearNode) {
  yearNode.textContent = new Date().getFullYear();
}

const root = document.documentElement;
const toggle = document.getElementById('themeToggle');
const savedTheme = localStorage.getItem('themePreference');

if (savedTheme === 'light') {
  root.classList.remove('dark');
}

if (toggle) {
  toggle.addEventListener('click', () => {
    root.classList.toggle('dark');
    localStorage.setItem('themePreference', root.classList.contains('dark') ? 'dark' : 'light');
  });
}
