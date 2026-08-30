/* In-app book chrome for JupyterLite notebook pages.
 *
 * JupyterLite serves each notebook as an isolated URL with no notion of what
 * book it belongs to or what comes next. This reads the ?path= parameter,
 * looks it up in the generated nav index, and adds three things:
 *
 *   - a slim top bar giving the reader their position and a way onward
 *   - a left sidebar listing the book's chapters, current one marked
 *   - a right sidebar listing the current chapter's headings
 *
 * All of it is injected into the app shell at build time; the notebooks
 * themselves are untouched, and nothing here reaches into JupyterLab's
 * internals. If any of it throws, the notebook still works.
 *
 * The chapter table of contents is read from the rendered DOM rather than
 * generated at build time. That is safe here because the notebook's
 * windowingMode is "contentVisibility", which keeps every cell in the document
 * and merely skips painting the offscreen ones — so all headings are
 * queryable, and each one is a real scroll target.
 */
(function () {
  var BASE = window.__BOOK_BASE__ || "/";
  var PREF_KEY = "book-sidebars";

  function param(name) {
    var m = new RegExp("[?&]" + name + "=([^&]+)").exec(window.location.search);
    return m ? decodeURIComponent(m[1]) : null;
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function link(href, cls, text) {
    var a = el("a", cls, text);
    a.href = href;
    return a;
  }

  /* Reader preferences. Wrapped because localStorage throws outright in some
     privacy modes rather than merely returning null. */
  function prefs() {
    try { return JSON.parse(localStorage.getItem(PREF_KEY)) || {}; }
    catch (e) { return {}; }
  }
  function setPref(k, v) {
    try {
      var p = prefs(); p[k] = v;
      localStorage.setItem(PREF_KEY, JSON.stringify(p));
    } catch (e) { /* choice just won't persist */ }
  }

  function applyPref(side, hidden) {
    document.body.classList.toggle("bn-hide-" + side, !!hidden);
  }

  /* JupyterLab's windowed notebook panel measures its width once and caches
     it. Moving the shell's left/right edges with CSS does not tell it to
     re-measure, so the reading column stays centred on the box it saw at boot
     — visibly off-centre once a sidebar appears. A resize event is the
     supported way to make it re-measure. */
  function reflow() {
    try { window.dispatchEvent(new Event("resize")); } catch (e) {}
  }

  /* The panel may not exist yet when the chrome is injected, and it re-lays
     out as the notebook mounts, so nudge it a few times rather than once. */
  function reflowUntilMounted() {
    var tries = 0;
    reflow();
    var t = setInterval(function () {
      reflow();
      if (++tries > 6 || document.querySelector(".jp-WindowedPanel-outer")) {
        if (tries > 6) clearInterval(t);
      }
      if (tries > 6) clearInterval(t);
    }, 500);
  }

  /* ---- top bar --------------------------------------------------------- */
  function renderTopBar(info) {
    var bar = el("nav", "book-nav");

    var left = el("div", "bn-left");
    left.appendChild(toggle("left", "☰", "Show or hide the chapter list"));
    left.appendChild(link(BASE + "index.html", "bn-home", "All books"));
    bar.appendChild(left);

    bar.appendChild(el("div", "bn-mid", "Chapter " + info.n + " of " + info.of));

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
    right.appendChild(toggle("right", "≡", "Show or hide this chapter's contents"));
    bar.appendChild(right);

    document.body.appendChild(bar);
    document.body.classList.add("has-book-nav");
  }

  function toggle(side, glyph, label) {
    var b = el("button", "bn-toggle bn-toggle-" + side, glyph);
    b.title = label;
    b.setAttribute("aria-label", label);
    b.addEventListener("click", function () {
      var hidden = !document.body.classList.contains("bn-hide-" + side);
      applyPref(side, hidden);
      setPref(side, hidden);
      reflow();
    });
    return b;
  }

  /* ---- left: the book's chapters --------------------------------------- */
  function renderBookSidebar(book, currentPath) {
    var aside = el("aside", "bn-side bn-side-left");
    aside.appendChild(el("div", "bn-side-title", book.title));

    var ol = el("ol", "bn-chapters");
    book.chapters.forEach(function (ch, i) {
      var li = el("li", ch.path === currentPath ? "bn-current" : null);
      var a = link(BASE + ch.url, "bn-chapter");
      a.appendChild(el("span", "bn-num", String(i + 1)));
      a.appendChild(el("span", "bn-chapter-title", ch.title));
      li.appendChild(a);
      ol.appendChild(li);
    });
    aside.appendChild(ol);
    document.body.appendChild(aside);
    document.body.classList.add("has-bn-left");
  }

  /* ---- right: this chapter's headings ---------------------------------- */
  function scroller() {
    return document.querySelector(".jp-WindowedPanel-outer") ||
           document.querySelector(".jp-Notebook");
  }

  function headings() {
    return [].slice.call(document.querySelectorAll(
      ".jp-MarkdownCell .jp-RenderedHTMLCommon h1," +
      ".jp-MarkdownCell .jp-RenderedHTMLCommon h2," +
      ".jp-MarkdownCell .jp-RenderedHTMLCommon h3," +
      ".jp-MarkdownCell .jp-RenderedHTMLCommon h4"));
  }

  function headingText(h) {
    // JupyterLab appends an anchor link to every heading; drop it.
    return (h.textContent || "").replace(/¶\s*$/, "").trim();
  }

  function renderChapterToc() {
    var aside = el("aside", "bn-side bn-side-right");
    aside.appendChild(el("div", "bn-side-title", "On this page"));
    var ol = el("ol", "bn-toc");
    aside.appendChild(ol);
    document.body.appendChild(aside);
    document.body.classList.add("has-bn-right");

    var entries = [];

    function build() {
      var hs = headings().filter(function (h) { return headingText(h); });
      // The first h1 is the chapter title, already shown in the top bar and
      // as the page's own heading; listing it again adds nothing.
      if (hs.length && hs[0].tagName === "H1") hs = hs.slice(1);

      ol.textContent = "";
      entries = hs.map(function (h) {
        var li = el("li", "bn-toc-" + h.tagName.toLowerCase());
        var a = el("a", "bn-toc-link", headingText(h));
        a.href = "#";
        a.addEventListener("click", function (ev) {
          ev.preventDefault();
          var s = scroller();
          if (!s) return;
          // scrollIntoView would put the heading under the fixed top bar
          s.scrollTop += h.getBoundingClientRect().top -
                         s.getBoundingClientRect().top - 12;
        });
        li.appendChild(a);
        ol.appendChild(li);
        return { h: h, a: a };
      });
      var empty = entries.length === 0;
      if (document.body.classList.contains("bn-empty-right") !== empty) {
        document.body.classList.toggle("bn-empty-right", empty);
        reflow();
      }
      highlight();
    }

    function highlight() {
      var s = scroller();
      if (!s || !entries.length) return;
      var top = s.getBoundingClientRect().top;
      var active = entries[0];
      entries.forEach(function (e) {
        if (e.h.getBoundingClientRect().top - top <= 24) active = e;
      });
      entries.forEach(function (e) {
        e.a.classList.toggle("bn-active", e === active);
      });
    }

    // Markdown cells render asynchronously and a reader can add or edit them,
    // so rebuild on change rather than once at load. Debounced: rendering a
    // notebook fires a great many mutations.
    var timer = null;
    function schedule() {
      clearTimeout(timer);
      timer = setTimeout(build, 250);
    }

    var host = document.querySelector(".jp-Notebook") || document.body;
    try {
      new MutationObserver(schedule).observe(host, { childList: true, subtree: true });
    } catch (e) { /* fall back to the initial build */ }

    var s = scroller();
    if (s) s.addEventListener("scroll", highlight, { passive: true });
    // the scroller does not exist until the notebook mounts
    if (!s) setTimeout(function () {
      var later = scroller();
      if (later) later.addEventListener("scroll", highlight, { passive: true });
    }, 3000);

    build();
  }

  /* ---- go --------------------------------------------------------------- */
  var path = param("path");
  if (!path) return;

  fetch(BASE + "book-nav.json")
    .then(function (r) { return r.json(); })
    .then(function (nav) {
      var info = nav.chapters && nav.chapters[path];
      if (!info) return;
      var p = prefs();
      applyPref("left", p.left);
      applyPref("right", p.right);
      renderTopBar(info);
      var book = nav.books && nav.books[info.bookId];
      if (book) renderBookSidebar(book, path);
      renderChapterToc();
      reflowUntilMounted();
    })
    .catch(function () { /* chrome is an enhancement; never break the notebook */ });
})();
