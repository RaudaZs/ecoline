const T = {
  kk: {
    nav: ['Басты бет','Өнімдер','Түстер','Байланыс'],
    store: '🏪 Дүкен табу',
    cats: ['Фасадтық бояу','Ішкі бояу','Антимороз','Грунтовка','Декоративті','Гидроизоляция'],
    more: 'Толығырақ',
    wa: '📦 WhatsApp тапсырыс',
    viz_btn: '🎨 Визуализаторды ашу',
  },
  ru: {
    nav: ['Главная','Продукты','Цвета','Контакты'],
    store: '🏪 Найти магазин',
    cats: ['Фасадная краска','Интерьерная краска','Антимороз','Грунтовка','Декоративная','Гидроизоляция'],
    more: 'Подробнее',
    wa: '📦 Заказ в WhatsApp',
    viz_btn: '🎨 Открыть визуализатор',
  },
  en: {
    nav: ['Home','Products','Colors','Contact'],
    store: '🏪 Find Store',
    cats: ['Facade Paint','Interior Paint','Anti-Frost','Primer','Decorative','Waterproofing'],
    more: 'Details',
    wa: '📦 WhatsApp Order',
    viz_btn: '🎨 Open Visualizer',
  }
};

function setLang(lang) {
  const t = T[lang];
  if (!t) return;
  localStorage.setItem('ecoLang', lang);

  // Active button
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
  const btn = document.getElementById('lang-' + lang);
  if (btn) btn.classList.add('active');

  // Nav links
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach((el, i) => { if (t.nav[i]) el.textContent = t.nav[i]; });

  // Store button
  const storeBtn = document.querySelector('.btn-store');
  if (storeBtn) storeBtn.innerHTML = t.store;

  // Category names
  const catNames = document.querySelectorAll('.cat-name');
  catNames.forEach((el, i) => { if (t.cats[i]) el.textContent = t.cats[i]; });

  // "Толығырақ" buttons
  document.querySelectorAll('.prod-btn').forEach(el => {
    const span = el.querySelector('span') || el;
    if (span.textContent.trim().match(/Толығырақ|Подробнее|Details/)) {
      span.textContent = t.more;
    } else if (el.textContent.trim().match(/Толығырақ|Подробнее|Details/)) {
      el.textContent = t.more;
    }
  });

  // WhatsApp buttons
  document.querySelectorAll('.btn-wa, .btn-whatsapp').forEach(el => {
    el.innerHTML = t.wa;
  });

  // Visualizer button
  const vizBtn = document.querySelector('.btn-viz, .viz-cta-btn');
  if (vizBtn) vizBtn.innerHTML = t.viz_btn;

  document.documentElement.lang = lang === 'kk' ? 'kk' : lang === 'ru' ? 'ru' : 'en';
}

document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('ecoLang') || 'kk';
  setLang(saved);
});
