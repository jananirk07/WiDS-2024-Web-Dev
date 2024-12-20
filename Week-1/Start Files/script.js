window.onscroll = function() {
    const navbar = document.querySelector('.first-nav');

    if (window.scrollY > 0) {
        navbar.classList.add('scrolled');  
    } else {
        navbar.classList.remove('scrolled'); 
    }

};


function changeCategory(category, button) {
    const projects = document.querySelectorAll('.DBA, .DBB, .DBC');
    projects.forEach(project => {
        project.style.display = 'none';  
    });

    if (category === 'all') {
        
        const allProjects = document.querySelectorAll('.DBA, .DBB, .DBC');
        allProjects.forEach(project => {
            project.style.display = 'block'; 
        });
    } else {
        
        const selectedCategoryProjects = document.querySelectorAll(`.${category}`);
        selectedCategoryProjects.forEach(project => {
            project.style.display = 'block'; 
        });
    }

    
    const buttons = document.querySelectorAll('.button-1, .button-2, .button-3, .button-4');
    buttons.forEach(btn => {
        btn.classList.remove('active');  
    });
    
    
    button.classList.add('active');
}


document.querySelector('.button-1').addEventListener('click', function() {
    changeCategory('all', this); 
});
document.querySelector('.button-2').addEventListener('click', function() {
    changeCategory('frontend', this); 
});
document.querySelector('.button-3').addEventListener('click', function() {
    changeCategory('full-stack', this); 
});
document.querySelector('.button-4').addEventListener('click', function() {
    changeCategory('backend', this); 
});
