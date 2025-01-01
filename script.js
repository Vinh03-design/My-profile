const menuT = document.querySelector('.menu-toggle');
const NavL = document.querySelector('.nav-links');

menuT.addEventListener('click', () => {
    menuT.classList.toggle('active');
    NavL.classList.toggle('open');
});

document.querySelectorAll('.nav-links a').forEach(links => {
    links.addEventListener('click', () => {
        menuT.classList.remove('active');
        NavL.classList.remove('open');
    });
});
