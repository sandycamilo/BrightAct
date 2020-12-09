// getinvolved2.js

// // Get the modal
// var modal = document.getElementById("sectorModal");
//
// hide all modals until the startButton is clicked
// hideAllModals();

// // Get the button that opens the modal
// var startButton = document.getElementById("startButton");

// Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];

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
        // modalIndex += 1; // gets next modal
        let selectedModalID = e.target.dataset.nextId;
        ///  repeat the following for all variations
        // get modalID then determine where to next
        // ifthen else or switch
        switch(selectedModalID){
            // goal: if id matches sector value
            case "sectorValue":
                const sector = document.getElementById('sectors').value;
                if(sector === "Civic") {
                    selectedModalID = "legalSupportModal"

                } else if(sector === "Public") {
                        // modalIndex = modalIds.indexOf("orgTypeModal")
                        selectedModalID = "orgTypeModal"
                } else if(sector === "University") {
                        // modalIndex = modalIds.indexOf("uniDeptModal")
                        selectedModalID = "uniDeptModal"
                } else if(sector === "Government (NGO)") {
                        // modalIndex = modalIds.indexOf("targetModal")
                        selectedModalID = "targetModel"
                }
                break;
            default:
                modalIndex = modalIndex + 1
                selectedModalID = modalIds[modalIndex]
        }
        // what was last answer and what should next modal be?
        showModal(selectedModalID)
    } else if (e.target.matches("#startButton")) {
        modalIndex = 0;
        showModal(modalIds[0])
    }
})

function showModal(id) {
    hideAllModals();
    document.getElementById(id).style.display = "block";
}

function hideModal(id) {
    document.getElementById(id).style.display = "none";
}

function hideAllModals() {
    modalIds.forEach((id) => {hideModal(id)})
}
