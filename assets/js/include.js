/* include.js — inject shared header + footer into each page.
   Works over HTTP (deploy environment). On file:// it silently no-ops,
   so local preview should use a small http server. */
(function () {
  'use strict';
  var BASE = '/';

  function inject(placeholderId, url, onDone) {
    var ph = document.getElementById(placeholderId);
    if (!ph) return;
    var x = new XMLHttpRequest();
    x.open = x.open || x.open;
    x.open('GET', BASE + url, true);
    x.onreadystatechange = function () {
      if (x.readyState === 4 && x.status === 200) {
        ph.innerHTML = x.responseText;
        if (onDone) onDone();
      }
    };
    x.send();
  }

  function navToggle() {
    var btn = document.getElementById('navToggle');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      btn.textContent = open ? 'Close' : 'Menu';
    });
  }

  function activeNav() {
    // highlight a nav link when its corresponding homepage category matches
    // (skip on homepage; anchors there resolve on click)
  }

  function year() {
    var y = document.getElementById('year');
    if (y) y.textContent = String(new Date().getFullYear());
  }

  if (window.addEventListener) {
    window.addEventListener('DOMContentLoaded', function () {
      inject('header-placeholder', 'components/header.html', navToggle);
      inject('footer-placeholder', 'components/footer.html', year);
    });
  } else {
    var oldOnload = window.onload;
    window.onload = function () {
      if (oldOnload) oldOnload();
      inject('header-placeholder', 'components/header.html', navToggle);
      inject('footer-placeholder', 'components/footer.html', year);
    };
  }
})();