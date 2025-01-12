function redirectToLogin() {
    window.location.href = '/login/';
}

function redirectToRegister() {
    window.location.href = '/register/';
}

function redirectToLogout() {
    window.location.href = '/logout/';
}

function redirecrtToQuesstionaire() {
    window.location.href = '/quesstionaire/'
}

function redirectToVisulize() {
    window.location.href = '/data_visulize/'
}

function redirectHome() {
    window.location.href = '/'
}

function updateDateVisibility() {
    const typetime = document.getElementById('typetime').value
    const yearlyContent = document.getElementById('yearly-content');
    const monthlyContent = document.getElementById('monthly-content');
    const dailyContent = document.getElementById('daily-content');

    // Hide all content divs initially
    yearlyContent.style.display = 'none';
    monthlyContent.style.display = 'none';
    dailyContent.style.display = 'none';

    // Show the relevant content div based on the selected value
    if (typetime === 'Year') {
        yearlyContent.style.display = 'block';
    } else if (typetime === 'Month') {
        monthlyContent.style.display = 'block';
    } else if (typetime === 'Day') {
        dailyContent.style.display = 'block';
    }
}