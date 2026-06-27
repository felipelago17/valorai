/* ValorAI — Chart.js global defaults.
   Charts are initialised inline on individual pages via immediately-invoked
   functions that guard against Chart.js not yet being loaded. */
document.addEventListener('DOMContentLoaded', function () {
  if (typeof Chart === 'undefined') return;
  Chart.defaults.font.family =
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.plugins.legend.position = 'bottom';
  Chart.defaults.plugins.tooltip.mode = 'index';
  Chart.defaults.animation.duration = 400;
});
