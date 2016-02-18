/* Project specific Javascript goes here. */
$('#sel1').change(function () {
    var price = this.value
    $('.price_detail').html('$'+price)
 })