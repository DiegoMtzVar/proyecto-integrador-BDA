
$(document).ready(function() {
    request = $.ajax({
        url: '/api/user',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            if (data.ID) {
                $('span.login-logout').html('<a href="logout"><i class="fas fa-sign-out-alt"></i></a>');
                if (data.role == 'administrador') {
                    $('a.dashboard').html('Dashboard')
                }
            } else {
                $('span.login-logout').html('<a href="login"><i class="fas fa-user"></i></a>');
            }
        }
    });
    request.done(function(data) {
        console.log('done');
    });

    $('#modal').on('show.bs.modal', function (event) { // Evento que se ejecuta al abrir el modal
        const button = $(event.relatedTarget); // Botón que activó el modal

        const title = button.data('title');
        const body = button.data('body');
        const action = button.data('action');

        const modal = $(this);
        modal.find('.modal-title').text(title);
        modal.find('.modal-body').text(body);

        const modalButton = modal.find('.btn-primary')
        modalButton.attr('href', action);

        modalButton.click(function() {
            modal.modal('hide');
        });
    });

    $('#dataTable').dataTable();
});

