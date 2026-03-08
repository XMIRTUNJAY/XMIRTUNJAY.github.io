const revealElements = document.querySelectorAll('.reveal');
const yearNode = document.getElementById('year');
const themeToggle = document.getElementById('themeToggle');

if (yearNode) {
  yearNode.textContent = new Date().getFullYear();
}

if (revealElements.length > 0) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('show');
        }
      });
    },
    { threshold: 0.14 }
  );

  revealElements.forEach((el) => observer.observe(el));
}

const savedTheme = localStorage.getItem('themePreference');
if (savedTheme === 'dark') {
  document.body.classList.add('dark');
  if (themeToggle) themeToggle.textContent = 'Light';
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const isDark = document.body.classList.toggle('dark');
    localStorage.setItem('themePreference', isDark ? 'dark' : 'light');
    themeToggle.textContent = isDark ? 'Light' : 'Dark';
  });
}
