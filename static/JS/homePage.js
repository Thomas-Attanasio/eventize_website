const observers = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            const target = entry.target.querySelector('.statNumber');

            if (target) {
                const countTo = parseInt(target.getAttribute('data-target'));

                let current = 0;
                const increment = countTo / 50;
                const updateCount = () => {
                    if (current < countTo) {
                        current += increment;

                        target.innerText = Math.ceil(current);
                        setTimeout(updateCount, 30);
                    } else {
                        target.innerText = countTo;
                    }
                };

                updateCount();
            }

            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.3 });

document.querySelectorAll('.reveal, .statCard').forEach((el) => observers.observe(el));