/* Bravaura LLC — site interactions */
(function () {
  "use strict";

  /* ---- Mobile nav toggle ---- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("open");
        toggle.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- FAQ accordion ---- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    if (!q || !a) return;
    q.addEventListener("click", function () {
      var isOpen = item.classList.contains("open");
      // close others
      document.querySelectorAll(".faq-item.open").forEach(function (other) {
        if (other !== item) {
          other.classList.remove("open");
          other.querySelector(".faq-a").style.maxHeight = null;
          other.querySelector(".faq-q").setAttribute("aria-expanded", "false");
        }
      });
      if (isOpen) {
        item.classList.remove("open");
        a.style.maxHeight = null;
        q.setAttribute("aria-expanded", "false");
      } else {
        item.classList.add("open");
        a.style.maxHeight = a.scrollHeight + "px";
        q.setAttribute("aria-expanded", "true");
      }
    });
  });

  /* ---- Contact / booking form ---- */
  /* Submits to Netlify Forms via AJAX so the visitor stays on the page and
     sees an inline confirmation. Netlify emails each submission to Kendal
     (set up under Site settings > Forms > notifications). If the network
     call fails, we fall back to a mailto so no request is ever lost. */
  document.querySelectorAll("form[data-bravaura-form]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    var button = form.querySelector('button[type="submit"]');
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      var get = function (name) {
        var el = form.querySelector('[name="' + name + '"]');
        return el ? el.value.trim() : "";
      };
      var name = get("name") || "there";

      var showOk = function () {
        if (status) {
          status.className = "form-status ok";
          status.textContent = "Thanks, " + name + "! Your request is in — we'll follow up by email within 24 hours with a custom, all-inclusive quote.";
          status.setAttribute("tabindex", "-1");
          status.focus();
        }
        form.reset();
      };

      var showError = function () {
        if (status) {
          status.className = "form-status error";
          status.innerHTML = "Sorry, something went wrong sending that. Please email us directly at <a href=\"mailto:bravaurallc@gmail.com\">bravaurallc@gmail.com</a> or call 908-894-3611.";
          status.setAttribute("tabindex", "-1");
          status.focus();
        }
      };

      if (button) { button.disabled = true; button.textContent = "Sending…"; }

      var body = new URLSearchParams(new FormData(form)).toString();
      fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: body
      }).then(function (res) {
        if (button) { button.disabled = false; button.textContent = "Send My Request"; }
        if (res.ok) { showOk(); } else { showError(); }
      }).catch(function () {
        if (button) { button.disabled = false; button.textContent = "Send My Request"; }
        showError();
      });
    });
  });

  /* ---- Footer year ---- */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
