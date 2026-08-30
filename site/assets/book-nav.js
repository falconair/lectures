/* In-app chapter navigation for JupyterLite notebook pages.
 *
 * JupyterLite serves each notebook as an isolated URL with no notion of what
 * book it belongs to or what comes next. This reads the ?path= parameter,
 * looks it up in the generated nav index, and renders a slim bar giving the
 * reader their position and a way onward.
 *
 * Injected into the app shell at build time; the notebooks themselves are
 * untouched.
 */
(function () {
  var BASE = (window.__BOOK_BASE__ || "/");

  function param(name) {
    var m = new RegExp("[?&]" + name + "=([^&]+)").exec(window.location.search);
    return m ? decodeURIComponent(m[1]) : null;
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.textContent = text;
    return e;
  }

  function link(href, cls, text) {
    var a = el("a", cls, text);
    a.href = href;
    return a;
  }

  function render(info) {
    var bar = el("nav", "book-nav");

    var left = el("div", "bn-left");
    left.appendChild(link(BASE + "index.html", "bn-home", "All books"));
    left.appendChild(el("span", "bn-sep", "/"));
    left.appendChild(link(BASE + "books/" + info.bookId + ".html", "bn-book", info.book));
    bar.appendChild(left);

    var mid = el("div", "bn-mid", "Chapter " + info.n + " of " + info.of);
    bar.appendChild(mid);

    var right = el("div", "bn-right");
    if (info.prev) {
      var p = link(BASE + info.prev.url, "bn-prev", "← " + info.prev.title);
      p.title = info.prev.title;
      right.appendChild(p);
    }
    if (info.next) {
      var n = link(BASE + info.next.url, "bn-next", info.next.title + " →");
      n.title = info.next.title;
      right.appendChild(n);
    }
    bar.appendChild(right);

    document.body.appendChild(bar);
    document.body.classList.add("has-book-nav");
  }

  var path = param("path");
  if (!path) return;

  fetch(BASE + "book-nav.json")
    .then(function (r) { return r.json(); })
    .then(function (index) {
      var info = index[path];
      if (info) render(info);
    })
    .catch(function () { /* nav is an enhancement; never break the notebook */ });
})();
