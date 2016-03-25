$(function() {
    var header  = $("#header");
    var menu    = $("#sticky-navbar");
    var body    = $("#body");

    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        if (scroll > header.outerHeight()) {
            menu.addClass("sticky-navbar-fixed");
            body.addClass("sticky-placeholder-active");
        } else {
            menu.removeClass("sticky-navbar-fixed");
            body.removeClass("sticky-placeholder-active");
        }
    });
});
