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
    const yearlyContent = document.getElementById('year-dates');
    const monthlyContent = document.getElementById('monthly-dates');
    const dailyContent = document.getElementById('daily-dates');

    console.log("Typetime:",typetime)

    yearlyContent.style.display = 'none';
    monthlyContent.style.display = 'none';
    dailyContent.style.display = 'none';

    if (typetime === 'Year') {
        yearlyContent.style.display = 'block';
    } else if (typetime === 'Month') {
        monthlyContent.style.display = 'block';
    } else if (typetime === 'Day') {
        dailyContent.style.display = 'block';
    }
}