const form = document.getElementById('contact-form')
const loading = document.querySelector('.js-loading')
const successMessage = document.querySelector('.js-success-message')

form.addEventListener('submit', () => {
  showLoadingIndicator()
})

function showLoadingIndicator() {
  form.classList.add('is-hidden')
  loading.classList.remove('is-hidden')
}
