
$(document).ready(function() {
    // Componente de login/logout
    request = $.ajax({
        url: '/api/user',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            if (data.ID) {
                $('a.logout').show();
                $('a.login').hide();

                if (data.role === 'administrador') { $('a.dashboard').html('Dashboard') }
            } else {
                $('a.logout').hide();
                $('a.login').show();
            }
        }
    });


    // Modal de confirmación
    $('#modalConfirm').on('show.bs.modal', function (event) { // Evento que se ejecuta al abrir el modal
        const button = $(event.relatedTarget); // Botón que activó el modal

        const title = button.data('title');
        const body = button.data('body');
        const action = button.data('action');

        const modal = $(this);
        modal.find('.modal-title').text(title);
        modal.find('.modal-body').text(body);

        const modalButton = modal.find('.btn-primary')
        modalButton.attr('href', action);
    });

    // Flash messages
    $('.flash').delay(3000).fadeOut(1000);
});

