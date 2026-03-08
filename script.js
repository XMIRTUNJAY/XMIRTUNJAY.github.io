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

const updateThemeButton = () => {
  if (!toggle) return;
  toggle.textContent = root.classList.contains('data-theme')
    ? 'Switch to AI Builder Theme'
    : 'Switch to Data Engineering Theme';
};

updateThemeButton();

if (toggle) {
  toggle.addEventListener('click', () => {
    if (root.classList.contains('data-theme')) {
      root.classList.remove('data-theme');
      root.classList.add('ai-theme');
      localStorage.setItem('themePreference', 'ai-theme');
    } else {
      root.classList.remove('ai-theme');
      root.classList.add('data-theme');
      localStorage.setItem('themePreference', 'data-theme');
    }
    updateThemeButton();
  });
}

const roleCycle = document.getElementById('roleCycle');
const roleModes = ['AI Builder', 'Data Engineer', 'Pipeline Architect', 'Analytics Automation', 'SLA Orchestrator'];
let roleIndex = 0;

if (roleCycle) {
  setInterval(() => {
    roleIndex = (roleIndex + 1) % roleModes.length;
    roleCycle.style.opacity = '0.15';
    setTimeout(() => {
      roleCycle.textContent = roleModes[roleIndex];
      roleCycle.style.opacity = '1';
    }, 140);
  }, 1800);
}
