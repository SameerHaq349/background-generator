var colorPickerOne = document.getElementById("colorpickerOne")
var colorPickerTwo = document.getElementById("colorpickerTwo")
var backGround = document.querySelector("body")
var label = document.querySelector("h4")

colorPickerOne.addEventListener("input", () => {
    backGround.style.background = "linear-gradient(to right," + colorPickerOne.value + "," + colorPickerTwo.value + ")"
    label.textContent = "CURRENT CSS BACKGROUND:" + "linear-gradient(to right," + colorPickerOne.value + "," + colorPickerTwo.value + ")"
});

colorPickerTwo.addEventListener("input", () => {
    backGround.style.background = "linear-gradient(to right," + colorPickerOne.value + "," + colorPickerTwo.value + ")"
    label.textContent = "CURRENT CSS BACKGROUND:" + "linear-gradient(to right," + colorPickerOne.value + "," + colorPickerTwo.value + ")"
});



/*
1. change it to be one background instead of two
2. create a linear gradient
*/