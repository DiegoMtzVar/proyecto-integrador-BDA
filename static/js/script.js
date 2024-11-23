$(document).ready(function() {
    request = $.ajax({
        url: '/api/user',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            if (data.ID) {
                $('span.login-logout').html('<a href="logout"><i class="fas fa-sign-out-alt"></i></a>');
                if (data.role == 'administrador') {
                    $('span.dashboard').html('Dashboard')
                }
            } else {
                $('span.login-logout').html('<a href="login"><i class="fas fa-user"></i></a>');
            }
        }
    });
    request.done(function(data) {
        console.log('done');
    });
});