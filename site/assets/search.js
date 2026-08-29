/* Client-side chapter search for the landing page.
 * Substring match over chapter titles and indexed prose; titles rank first. */
(function () {
  var box = document.getElementById("q");
  var out = document.getElementById("results");
  if (!box || !out) return;

  var docs = [];
  fetch("search.json")
    .then(function (r) { return r.json(); })
    .then(function (d) { docs = d; })
    .catch(function () { box.placeholder = "Search unavailable"; });

  function run() {
    var q = box.value.trim().toLowerCase();
    out.innerHTML = "";
    if (q.length < 2) return;

    var hits = [];
    for (var i = 0; i < docs.length; i++) {
      var d = docs[i];
      var inTitle = d.t.toLowerCase().indexOf(q) !== -1;
      var inText = !inTitle && d.x.indexOf(q) !== -1;
      if (inTitle || inText) hits.push({ d: d, rank: inTitle ? 0 : 1 });
    }
    hits.sort(function (a, b) { return a.rank - b.rank; });

    hits.slice(0, 25).forEach(function (h) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = h.d.u;
      a.textContent = h.d.t;
      var s = document.createElement("span");
      s.className = "in-book";
      s.textContent = h.d.b;
      a.appendChild(s);
      li.appendChild(a);
      out.appendChild(li);
    });

    if (!hits.length) {
      var li = document.createElement("li");
      li.style.padding = ".6rem .3rem";
      li.style.color = "var(--muted)";
      li.textContent = "No chapters match “" + box.value.trim() + "”";
      out.appendChild(li);
    }
  }

  box.addEventListener("input", run);
})();
