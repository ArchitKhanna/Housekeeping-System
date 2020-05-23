function setStatusClass(status, num) {

  var x = document.getElementById("status "+num);

  if(status=="Dirty"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-ashleyred");
  }
  else if(status=="Cleaned"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-ashleyorange");
  }
  else if(status=="Audited"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-ashleygreen");
  }
  else if(status=="Ready"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-darkgreen");
  }
}

function setTaskClass(task, num) {

  var x = document.getElementById("task "+num);

  if(task=="Clean"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-ashleyorange");
  }
  else if(task=="Audit"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-ashleygreen");
  }
  else if(task=="Call Backs"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-ashleyorange");
  }
  else if(task=="Check In"){
    x.setAttribute("class","col-sm-3 text-white colorsetter-ashleyblue");
  }
}
