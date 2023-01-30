const elements = document.getElementsByClassName("bar");
const audio = document.getElementsByClassName("my-audio")[0];

for (let element of elements) {
    element.addEventListener("mouseenter", function() {
        audio.play();
    });
}