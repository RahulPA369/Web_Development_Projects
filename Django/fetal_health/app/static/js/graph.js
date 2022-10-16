function updateReport(data) {
  var progressbar = document.querySelector(".report .progress-bar");
  var situation = document.querySelector(".current-situation p");
  switch (data) {
    case "Normal":
      progressbar.style.width = "100%";
      progressbar.style.backgroundColor = "#19FF43";
      situation.innerHTML = "Normal";
      break;

    case "Suspect":
      progressbar.style.width = "50%";
      progressbar.style.backgroundColor = "#FF8819";
      situation.innerHTML = "Suspicious";
      break;

    case "Pathological":
      progressbar.style.width = "100%";
      progressbar.style.backgroundColor = "#FF1919";
      situation.innerHTML = "Pathological";
      break;

    default:
      progressbar.style.width = "0%";
      situation.innerHTML = "No Data Available";
      break;
  }
}
function valvalidation(ele_id) {
  var elem = document.getElementById(ele_id);
  var msg = document.getElementById(ele_id + "alert");
  var values = {
    bline: [100, 200],
    acc: [0, 0.02],
    fm: [0, 0.5],
    uc: [0, 0.02],
    ld: [0, 0.02],
    sd: [0, 0.002],
    pd: [0, 0.006],
    astv: [10, 100],
  };

  if (elem.value < values[ele_id][0] || elem.value > values[ele_id][1]) {
    msg.style.display = "block";
    elem.value = "";
    elem.focus();
    msg.innerHTML =
      "<div class='msgpop'><div><small>*Value should be between " +
      values[ele_id][0] +
      " and " +
      values[ele_id][1] +
      "</small></div></div>";
  } else {
    msg.style.display = "none";
  }
}

