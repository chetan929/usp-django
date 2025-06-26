window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.backgroundColor = '#0d72ee';
    } else {
        navbar.style.backgroundColor = 'transparent';
    }
});



document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('backToTop');
    if (btn) {
        btn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});

