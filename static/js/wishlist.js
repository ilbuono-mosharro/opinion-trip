$(document).ready(function () {
        let isLoading = false;

        $('.favorite-form').submit(function (e) {
        e.preventDefault()
        if (!isLoading) {
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const url = $(".favorite-form").attr("action");
            const attraction_id = $(this).attr('id');
            isLoading = true;

            $.ajax({
                type: 'POST',
                url: url,
                dataType: "json",
                mode: 'same-origin',
                headers: {
                    'X-CSRFToken': csrftoken,
                    "X-Requested-With": "XMLHttpRequest",
                },
                data: JSON.stringify({
                    'csrfmiddlewaretoken': csrftoken,
                    'attraction_id': attraction_id,
                }),
                success: function (response) {
                    if (response.status) {
                        $('#heart-' + attraction_id).addClass('bi-heart-fill fs-5 text-danger').removeClass('bi-heart');
                    } else {
                        $('#heart-' + attraction_id).addClass('bi-heart').removeClass('bi-heart-fill text-danger');
                    }
                    isLoading = false;
                },
                error: function (error) {
                    console.log('you need to login.');
                },
                statusCode: {
                    403: function (error) {
                        console.log(error);
                    },
                },
            });
        }
    });
});