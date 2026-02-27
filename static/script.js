const openAbout = document.getElementById("open_about");
const about_modal_container = document.getElementById("about_modal_container");
const about_close = document.getElementById("about_close");

const openContact = document.getElementById("open_contact");
const contact_modal_container = document.getElementById("contact_modal_container");
const contact_close = document.getElementById("contact_close");

const openPortfolio = document.getElementById("open_portfolio");
const portfolio_modal_container = document.getElementById("portfolio_modal_container");
const portfolio_close = document.getElementById("portfolio_close");

const openSidebar = document.getElementById("sidebar_button");
const sidebar_display = document.getElementById("sidebar_menu");


/*Open and closes about section*/
openAbout.addEventListener("click", () => {
    about_modal_container.classList.add("show");
})
about_close.addEventListener("click", () => {
    about_modal_container.classList.remove("show");
})

/*Open and closes contact */
openContact.addEventListener("click", () => {
    contact_modal_container.classList.add("show");
})
contact_close.addEventListener("click", () => {
    contact_modal_container.classList.remove("show");
})

/*Open and closes contact */
openPortfolio.addEventListener("click", () => {
    portfolio_modal_container.classList.add("show");
})
portfolio_close.addEventListener("click", () => {
    portfolio_modal_container.classList.remove("show");
})

// Opens the sidebar

openSidebar.addEventListener("click", () => {
    sidebar_display.style.display = "flex"

})