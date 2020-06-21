const nav_links=document.querySelectorAll('.nav-item');
const nav=document.querySelector('nav');


for (let i=0; i<nav_links.length; i++){
    nav_links[i].addEventListener('mouseover',displayWhiteNav);
};

for (let i=0; i<nav_links.length;i++){
    nav_links[i].addEventListener('mouseleave',removeWhiteNav);
}

function displayWhiteNav(){
    nav.style.backgroundColor="white";
}

function removeWhiteNav(){
    nav.style.backgroundColor="none";
}


