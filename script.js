document.documentElement.classList.add('js');

const revealElements = document.querySelectorAll('.reveal');
const bars = document.querySelectorAll('.bar i');
const themeToggle = document.getElementById('themeToggle');
const year = document.getElementById('year');

if (year) year.textContent = new Date().getFullYear();

const revealAll = () => {
  revealElements.forEach((el) => el.classList.add('show'));
  bars.forEach((bar) => {
    bar.style.width = bar.dataset.width || '0%';
  });
};

if ('IntersectionObserver' in window) {
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

  // Safety fallback: if observer callbacks are blocked/delayed in a browser,
  // reveal all content so sections never remain hidden.
  window.setTimeout(() => {
    if (!document.querySelector('.reveal.show')) {
      revealAll();
    }
  }, 1200);
} else {
  revealAll();
}

let savedTheme = null;
try {
  savedTheme = localStorage.getItem('portfolioTheme');
} catch (error) {
  savedTheme = null;
}
if (savedTheme === 'light') {
  document.body.classList.add('light');
  document.documentElement.classList.remove('dark');
  if (themeToggle) themeToggle.textContent = 'Dark';
}

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const isLight = document.body.classList.toggle('light');
    document.documentElement.classList.toggle('dark', !isLight);
    try {
      localStorage.setItem('portfolioTheme', isLight ? 'light' : 'dark');
    } catch (error) {
      // Ignore storage restrictions (e.g., strict privacy/file protocol).
    }
    themeToggle.textContent = isLight ? 'Dark' : 'Light';
  });
}
