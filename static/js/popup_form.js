// $(function() {
//   $('#popup-btn').click(() => {
//     alert('clicked');
//     // $('.form-container').fadeToggle();
//   })
  
//   $(document).mouseup((e) => {
//     var container = $('.form-container');

//     if (!container.is(e.target) && container.has(e.target).length === 0) {
//       container.fadeOut();
//     }
//   });

// });

$(document).ready(function() {
  $('#popup-btn').on('submit', function(e) {
    e.prevenDefault()
    alert("click")
  })
})