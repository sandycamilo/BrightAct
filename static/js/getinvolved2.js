// getinvolved2.js

// // Get the modal
// var modal = document.getElementById("sectorModal");
//
// // Get the button that opens the modal
// var btn = document.getElementById("myBtn");
//
// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];
//
// // When the user clicks on the button, open the modal
// btn.onclick = function() {
//   modal.style.display = "block";
// }
//
// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }
//
// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }

// // Intended to be a way to get the next question in a series of questions stored in an array of strings
// function(nextQ) {
//     document.getElementById("nextBtn");
//      let sector = #?
//      if(sector === None) {
//            modal = getElementById("?")
//        } else {
//            if(sector === "civil") {
//                modal = getElementById("?")
//            }
//        }
// }

// make a list of all modal ids
const modalIds = ["personNameModal", "orgNameModal", "countryModal", "roleModal", "sectorModal", "phoneModal", "foundModal", "reasonModal", "infoModal", "targetModal", "brandedModal", "collaborationModal", "orgTypeModal", "deptModal", "uniDeptModal", "studiesLevelModal", "researchModal", "legalSupportModal", "offerUsersModal"]

let modalIndex = 0;

document.querySelector("body").addEventListener("click", (e) => {
    if(e.target.matches(".next-question")) {
        modalIndex += 1;
        hideAllModals();
        console.log("Area of code reached")
        // what was last answer and what should next modal be?
        showModal(modalIds[modalIndex])
    }
})

function showModal(id) {
    document.getElementById(id).style.display = "block";
}

function hideModal(id) {
    document.getElementById(id).style.display = "none";
}

function hideAllModals() {
    modalIds.forEach((id) => {hideModal(id)})
}

hideAllModals()

showModal(modalIds[0])
