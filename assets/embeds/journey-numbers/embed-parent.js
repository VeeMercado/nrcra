// Resizes the Journey numbers iframe to fit its content.
// Include once on any page that embeds assets/embeds/journey-numbers/index.html in an iframe with id="journey-numbers".
(function () {
  window.addEventListener("message", function (e) {
    var d = e.data;
    if (!d || d.type !== "nrcra-embed-height") return;
    var f = document.getElementById(d.id);
    if (f && e.source === f.contentWindow) f.style.height = d.height + "px";
  });
})();
