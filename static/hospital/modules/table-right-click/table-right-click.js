(function ($, window) {

    $.fn.contextMenu = function (settings) {

        return this.each(function () {

            // Open context menu
            $(this).on("contextmenu", function (e) {
                // return native menu if pressing control
                if (e.ctrlKey) return;

                //open menu
                var $menu = $(settings.menuSelector)
                    .data("invokedOn", $(e.target))
                    .show()
                    .css({
                        position: "absolute",
                        left: getMenuPosition(e.clientX, 'width', 'scrollLeft'),
                        top: getMenuPosition(e.clientY, 'height', 'scrollTop')
                    })
                    .off('click')
                    .on('click', 'a', function (e) {
                        $menu.hide();

                        var $invokedOn = $menu.data("invokedOn");
                        var $selectedMenu = $(e.target);

                        settings.menuSelected.call(this, $invokedOn, $selectedMenu);
                    });

                return false;
            });

            //make sure menu closes on any click
            $('body').click(function () {
                $(settings.menuSelector).hide();
            });
        });

        function getMenuPosition(mouse, direction, scrollDir) {
            var win = $(window)[direction](),
                scroll = $(window)[scrollDir](),
                menu = $(settings.menuSelector)[direction](),
                position = mouse + scroll;

            // opening menu would pass the side of the page
            if (mouse + menu > win && menu < mouse)
                position -= menu;

            return position;
        }

    };
})(jQuery, window);
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
$(".table-right-click td").contextMenu({
    menuSelector: "#contextMenu",
    menuSelected: function (invokedOn, selectedMenu) {
        var user_id = $(invokedOn).parent("tr").attr("data-value");
        if ($(selectedMenu).attr("data-target") === "accept") {
            $("#acceptModal").find("[name=user_id]").val(user_id);
            $('#acceptModal').modal('toggle');
            var description = $("#acceptModal").find("[name=description]").val();
            $('#acceptModal').on("click", ".btn", function()
            {
                $.ajax({
                    url: "/admin/organization/firstconfirm",
                    data: {user_id: user_id,description: description},
                    method: 'post',
                    success: function (data) {
                        location.reload();
                    }
                });
            });
        }
        if ($(selectedMenu).attr("data-target") === "acceptLevel") {
            $("#acceptLevel").find("[name=description]").val("");
            var organization_level_id = $(invokedOn).parent("tr").attr("data-value");
            $('#acceptLevel').modal('toggle');
            $('#acceptLevel').on("click", ".btn", function()
            {
                var description = $("#acceptLevel").find("[name=description]").val();
                $.ajax({
                    url: "/admin/organizations/accept_level",
                    data: {organization_level_id: organization_level_id,description: description},
                    method: 'post',
                    success: function (data) {
                        location.reload();
                    }
                });
            });
        }
        if ($(selectedMenu).attr("data-target") === "finalConfirm") {
            $("#finalConfirmModal").find("[name=user_id]").val(user_id);
            $('#finalConfirmModal').modal('toggle');
            var description = $("#finalConfirmModal").find("[name=description]").val();
            $('#finalConfirmModal').on("click", ".btn", function()
            {
                $.ajax({
                    url: "/admin/organization/finalconfirm",
                    data: {user_id: user_id,description: description},
                    method: 'post',
                    success: function (data) {
                        location.reload();
                    }
                });
            });
        }


        /*var msg = "You selected the menu item '" + selectedMenu.text() +
            "' on the value '" + invokedOn.text() + "'";
        alert(msg);*/
    }
});