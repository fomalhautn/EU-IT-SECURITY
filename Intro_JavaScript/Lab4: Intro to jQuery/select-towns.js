//Create an HTML page listing Cities, a city should be selectable.
//Clicking on a town should select/deselect it, a selected city should have the data-selected attribute added to it and its background color should be changed to #DDD.
//Also create a button [Show Cities] that prints the text "Selected cities: " followed by all selected towns joined with a ", ".

function attachEvents() {
    // TODO
    $('#items li').on('click', function () {
        if ($(this).attr('data-selected')) {
            $(this).removeAttr('data-selected');
            $(this).css('background-color', '');
        } else {
            $(this).attr('data-selected', true);
            $(this).css('background-color', '#DDD');
        }
    }
    );
    $('#showTownsButton').on('click', function () {
        let selected = $('#items li[data-selected=true]').toArray().map(li => li.textContent).join(', ');
        $('#selectedTowns').text(`Selected towns: ${selected}`);
    }
    );
   }