function addNewBoard() {
    var title = document.getElementById("add-title").value;
    var url = "http://" + location.host + "/board";
    $.post(url, {title: title});
    location.reload();

}

function deleteBoard(boardID) {
    var url = "http://" + location.host + "/delete/" + boardID;
    $.post(url, {board_id: boardID});
    location.reload();

}
function handle(e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        addNewBoard();
    }
}