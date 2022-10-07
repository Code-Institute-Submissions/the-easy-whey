const buttons = document.getElementsByClassName("standout-button");

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("mouseover", function (event) {
        this.style.backgroundColor = "saddleBrown";
    });
};

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("mouseout", function (event) {
        this.style.backgroundColor = "coral";
    });
};