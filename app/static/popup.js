const trigger = document.getElementById("internetBtn")
const popup = document.getElementById("popup_container")
const closePopup = document.getElementById("close_popup")

trigger.onclick = () => popup.style.display = 'block'
closePopup.onclick = () => popup.style.display = 'none';
window.onclick = (e) => {
    if (e.target === popup) popup.style.display = 'none';
}