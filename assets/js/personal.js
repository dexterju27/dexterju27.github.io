(() => {
  'use strict';
  document.querySelectorAll('[data-enhanced]').forEach(element => { element.hidden = false; });
  const search = document.querySelector('#paper-search');
  const year = document.querySelector('#paper-year');
  const buttons = [...document.querySelectorAll('[data-topic]')];
  const papers = [...document.querySelectorAll('.paper')];
  let topic = '';
  const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const searchText = new Map(papers.map(p => [p, normalize(p.dataset.search || p.textContent)]));
  function filter() {
    const query = normalize(search.value.trim());
    let count = 0;
    papers.forEach(paper => {
      paper.hidden = !!((topic && !paper.dataset.topics.split(' ').includes(topic)) ||
        (year.value && paper.dataset.year !== year.value) || (query && !searchText.get(paper).includes(query)));
      if (!paper.hidden) count++;
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.topic === topic)));
    document.querySelector('#paper-status').textContent = count + (count === 1 ? ' work' : ' works') + ((query || topic || year.value) ? ' matching your filters' : ' in the collection');
    document.querySelector('#clear-papers').hidden = !(query || topic || year.value);
    document.querySelector('#paper-empty').hidden = count !== 0;
  }
  function reset() { topic = ''; search.value = ''; year.value = ''; filter(); }
  if (search) {
    search.addEventListener('input', filter);
    year.addEventListener('change', filter);
    buttons.forEach(button => button.addEventListener('click', () => { topic = button.dataset.topic; filter(); }));
    document.querySelector('#clear-papers').addEventListener('click', reset);
    document.querySelector('#reset-papers').addEventListener('click', reset);
    filter();
  }
  const navigation = [...document.querySelectorAll('.main-nav a[href^="/#"]')];
  if ('IntersectionObserver' in window && search) {
    const sections = [...document.querySelectorAll('main section[id]')];
    const observer = new IntersectionObserver(entries => {
      entries.filter(entry => entry.isIntersecting).forEach(entry => {
        const target = entry.target.id === 'publications' ? 'research' : entry.target.id;
        navigation.forEach(link => { if (link.hash === '#' + target) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); });
      });
    }, {rootMargin: '-20% 0px -55% 0px'});
    sections.forEach(section => observer.observe(section));
  }
})();
