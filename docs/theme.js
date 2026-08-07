/* Grounded AI Practice — theme switch.
   The stylesheet follows the visitor's system setting by default. This
   script adds a manual override, cycling auto -> light -> dark, because
   some browsers pin the reported scheme regardless of the operating
   system (an explicit browser theme, a hardened configuration) and a
   visitor in that position could otherwise never see the other half of
   the site. The choice is stored on this device (localStorage, one key,
   sent nowhere). Without JavaScript the button stays hidden and the
   site behaves exactly as it did before this file existed. */
(function () {
  "use strict";

  var KEY = "gap-theme";
  var root = document.documentElement;

  function stored() {
    try {
      var v = localStorage.getItem(KEY);
      return v === "light" || v === "dark" ? v : "auto";
    } catch (e) {
      return "auto";
    }
  }

  function store(mode) {
    try {
      if (mode === "auto") localStorage.removeItem(KEY);
      else localStorage.setItem(KEY, mode);
    } catch (e) { /* private mode: the choice just does not persist */ }
  }

  function apply(mode) {
    if (mode === "auto") delete root.dataset.theme;
    else root.dataset.theme = mode;

    /* The dark logo and figure variants are chosen by <source media=...>
       queries, which follow the system setting rather than data-theme.
       An override has to switch them by hand, or the CSS and the images
       part company — an Ink wordmark on an Ink background. */
    var sources = document.querySelectorAll("picture > source[media]");
    for (var i = 0; i < sources.length; i++) {
      var s = sources[i];
      if (!s.dataset.media) s.dataset.media = s.getAttribute("media");
      if (s.dataset.media.indexOf("dark") === -1) continue;
      if (mode === "auto") s.setAttribute("media", s.dataset.media);
      else s.setAttribute("media", mode === "dark" ? "all" : "not all");
    }
  }

  /* Run before first paint so an override never flashes the wrong
     theme. The <picture> pass reruns on DOM ready, because at this
     point in <head> no pictures exist yet. */
  apply(stored());

  document.addEventListener("DOMContentLoaded", function () {
    apply(stored());

    var button = document.getElementById("theme-toggle");
    if (!button) return;

    var ORDER = ["auto", "light", "dark"];

    function label(mode) { button.textContent = "Theme: " + mode; }

    label(stored());
    button.hidden = false;

    button.addEventListener("click", function () {
      var next = ORDER[(ORDER.indexOf(stored()) + 1) % ORDER.length];
      store(next);
      apply(next);
      label(next);
    });
  });
}());
