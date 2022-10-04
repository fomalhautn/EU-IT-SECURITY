function search() {
    let searchText = $('#searchText').val();
    let matches = 0;
    $('#towns li').css('font-weight', '');
    $('#towns li').each((index, li) => {
        if (li.textContent.includes(searchText)) {
            $(li).css('font-weight', 'bold');
            matches++;
        }
    }
    );
    $('#result').text(`${matches} matches found`);
   }