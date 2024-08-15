const button = document.getElementById("scroll-down-btn");
const productdiv = document.getElementById("product");

button.addEventListener('click', function() {
    productdiv.scrollIntoView({ behavior: 'smooth' });
});
