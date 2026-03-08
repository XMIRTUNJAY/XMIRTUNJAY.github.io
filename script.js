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

if (savedTheme === 'light') {
  root.classList.remove('dark');
}

if (toggle) {
  toggle.addEventListener('click', () => {
    root.classList.toggle('dark');
    localStorage.setItem('themePreference', root.classList.contains('dark') ? 'dark' : 'light');
  });
}

const roleCycle = document.getElementById('roleCycle');
const roleModes = ['Data Engineering', 'AI Workflow Builder', 'Pipeline Architect', 'Analytics Automation'];
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
