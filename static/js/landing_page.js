$(function () {
    $('[data-toggle="popover"]').popover();

    $('.carousel').carousel()

    $('#one-in-three-source').popover({content: "<p>Women who have experienced physical and/or sexual violence by current and/or previous partner, since the age of 15. </p><p>* Data collection was made in 2012 via phone interviews by FRA. For the full results of the survey <a href='https://fra.europa.eu/sites/default/files/fra_uploads/fra-2014-vaw-survey-main-results-apr14_en.pdf' target='blank'>check the report</a>", html: true, placement: "right"});
});