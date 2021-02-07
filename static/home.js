$(function () {
    // pass the event object as 'evt' to the callback
    $('#submit').click(async function sendAnswer(evt){
    evt.preventDefault();
    let inputValue = $("#guessValue").val()
    console.log(inputValue);
    /* Make axios post request to flask server */
    const resp = await axios.get("/check-word", { params: { inputValue: inputValue }});
    if (resp.data.result === "not-word") {
      showMessage(`${inputValue} is not a valid English word`);
    } else if (resp.data.result === "not-on-board") {
      showMessage(`${inputValue} is not a valid word on this board`);
    } 
});

function showMessage(msg){
    let message = $("#msg")
    message.innerText = msg
}

window.onload = function() {
    $("#gameOver").hide()
    let count = 60, timer = setInterval(function() {
        $("#timer").html(`Time left: ` + count-- + ` seconds`);
        if(count === -1) {
            clearInterval(timer)
            $("#guessValue").hide()
            $("#submit").hide()
            $("#labelGuess").hide()
            $("#gameOver").show()
        }
    }, 1000);
}
})