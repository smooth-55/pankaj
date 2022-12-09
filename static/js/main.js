// api url
const api_url = "https://marcconrad.com/uob/smile/api.php"

const questionImage = document.getElementById("question_img")
const resultText = document.getElementById("result__text")
let actualQuestion = ""
let actualsolution = ""

let fetchAPI = () => {
    console.log("fetching!!");

    fetch(`${api_url}`, {
        "method": "GET",
    })
    .then(response => {
        console.log("response", response.body);
        return response.json()
    }).then(data => {

        const api_data = data
        actualQuestion = api_data.question 
        actualsolution = api_data.solution 
        console.log(api_data, "api data")
        questionImage.src = actualQuestion
    })
}


function handleSubmit(){
    let ansText = document.getElementById("ans_inp").value 
    if (ansText != actualsolution) {
            fetchAPI()
            document.getElementById("incorrect_input").value = parseInt(document.getElementById("incorrect_input").value) + 1;
            document.getElementById("incorrect_count").innerHTML = document.getElementById("incorrect_input").value;
            document.getElementById("ans_inp").classList.add("err");
        document.getElementById("ans_inp").value =""

    } else{
        document.getElementById("correct_input").value = parseInt(document.getElementById("correct_input").value) + 1;
        document.getElementById("correct_count").innerHTML = document.getElementById("correct_input").value;
        document.getElementById("ans_inp").classList.add("success");
        document.getElementById("ans_inp").value =""
        fetchAPI()
    }
    
}

function removeErr(){
    document.getElementById("ans_inp").classList.remove("err");
    document.getElementById("ans_inp").classList.remove("success");
    
}

fetchAPI()

