(() => {
  const initNavigation = () => {
    const nav = document.querySelector('.navbar');
    const toggle = document.querySelector('.menu-toggle');
    const links = document.querySelector('.nav-links');
    const dropdown = document.querySelector('.nav-dropdown');

    if (!nav || !toggle || !links) return;

    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', 'primary-navigation');
    links.id = 'primary-navigation';

    const closeMenu = () => {
      links.classList.remove('active');
      toggle.setAttribute('aria-expanded', 'false');
      dropdown?.classList.remove('open');
    };

    const toggleMenu = () => {
      const isOpen = links.classList.toggle('active');
      toggle.setAttribute('aria-expanded', String(isOpen));
      if (!isOpen) dropdown?.classList.remove('open');
    };

    // Capture the click so legacy page-specific menu listeners cannot toggle twice.
    document.addEventListener('click', (event) => {
      if (event.target.closest('.menu-toggle')) {
        event.preventDefault();
        event.stopPropagation();
        toggleMenu();
        return;
      }

      if (window.matchMedia('(max-width: 768px)').matches && event.target.closest('.dropdown-toggle')) {
        event.preventDefault();
        dropdown?.classList.toggle('open');
        return;
      }

      if (window.matchMedia('(max-width: 768px)').matches && event.target.closest('.nav-links a')) {
        closeMenu();
        return;
      }

      if (!nav.contains(event.target)) closeMenu();
    }, true);

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        closeMenu();
        toggle.focus();
      }
    });

    window.addEventListener('resize', () => {
      if (!window.matchMedia('(max-width: 768px)').matches) closeMenu();
    });
  };

  document.addEventListener('DOMContentLoaded', initNavigation);
})();
