const revealElements = document.querySelectorAll('.reveal');

if (revealElements.length > 0) {
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

  revealElements.forEach((el) => observer.observe(el));
}

const yearNode = document.getElementById('year');
if (yearNode) {
  yearNode.textContent = new Date().getFullYear();
}

const root = document.documentElement;
const toggle = document.getElementById('themeToggle');
const savedTheme = localStorage.getItem('themePreference');

if (savedTheme === 'data-theme') {
  root.classList.remove('ai-theme');
  root.classList.add('data-theme');
}

if (toggle) {
  toggle.addEventListener('click', () => {
    root.classList.toggle('dark');
    localStorage.setItem('themePreference', root.classList.contains('dark') ? 'dark' : 'light');
  });
}
