$(function () {
    // pass the event object as 'evt' to the callback
    $('#submit').click(async function sendAnswer(evt){
    evt.preventDefault();
    const $inputValue = $("#guessValue").val()
    console.log($inputValue);
    const response = await axios({
        method: "POST",
        url: `/stories`,
        data: {
          answer: $inputValue
        },
      });
    
    });
  });
