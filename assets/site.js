const btn = document.querySelector("[data-menu]");
const nav = document.querySelector("header nav");
if (btn && nav) {
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
}
