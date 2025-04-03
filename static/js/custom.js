$(document).ready(function() {
    // Auto-hide flash messages after 5 seconds
    setTimeout(function() {
        $('.flash-message').fadeOut('slow');
    }, 5000);

    // Add active class to nav links based on current page
    const currentPath = window.location.pathname;
    $('.nav-item a').each(function() {
        if ($(this).attr('href') === currentPath) {
            $(this).parent().addClass('active');
        }
    });
});