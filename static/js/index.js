let index = 0
let activeIndex = 0

let application_heading_link = document.getElementsByClassName('application_heading_link')

function Change(moves) {
    for (i = 0; i < application_heading_link.length; i++) {
        application_heading_link[i].classList.remove('active')
    }
    index += moves
    application_heading_link[index].classList.add('active')
    let contents = document.getElementsByClassName('application_body_page')
    if (index >= contents.length) {
        index = 0
    }
    if (index < 0) {
        index = contents.length - 1
    }
    for (let i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    contents[index].style.display = 'block'
}


function AddActive() {
    for (i = 0; i < application_heading_link.length; i++) {
        application_heading_link[i].classList.remove('active')
    }
    const currentIndex = Array.from(application_heading_link).indexOf(this)
    index = currentIndex
    this.classList.add('active');
}
for (i = 0; i < application_heading_link.length; i++) {
    application_heading_link[i].addEventListener('click', AddActive)
}

function Plans() {
    let contents = document.getElementsByClassName('application_body_page')
    let plans = document.getElementById('plans')
    for (let i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    plans.style.display = 'block'
}

function Personal() {
    let contents = document.getElementsByClassName('application_body_page')
    let personal = document.getElementById('personal')
    for (let i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    personal.style.display = 'block'
}

function Demographics() {
    let contents = document.getElementsByClassName('application_body_page')
    let demographics = document.getElementById('demographics')
    for (let i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    demographics.style.display = 'block'
}

function Next_of_kin() {
    let contents = document.getElementsByClassName('application_body_page')
    let next_of_kin = document.getElementById('next_of_kin')
    for (let i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    next_of_kin.style.display = 'block'
}

function Academics() {
    let contents = document.getElementsByClassName('application_body_page')
    let academics = document.getElementById('academics')
    for (let i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    academics.style.display = 'block'
}

function Declaration() {
    let contents = document.getElementsByClassName('application_body_page')
    let declaration = document.getElementById('declaration')
    for (let i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    declaration.style.display = 'block'
}