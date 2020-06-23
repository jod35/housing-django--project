const nav = document.querySelector("nav");
const navbar_items = document.querySelectorAll(".nav-link");
const logo_area = document.querySelector(".logo");
const dropdown_menu = document.querySelector(".drop-down");
const dropdown_link = document.getElementById("buy-btn");

window.onscroll = function () {
  shrinkOnscroll();
};

function shrinkOnscroll() {
  if (
    document.body.scrollTop > 100 ||
    document.documentElement.scrollTop > 100
  ) {
    nav.style.backgroundColor = "rgb(219, 30, 30)";
    nav.style.color = "white";
    nav.style.padding = "10px";

    logo_area.style.color = "white";

    for (let i = 0; i < navbar_items.length; i++) {
      navbar_items[i].style.color = "white";
    }
  } else {
    nav.style.backgroundColor = "white";
    logo_area.style.color = "rgb(219, 30, 30)";
    nav.style.padding = "20px";
    for (let i = 0; i < navbar_items.length; i++) {
      navbar_items[i].style.color = "rgb(219, 30, 30)";
    }
  }
}

dropdown_link.addEventListener("click", showDropDownMenu);

function showDropDownMenu() {
  dropdown_menu.style.display = "";
}
