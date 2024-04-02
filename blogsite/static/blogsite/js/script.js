
(function ($) {
    "use strict";

    // init Isotope
    var initIsotope = function () {

        $('.grid').each(function () {

            var $buttonGroup = $('.button-group');
            var $checked = $buttonGroup.find('.is-checked');
            var filterValue = $checked.attr('data-filter');

            var $grid = $('.grid').isotope({
                itemSelector: '.photocards-item',
                // layoutMode: 'fitRows',
                filter: filterValue
            });

            // bind filter button click
            $buttonGroup.on('click', 'a', function (e) {
                e.preventDefault();
                filterValue = $(this).attr('data-filter');
                $grid.isotope({filter: filterValue});
            });

            // change is-checked class on buttons
            $buttonGroup.each(function (i, buttonGroup) {
                $buttonGroup.on('click', 'a', function () {
                    $buttonGroup.find('.is-checked').removeClass('is-checked');
                    $(this).addClass('is-checked');
                });
            });
            // });

        });
    }

    var initScrollNav = function () {
        var scroll = $(window).scrollTop();
        if (scroll >= 200) {

            $('#header.fixed-top').addClass("bg-white");
        } else {
            $('#header.fixed-top').removeClass("bg-white");
        }
    }
    var initChocolat = function () {
        Chocolat(document.querySelectorAll('.chocolat-image'), {
            loop: false,
            imageSize: 'contain',
            setTitle: function () {
                return 'Забытые фотокарточки'
            },
            linkImages: false,
        })
    }

    // ------------------------------------------------------------------------------ //
    // Overlay Menu Navigation
    // ------------------------------------------------------------------------------ //
    var overlayMenu = function () {

        if (!$('.nav-overlay').length) {
            return false;
        }
        var body = undefined;
        var menu = undefined;
        var menu_close = undefined;
        var menuItems = undefined;
        var init = function init() {
            body = document.querySelector('body');
            menu = document.querySelector('#menu-btn');
            menu_close = document.querySelector('#menu-btn-close');
            menuItems = document.querySelectorAll('.nav__list-item');
            applyListeners();
        };
        var applyListeners = function applyListeners() {
            menu.addEventListener('click', function () {
                return toggleClass(body, 'nav-active');
            });
            menu_close.addEventListener('click', function () {
                return toggleClass(body, 'nav-active');
            });
        };
        var toggleClass = function toggleClass(element, stringClass) {
            if (element.classList.contains(stringClass)) element.classList.remove(stringClass); else element.classList.add(stringClass);
        };
        init();
    }

    $(document).ready(function () {
        initScrollNav();
        overlayMenu();

        AOS.init({
            duration: 1000,
            once: true
        })
        $('#btn-menu').click(function (e) {
            e.preventDefault();
            $('.sidebar-menu').toggleClass('open');
        })
        // $('#darkModeSwitch').click(function () {
        //     $.ajax({
        //         data: $('body').attr("data-bs-theme"),
        //         type: "POST",
        //         url: "{% url %}"
        //     }
        // };
    }); // End of a document

    $(window).on('load', (function () {
        initIsotope();
        initChocolat();
    }));

    $(window).scroll(function () {
        initScrollNav();
    });

})(jQuery);