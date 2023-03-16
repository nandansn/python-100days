
let imgElement = document.getElementById("image_1");;

imgElement.addEventListener("click", (e) => {
  e.preventDefault();
  document.body.style.backgroundColor = "red"
});