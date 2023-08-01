(function ($) {
    "use strict";
    var of_theme = {
        window: $(window),
        html: $('html, body'),
        document: $(document),
        body: $('body'),
        get_rtl: function () {
            return of_theme.body.hasClass('rtl');
        },

        document_ready: function () {
            of_theme.my_account_modal();
            of_theme.search_header();
            of_theme.canvas_menu_mobile();
            //of_theme.of_nav_to_select();
            of_theme.of_sticky_header();
        },

        document_resize: function () {
            of_theme.window.resize(function () {


            })
        },

        my_account_modal: function () {
            var acc_form = $('.account_action');
            var mask_overlay = $('.of-site-mask');
            $('span.login_user_btn').on('click', function () {
                mask_overlay.addClass('active');
                acc_form.addClass('active');
                acc_form.find('.acc_div').hide();
                acc_form.removeClass('trbox');
                $('.login_form').show();

            });

            $('span.singup_user_btn').on('click', function () {
                mask_overlay.addClass('active');
                acc_form.addClass('active');
                acc_form.find('.acc_div').hide();
                $('.register_form').show();
                acc_form.addClass('trbox');

            });

            $('.of-site-mask , .close_modal').on('click', function () {
                acc_form.removeClass('active');
                mask_overlay.removeClass('active');
            });
        },

        search_header: function () {
            $('.m_search').on('click', function (e) {
                e.preventDefault();
                $('.search_wrap').toggleClass('active');
                if ($('.search_wrap').hasClass('active')) {
                    $(this).find('i').removeClass('fa-search').addClass('fa-times');
                } else {
                    $(this).find('i').removeClass('fa-times').addClass('fa-search');
                }
            });

        },

        canvas_menu_mobile: function () {
            var of_off_canvas_button = $('#of-trigger');
            var of_off_canvas_button_close = $('#of-close-off-canvas');
            var of_mask = $('.of-site-mask');
            of_off_canvas_button.click(function () {
                of_theme.body.toggleClass('mobile-js-menu');
                $('body').addClass('lock-scroll');
                return false;
            });

            of_off_canvas_button_close.click(function () {
                of_theme.body.removeClass('mobile-js-menu');
                $('body').removeClass('lock-scroll');
                return false;
            });

            of_mask.click(function () {
                of_theme.body.removeClass('mobile-js-menu');
                $('body').removeClass('lock-scroll');
                return false;
            });


            var mobile_menu = $('.mobile-menu-wrap');
            var sub_mobile_menu = mobile_menu.find('li.menu-item-has-children');
            var sub_mobile_a = mobile_menu.find('li.menu-item-has-children > a');

            sub_mobile_a.append('<i class="explain-menu fal fa-angle-left"></i>');

            $('.explain-menu').unbind('click').bind('touchend click', function (e) {
                e.preventDefault();
                $(this).parent('a').toggleClass('active').siblings('ul').slideToggle(500);
            });

            sub_mobile_menu.find('a').click(function (event) {
                event.stopPropagation();
            });

            mobile_menu.click(function (event) {
                event.stopPropagation();
            });

        },

        of_sticky_header: function () {

            if ($(".menu_sticky").length > 0) {

                var offset_top = $('header').height();
                $(window).scroll(function (event) {
                    var currentScroll = $(this).scrollTop();
                    if (currentScroll > offset_top) {
                        $('.menu_sticky').addClass('my_sticky');
                    } else {
                        $('.menu_sticky').removeClass('my_sticky');
                    }
                });

            }
        },


    };

    $(document).ready(function () {
        of_theme.document_ready();
        of_theme.document_resize();

    });

})(jQuery);











