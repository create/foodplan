$(document).ready(function() {
    $('.reroll').click(function(e) {
        var day_no = $(this).attr('day_no');
        $.get('/reroll?day=' + day_no, function(res) {
           if (res != 'error') {
                var image = $('.meal-card-image.card-' + day_no);
               image.css('backgroundImage', 'url("' + res.result.image_url + '")');
               $('.meal-card-name', image).text(res.result.name);
               $('.meal-card-price .num', image).text(res.result.price);
               var oldPrice = $('#totalpriceval').text();
               var newPrice = parseFloat(oldPrice) + parseFloat(res.result.total_price_change);
               $('#totalpriceval').text(newPrice.toFixed(2));
           } else {
               console.log("Error rerolling!");
               console.log(res);
           }
        });
    });
    $('.evernote').click(function(e) {
        // create an message bar instance
        var msgBar = new MessageBar();
        // initialize it, it will create a message bar dom for later interact.
        msgBar.initialize();
        msgBar.show('Exporting to Evernote... Please wait.');
        $.get('/export', function(res) {
            msgBar.success('Exported to Evernote!');
        });
    });
});