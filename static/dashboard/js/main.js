/*
=========================================================
* Dash UI - Bootstrap 5 Admin & Dashboard Theme
=========================================================
* Product Page: https://codescandy.com/dashui/index.html
* Copyright 2020 Codescandy (https://codescandy.com/)
* Designed and coded by https://codescandy.com
========================================================= */


//
// Main js
//


'use strict';
(function () {

    // Menu toggle for admin dashboard

    if ($("#nav-toggle").length) {
        $("#nav-toggle").on("click", function (e) {
            e.preventDefault();
            $("#db-wrapper").toggleClass("toggled");
        });

    }


    //  slimscroll for sidebar nav

    if ($(".nav-scroller").length) {
        $(".nav-scroller").slimScroll({
            height: "97%",
        });
    }


    // Default Tooltip

    if ($('[data-bs-toggle="tooltip"]').length) {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        })
    }


    // Default Popover

    if ($('[data-bs-toggle="popover"]').length) {
        var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
        var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
            return new bootstrap.Popover(popoverTriggerEl)
        })
    }

    // Scrollspy

    if ($('[data-bs-spy="scroll"]').length) {
        var dataSpyList = [].slice.call(document.querySelectorAll('[data-bs-spy="scroll"]'))
        dataSpyList.forEach(function (dataSpyEl) {
            bootstrap.ScrollSpy.getInstance(dataSpyEl)
                .refresh()
        })

    }

    // Toast

    if ($('.toast').length) {

        var toastElList = [].slice.call(document.querySelectorAll('.toast'))
        var toastList = toastElList.map(function (toastEl) {
            return new bootstrap.Toast(toastEl)
        })

    }


// offcanvas
    if ($(".offcanvas").length) {
        var offcanvasElementList = [].slice.call(document.querySelectorAll('.offcanvas'))
        var offcanvasList = offcanvasElementList.map(function (offcanvasEl) {
            return new bootstrap.Offcanvas(offcanvasEl)
        })

    }

})();
