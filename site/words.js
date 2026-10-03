const rows = Array.from(document.querySelectorAll("[data-word-row]"));
const searchInput = document.querySelector("#word-search");
const sortSelect = document.querySelector("#word-sort");
const tableBody = document.querySelector("#word-table tbody");
const countLabel = document.querySelector("#word-count");

let activeNgram = "";

function lowerText(row, key) {
  return (row.dataset[key] || "").toLowerCase();
}

function numberValue(row, key) {
  return Number.parseInt(row.dataset[key] || "0", 10) || 0;
}

function compareRows(a, b, sortKey) {
  if (sortKey === "phrase") {
    return lowerText(a, "phrase").localeCompare(lowerText(b, "phrase"));
  }
  if (sortKey === "type") {
    const byType = numberValue(a, "ngram") - numberValue(b, "ngram");
    if (byType !== 0) return byType;
    return numberValue(b, "count") - numberValue(a, "count");
  }
  if (sortKey === "article-count") {
    const byArticleCount = numberValue(b, "articleCount") - numberValue(a, "articleCount");
    if (byArticleCount !== 0) return byArticleCount;
    return numberValue(b, "count") - numberValue(a, "count");
  }
  if (sortKey === "top-article") {
    const byArticle = lowerText(a, "topArticle").localeCompare(lowerText(b, "topArticle"));
    if (byArticle !== 0) return byArticle;
    return numberValue(b, "count") - numberValue(a, "count");
  }
  const byCount = numberValue(b, "count") - numberValue(a, "count");
  if (byCount !== 0) return byCount;
  return lowerText(a, "phrase").localeCompare(lowerText(b, "phrase"));
}

function applyWordView() {
  const query = (searchInput?.value || "").toLowerCase().trim();
  const sortKey = sortSelect?.value || "count";
  const sortedRows = rows.slice().sort((a, b) => compareRows(a, b, sortKey));

  let visibleCount = 0;
  for (const row of sortedRows) {
    const haystack = `${row.dataset.phrase} ${row.dataset.type} ${row.dataset.topArticle}`.toLowerCase();
    const matchesQuery = !query || haystack.includes(query);
    const matchesType = !activeNgram || row.dataset.ngram === activeNgram;
    const visible = matchesQuery && matchesType;
    row.hidden = !visible;
    if (visible) visibleCount += 1;
    tableBody?.appendChild(row);
  }

  if (countLabel) {
    const noun = visibleCount === 1 ? "term" : "terms";
    countLabel.textContent = `${visibleCount} ${noun}`;
  }

  for (const button of document.querySelectorAll("[data-ngram-filter]")) {
    button.setAttribute("aria-pressed", String((button.getAttribute("data-ngram-filter") || "") === activeNgram));
  }
}

searchInput?.addEventListener("input", applyWordView);
sortSelect?.addEventListener("change", applyWordView);

for (const button of document.querySelectorAll("[data-ngram-filter]")) {
  button.addEventListener("click", () => {
    const selected = button.getAttribute("data-ngram-filter") || "";
    activeNgram = selected === activeNgram ? "" : selected;
    applyWordView();
  });
}

applyWordView();
