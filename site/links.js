const rows = Array.from(document.querySelectorAll("[data-link-row]"));
const searchInput = document.querySelector("#link-search");
const sortSelect = document.querySelector("#link-sort");
const tableBody = document.querySelector("#link-table tbody");
const countLabel = document.querySelector("#link-count");
const reviewToggle = document.querySelector("#show-link-review");

let activeDomain = "";
let activeIssue = "";

function textFor(row, key) {
  return (row.dataset[key] || "").toLowerCase();
}

function applyLinkView() {
  const query = (searchInput?.value || "").toLowerCase().trim();
  const sortKey = sortSelect?.value || "domain";
  const sortedRows = rows.slice().sort((a, b) => {
    const primary = textFor(a, sortKey).localeCompare(textFor(b, sortKey));
    if (primary !== 0) return primary;
    return textFor(a, "article").localeCompare(textFor(b, "article"));
  });

  let visibleCount = 0;
  for (const row of sortedRows) {
    const haystack = `${row.dataset.domain} ${row.dataset.article} ${row.dataset.url} ${row.dataset.label} ${row.dataset.issues} ${row.dataset.findings}`.toLowerCase();
    const matchesQuery = !query || haystack.includes(query);
    const matchesDomain = !activeDomain || row.dataset.domain === activeDomain;
    const issueCodes = (row.dataset.issues || "").split(" ").filter(Boolean);
    const matchesIssue = !activeIssue || issueCodes.includes(activeIssue);
    const visible = matchesQuery && matchesDomain && matchesIssue;
    row.hidden = !visible;
    if (visible) visibleCount += 1;
    tableBody?.appendChild(row);
  }

  if (countLabel) {
    const noun = visibleCount === 1 ? "link" : "links";
    countLabel.textContent = `${visibleCount} ${noun}`;
  }

  for (const button of document.querySelectorAll("[data-domain-filter]")) {
    button.setAttribute("aria-pressed", String((button.getAttribute("data-domain-filter") || "") === activeDomain));
  }
  for (const button of document.querySelectorAll("[data-issue-filter]")) {
    button.setAttribute("aria-pressed", String((button.getAttribute("data-issue-filter") || "") === activeIssue));
  }
}

searchInput?.addEventListener("input", applyLinkView);
sortSelect?.addEventListener("change", applyLinkView);
reviewToggle?.addEventListener("change", () => {
  document.documentElement.classList.toggle("show-link-review", Boolean(reviewToggle.checked));
});

for (const button of document.querySelectorAll("[data-domain-filter]")) {
  button.addEventListener("click", () => {
    const selected = button.getAttribute("data-domain-filter") || "";
    activeDomain = selected === activeDomain ? "" : selected;
    applyLinkView();
  });
}

for (const button of document.querySelectorAll("[data-issue-filter]")) {
  button.addEventListener("click", () => {
    const selected = button.getAttribute("data-issue-filter") || "";
    activeIssue = selected === activeIssue ? "" : selected;
    applyLinkView();
  });
}

applyLinkView();
document.documentElement.classList.toggle("show-link-review", Boolean(reviewToggle?.checked));
