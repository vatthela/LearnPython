
function changeColor() {
  document.getElementById("paragraph1").style.color = "#66CCFF";
  document.getElementById("paragraph2").style.color = "#FFFF00";
  document.getElementById("paragraph3").style.color = "#FF6600";
}

function changeBgColor() {
  document.body.style.backgroundColor = "#6699FF";
}

function copyContent() {
  let doan1 = document.getElementById("paragraph1").innerHTML;
  document.getElementById("paragraph2").innerHTML = doan1;
}

function changeFontSize(x) {
  document.getElementById("paragraph1").style.fontSize = x + 'px';
  document.getElementById("paragraph2").style.fontSize = x + 'px';
  document.getElementById("paragraph3").style.fontSize = x + 'px';
}

function changeFontSize2(x, paragraph) {
  document.getElementById(paragraph).style.fontSize = x + 'px';
}

function increaseFontSize(paragraph) {
  let elem = document.getElementById(paragraph);
  let current_fontsize = window.getComputedStyle(elem, null).getPropertyValue('font-size');
  let x = parseInt(current_fontsize) + 1;
  if (x <= 30) {
    changeFontSize2(x, paragraph);
  }
}

function decreaseFontSize(paragraph) {
  let elem = document.getElementById(paragraph);
  let current_fontsize = window.getComputedStyle(elem, null).getPropertyValue('font-size');
  let x = parseInt(current_fontsize) - 1;
  if (x >= 10) {
    changeFontSize2(x, paragraph);
  }
}