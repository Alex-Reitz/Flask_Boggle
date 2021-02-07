$(function () {
    // pass the event object as 'evt' to the callback
    $('#submit').click(async function sendAnswer(evt){
    evt.preventDefault();
    const $inputValue = $("#guessValue").val()
    console.log($inputValue);
    /* Make axios post request to flask server */
    const response = await axios({
        method: "post",
        url: "localhost:5000/",
        data: {
            input: `${$inputValue}`
            }
        })
    });
});

window.onload = function() {
    $("#gameOver").hide()
    let count = 60, timer = setInterval(function() {
        $("#timer").html(`Time left: ` + count-- + ` seconds`);
        if(count === -1){
            clearInterval(timer)
            $("#guessValue").hide()
            $("#submit").hide()
            $("#labelGuess").hide()
            $("#gameOver").show()
        }
    }, 1000);
  }
