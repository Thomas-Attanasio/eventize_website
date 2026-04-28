const chartObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const bars = entry.target.querySelectorAll('.barFill');

            bars.forEach(bar => {
                const widthValue = bar.getAttribute('style').split('--target-width: ')[1].split(';')[0];
                bar.style.width = widthValue;
            });
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.chartsContainer').forEach(c => chartObserver.observe(c));

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.2 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));