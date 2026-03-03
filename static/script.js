const open_about_topbar = document.getElementById("open_about_topbar");
const open_about_sidebar = document.getElementById("open_about_sidebar");
const about_modal_container = document.getElementById("about_modal_container");
const about_close = document.getElementById("about_close");

const openContact = document.getElementById("open_contact");
const open_contact_sidebar = document.getElementById("open_contact_sidebar")
const contact_modal_container = document.getElementById("contact_modal_container");
const contact_close = document.getElementById("contact_close");

const openGame = document.getElementById("open_game");
const game_modal_container = document.getElementById("games_modal_container");
const game_close = document.getElementById("game_close");

const openPortfolio = document.getElementById("open_portfolio");
const portfolio_modal_container = document.getElementById("portfolio_modal_container");
const portfolio_close = document.getElementById("portfolio_close");

const openSidebar = document.getElementById("sidebar_button");
const sidebar_display = document.getElementById("sidebar_menu");
const closeSidebar = document.getElementById("close_menu");


/*Open and closes about section*/
open_about_topbar.addEventListener("click", () => {
    about_modal_container.classList.add("show");
})
open_about_sidebar.addEventListener("click", () => {
    about_modal_container.classList.add("show");
    sidebar_display.style.display = "none"
})
about_close.addEventListener("click", () => {
    about_modal_container.classList.remove("show");
})

/*Open and closes contact */
openContact.addEventListener("click", () => {
    contact_modal_container.classList.add("show");
})
open_contact_sidebar.addEventListener("click", () => {
    contact_modal_container.classList.add("show")
    sidebar_display.style.display = "none"
})
contact_close.addEventListener("click", () => {
    contact_modal_container.classList.remove("show");
})

/*Open and closes games */
openGame.addEventListener("click", () => {
    game_modal_container.classList.add("show");
})
game_close.addEventListener("click", () => {
    game_modal_container.classList.remove("show");
})

/*Open and closes portfolio */
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
closeSidebar.addEventListener("click", () => {
    sidebar_display.style.display = "none"
})