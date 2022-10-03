//An HTML page holds a list of towns, a search box and a [Search] button.
//Implement the search function to bold the items from the list which include the text from the search box.
//Also print the amount of items the current search matches in the format "<matches> matches found."

function search() {
    // TODO
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