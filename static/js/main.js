$(document).ready(function() {
    $('.reroll').click(function(e) {
        var day_no = $(this).attr('day_no');
        $.get('/reroll?day=' + day_no, function(res) {
           if (res != 'error') {
                var image = $('.meal-card-image.card-' + day_no);
               image.css('backgroundImage', 'url("' + res.result.image_url + '")');
               $('.meal-card-name', image).text(res.result.name);
               $('.meal-card-price', image).text(res.result.price);
           } else {
               console.log("Error rerolling!");
               console.log(res);
           }
        });
    });
});