const openFormBtn = document.getElementById('openFormBtn');
const closeFormBtn = document.getElementById('closeFormBtn');

openFormBtn.addEventListener('click', () => {
    document.getElementById('formContainer').style.display = 'flex';
});

closeFormBtn.addEventListener('click', () => {
    document.getElementById('formContainer').style.display = 'none';
});

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));