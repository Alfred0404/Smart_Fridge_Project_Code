
const navLink = document.querySelectorAll('.nav_link')

function linkColor(){
    navLink.forEach(link => link.classList.remove('active-link'))
    this.classList.add('active-link')
}
navLink.forEach(link => link.addEventListener('click', linkColor))