const openAbout = document.getElementById("open_about");
const about_modal_container = document.getElementById("about_modal_container");
const about_close = document.getElementById("about_close");

const openContact = document.getElementById("open_contact");
const contact_modal_container = document.getElementById("contact_modal_container");
const contact_close = document.getElementById("contact_close");


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