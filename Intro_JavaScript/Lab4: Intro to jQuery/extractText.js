//A HTML page holding a list of items and an [Extract Text] button is given.
//Implement the extractText function which will be called when the button's onClick event is fired.

function extractText() {
    $('#result').text($('#items li').toArray().map(li => li.textContent).join(", "));
    }   