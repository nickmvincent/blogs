(() => {
  const input = document.querySelector('#query');
  if (!input) return;
  const results = document.querySelector('#search-results');
  const status = document.querySelector('#search-status');
  let data;
  let version = 0;
  input.addEventListener('input', async () => {
    const current = ++version;
    const query = input.value.trim().toLocaleLowerCase();
    results.replaceChildren();
    status.textContent = '';
    if (!query) return;
    try {
      data ||= fetch('/search-index.json').then(r => { if (!r.ok) throw new Error(); return r.json(); });
      const posts = await data;
      if (current !== version) return;
      const terms = query.split(/\s+/);
      const matches = posts.filter(p => terms.every(t => `${p.title} ${p.summary} ${p.text}`.toLocaleLowerCase().includes(t)));
      status.textContent = `${matches.length} result${matches.length === 1 ? '' : 's'}`;
      for (const post of matches) {
        const row = document.createElement('li');
        const category = document.createElement('div'); category.className = 'list-meta';
        category.textContent = post.section === 'drafts' ? 'Public draft' : 'Archive';
        const content = document.createElement('div');
        const link = document.createElement('a'); link.href = post.url; link.textContent = post.title;
        const excerpt = document.createElement('p'); excerpt.textContent = post.summary || post.text.slice(0, 180);
        content.append(link, excerpt); row.append(category, content); results.append(row);
      }
    } catch {
      if (current === version) status.textContent = 'Search could not load. Browse the Archive or Public drafts instead.';
      data = undefined;
    }
  });
  document.addEventListener('keydown', event => {
    if ((event.key === 'k' && (event.metaKey || event.ctrlKey)) ||
        (event.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName))) {
      event.preventDefault(); input.focus();
    }
  });
})();
