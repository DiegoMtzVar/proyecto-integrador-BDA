
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

    // Flash messages
    $('.flash').delay(3000).fadeOut(1000);

    // DataTable de usuarios
    let table = $('#tablaUsuarios').dataTable({
        columnDefs: [
            {
                targets: 0,
                className: 'dt-control'
            },
            {
                targets: [3, 4],
                searchable: false,
                orderable: false
            }
        ]
    });

    formatRecentPurchases = function(data) {
        return (
            data.map(function(purchase) {
                return (
                    '<tr>' +
                        '<td>' + purchase.name + '</td>' +
                    '</tr>'
                );
            }
        )
        );
    }

    table.on('click', 'td.dt-control', function(e) {
        let tr = e.target.closest('tr');
        let row = table.api().row(tr);

        if (row.child.isShown()) {
            row.child.hide();
        } else {
            let id = row.data()[0];
            
            let request = $.ajax({
                url: '/dashboard/usuariosGestion/getRecentPurchases/' + id,
                type: 'GET',
                dataType: 'json'
            });
    
            request.done(function(data) {
                row.child(formatRecentPurchases(data)).show();
            });
        }
    });

    // DataTable de productos
    $('#tablaProductos').dataTable();

});

