function initializeTable() {
    $('#createLink').click(createCountry);
    fixRowLinks();
    function createCountry() {
        let country = $('#newCountryText').val();
        let capital = $('#newCapitalText').val();
        let row = $('<tr>')
            .append($('<td>').text(country))
            .append($('<td>').text(capital))
            .append($('<td>')
                .append($('<a href="#">[Up]</a>').click(moveUp))
                .append($('<a href="#">[Down]</a>').click(moveDown))
                .append($('<a href="#">[Delete]</a>').click(deleteRow)));
        row.css('display', 'none');
        $('#countriesTable').append(row);
        row.fadeIn();
        fixRowLinks();
        $('#newCountryText').val('');
        $('#newCapitalText').val('');
    }
    function moveUp() {
        let row = $(this).parent().parent();
        row.fadeOut(function () {
            row.insertBefore(row.prev());
            row.fadeIn();
            fixRowLinks();
        });
    }
    function moveDown() {
        let row = $(this).parent().parent();
        row.fadeOut(function () {
            row.insertAfter(row.next());
            row.fadeIn();
            fixRowLinks();
        });
    }
    function deleteRow() {
        let row = $(this).parent().parent();
        row.fadeOut(function () {
            row.remove();
            fixRowLinks();
        });
    }
    function fixRowLinks() {
        // Show all links in the table
        $('#countriesTable a').css('display', 'inline');
        // Hide [Up] link in the first table data
        let tableRows = $('#countriesTable tr');
        $(tableRows[2]).find("a:contains('Up')").css('display', 'none');
        // Hide [Down] link in the last table row
        $(tableRows[tableRows.length - 1]).find("a:contains('Down')").css('display', 'none');
    }
   }