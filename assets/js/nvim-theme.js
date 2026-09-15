(() => {
  const key = "portfolio-nvim-theme";
  let theme = "light";
  try {
    if (localStorage.getItem(key) === "dark") theme = "dark";
  } catch {
    // Theme switching still works when browser storage is unavailable.
  }

  function apply() {
    const dark = theme === "dark";
    document.documentElement.dataset.theme = theme;
    document.querySelector('meta[name="theme-color"]')?.setAttribute(
      "content", dark ? "#282828" : "#fbf1c7"
    );
    const button = document.getElementById("dark-toggle");
    if (button) button.setAttribute("aria-pressed", String(dark));
    const label = document.getElementById("theme-label");
    if (label) label.textContent = `gruvbox · ${theme}`;
  }

  // Apply saved colors before the stylesheet loads to avoid a light flash.
  apply();
  document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("dark-toggle");
    if (!button) return;
    button.hidden = false;
    apply();
    button.addEventListener("click", () => {
      theme = theme === "dark" ? "light" : "dark";
      apply();
      try { localStorage.setItem(key, theme); } catch { /* Optional persistence. */ }
    });
  });
})();
