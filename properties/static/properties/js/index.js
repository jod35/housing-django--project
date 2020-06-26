const nav = document.querySelector("nav");
const navbar_items = document.querySelectorAll(".nav-link");
const logo_area = document.querySelector(".logo");
const dropdown_menu = document.querySelector(".drop-down");
const dropdown_link = document.getElementById("buy-btn");
const mobile_menu_icon=document.querySelector('#mobile-menu');
const overlay=document.querySelector('#overlay');



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
    nav.style.padding = "15px";
    // mobile_menu_button.style.color="white";

    logo_area.style.color = "white";

    for (let i = 0; i < navbar_items.length; i++) {
      navbar_items[i].style.color = "white";
    }
  } else {
    nav.style.backgroundColor = "white";
    logo_area.style.color = "rgb(219, 30, 30)";
    nav.style.padding = "30px";
    for (let i = 0; i < navbar_items.length; i++) {
      navbar_items[i].style.color = "rgb(219, 30, 30)";
    }
    // mobile_menu_button.style.color="rgb(219, 30, 30)";
   
  }
}






mobile_menu_icon.addEventListener('click',displayNav);

function displayNav(){
  if(overlay.style.display=="none"){
    overlay.style.display="block";
  }
  else{
    overlay.style.display="none";
   
  }
}