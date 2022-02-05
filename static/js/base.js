const profileMenu = document.getElementById('dropdown-profile');
const loginSignup = document.getElementById('dropdown-enter');
const dropdown = document.querySelectorAll('.account__options');

document.addEventListener('DOMContentLoaded', function () {
  document.addEventListener('click', (e) => {
    if ((e.target !== dropdown && e.target !== loginSignup) && loginSignup.classList.contains('open')) {
      loginSignup.classList.remove('open');
    }
  })
  loginSignup.addEventListener('click', () => {
    loginSignup.classList.toggle('open');
    console.log('click');
  });
});