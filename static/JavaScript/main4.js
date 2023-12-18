// TOGGLE MOBILE MENU ICON 
document.addEventListener("DOMContentLoaded", function () {
    const mobileMenuIcon = document.querySelector('.mobile-menu');
    const navMenu = document.querySelector('.authHeader__nav__ul');
    mobileMenuIcon.addEventListener('click', function () {
        navMenu.classList.toggle('show');
        if (navMenu.classList.contains('show')) {
            mobileMenuIcon.innerHTML = "<i class='bx bx-x' style='font-size: 2.6rem; color: darkred; font-weight: bold; transition: 0.7s ease-in-out;'></i>";
        } else {
            mobileMenuIcon.innerHTML = "<i class='bx bx-menu-alt-right' style='transition: 0.7s ease-in-out;'></i>"; 
        }
    });
});



document.addEventListener("DOMContentLoaded", function () {
    const authHeader = document.querySelector('.auth-header');
    const faSearch = document.querySelector('.fa-search ');
    const links = authHeader.querySelectorAll('a');

    // Initial styles
    links.forEach(link => {
        link.style.color = '#fff';
    });

    let shouldKeepBackground = false; 
    
    // Change color on mouseenter/mouseleave
    authHeader.addEventListener("mouseenter", handleMouseEnter);
    authHeader.addEventListener("mouseleave", handleMouseLeave);

    function handleMouseEnter() {
        authHeader.style.backgroundColor = '#ff5700'; 
        faSearch.style.color = '#000'
        links.forEach(link => {
            link.style.color = '#fff';
        });
    }

    function handleMouseLeave() {
        if (!shouldKeepBackground) {
            authHeader.style.backgroundColor = 'transparent';
            links.forEach(link => {
                link.style.color = '#fff';
            });
        }
    }

    // Change header background on scroll
    document.addEventListener("scroll", handleScroll);

    function handleScroll() {
        const scrollPosition = window.scrollY;

        if (scrollPosition > 10) {
            authHeader.style.backgroundColor = '#ff5700';
            shouldKeepBackground = true;
        } else {
            authHeader.style.backgroundColor = 'transparent';
            shouldKeepBackground = false;
        }
    }
});
