////////////////// javascript for posts page /////

$(function() {
    // executed when js-option-icon js is clicked //
    $('.js-option-icon').click(function() {
        $(this).next().toggle();
    })
})