permitsCount = 0;
emergencyFileCount = 0;
reinforcementFileCount = 0;
effortFileCount = 0;
substitutionFileCount = 0;
violationsFileCount = 0;
teamModelsCount = 0;
preWorkMeetingsCount = 0;
riskAssessmentsCount = 0;
safeWorkProceduresCount = 0;
paramedicsCount = 0;
fightersCount = 0;
assignedTasksCount = 0;
artificialSecurityCardsCount = 0;
recipientsCount = 0;
sourcesCount = 0;
tuvForEquipmentAndDriversCount = 0;
fireExtinguishersCount = 0;
firstAidsCount = 0;
workTeamsCount = 0;
picturesOfSitesCount = 0;
subscriptionNumbersCount = 0;
cutterCapacitysCount = 0;
countersCount = 0;
missionLocksCount = 0;
safetyBarriersCount = 0;
objectsCount = 0;
obstaclesCount = 0;
violationsCount = 0;

$(document).on("click","[data-for]",function(){
    document.getElementById(this.dataset.for).click();
});
function creator(c,evt,parentId,childId,uploadType = "image"){
  imgCard = document.createElement("div");
  imgCard.className = "img-card";
  imgCard.id = `${childId}bx${c}`;
  imgCardBox = document.createElement("div");
  imgCardBox.className = "img-card-box";
  img = document.createElement("img");
  $(imgCardBox).append(img);
  var tgt = evt.target || window.event.srcElement,
      files = tgt.files;
  
  // FileReader support 
  if (uploadType == "image"){
    if (FileReader && files && files.length) {
        var fr = new FileReader();
        fr.onload = function () {
          img.src = fr.result;
        }
        fr.readAsDataURL(files[0]);
    }
    else {
    }
  }else{
    img.src = "/static/img/pdf.png"
  }
  p = document.createElement("p");
  p.innerHTML = document.getElementById(childId).value.split("\\").pop();
  button = document.createElement("button");
  button.type = "button";
  button.className = "btn ibtn";
  button.dataset.close = `${childId}bx${c}`;
  span = document.createElement("span");
  span.className = "material-symbols-sharp";
  span.innerHTML = "close";
  $(button).append(span);
  $(imgCard).append(imgCardBox);
  $(imgCard).append(p);
  $(imgCard).append(button);
  $(`#${parentId}`).append(imgCard);
  document.getElementById(childId).setAttribute('name',`${childId}${c}`);
  document.getElementById(childId).id = `${childId}${c}`;
  permit = document.createElement("input");
  permit.type = "file";
  if(uploadType == "image"){
    permit.accept = "image/*";
  }else{
    permit.accept = ".pdf";
  }
  permit.setAttribute("hidden","");
  permit.id = childId;
  $(`#${parentId}Group`).append(permit);
  imgCard.appendChild(document.getElementById(`${childId}${c}`));
}

$(document).on("change","#permit",function(evt){
  permitsCount += 1;
  creator(permitsCount,evt,'permits','permit');
});
$(document).on("change","#emergencyFile",function(evt){
  emergencyFileCount += 1;
  creator(emergencyFileCount,evt,'emergencyFiles','emergencyFile',"pdf");
});
$(document).on("change","#substitutionFile",function(evt){
  substitutionFileCount += 1;
  creator(substitutionFileCount,evt,'substitutionFiles','substitutionFile',"pdf");
});
$(document).on("change","#reinforcementFile",function(evt){
  reinforcementFileCount += 1;
  creator(reinforcementFileCount,evt,'reinforcementFiles','reinforcementFile',"pdf");
});
$(document).on("change","#effortFile",function(evt){
  effortFileCount += 1;
  creator(effortFileCount,evt,'effortFiles','effortFile',"pdf");
});
$(document).on("change","#violationsFile",function(evt){
  violationsFileCount += 1;
  creator(violationsFileCount,evt,'violationsFiles','violationsFile',"pdf");
});
$(document).on("change","#teamModel",function(evt){
  teamModelsCount += 1;
  creator(teamModelsCount,evt,'teamModels','teamModel');
});
$(document).on("change","#preWorkMeeting",function(evt){
  preWorkMeetingsCount += 1;
  creator(preWorkMeetingsCount,evt,'preWorkMeetings','preWorkMeeting');
});
$(document).on("change","#riskAssessment",function(evt){
  riskAssessmentsCount += 1;
  creator(riskAssessmentsCount,evt,'riskAssessments','riskAssessment');
});
$(document).on("change","#safeWorkProcedure",function(evt){
  safeWorkProceduresCount += 1;
  creator(safeWorkProceduresCount,evt,'safeWorkProcedures','safeWorkProcedure');
});
$(document).on("change","#paramedic",function(evt){
  paramedicsCount += 1;
  creator(paramedicsCount,evt,'paramedics','paramedic');
});
$(document).on("change","#fighter",function(evt){
  fightersCount += 1;
  creator(fightersCount,evt,'fighters','fighter');
});
$(document).on("change","#assignedTask",function(evt){
  assignedTasksCount += 1;
  creator(assignedTasksCount,evt,'assignedTasks','assignedTask');
});
$(document).on("change","#artificialSecurityCard",function(evt){
  artificialSecurityCardsCount += 1;
  creator(artificialSecurityCardsCount,evt,'artificialSecurityCards','artificialSecurityCard');
});
$(document).on("change","#recipientCard",function(evt){
  recipientsCount += 1;
  creator(recipientsCount,evt,'recipientCards','recipientCard');
});
$(document).on("change","#sourceCard",function(evt){
  sourcesCount += 1;
  creator(sourcesCount,evt,'sourceCards','sourceCard');
});
$(document).on("change","#tuvForEquipmentAndDriver",function(evt){
  tuvForEquipmentAndDriversCount += 1;
  creator(tuvForEquipmentAndDriversCount,evt,'tuvForEquipmentAndDrivers','tuvForEquipmentAndDriver');
});
$(document).on("change","#fireExtinguisher",function(evt){
  fireExtinguishersCount += 1;
  creator(fireExtinguishersCount,evt,'fireExtinguishers','fireExtinguisher');
});
$(document).on("change","#firstAid",function(evt){
  firstAidsCount += 1;
  creator(firstAidsCount,evt,'firstAids','firstAid');
});
$(document).on("change","#workTeam",function(evt){
  workTeamsCount += 1;
  creator(workTeamsCount,evt,'workTeams','workTeam');
});
$(document).on("change","#picturesOfSite",function(evt){
  picturesOfSitesCount += 1;
  creator(picturesOfSitesCount,evt,'picturesOfSites','picturesOfSite');
});
$(document).on("change","#subscriptionNumber",function(evt){
  subscriptionNumbersCount += 1;
  creator(subscriptionNumbersCount,evt,'subscriptionNumbers','subscriptionNumber');
});
$(document).on("change","#cutterCapacity",function(evt){
  cutterCapacitysCount += 1;
  creator(cutterCapacitysCount,evt,'cutterCapacitys','cutterCapacity');
});
$(document).on("change","#counter",function(evt){
  countersCount += 1;
  creator(countersCount,evt,'counters','counter');
});
$(document).on("change","#missionLock",function(evt){
  missionLocksCount += 1;
  creator(missionLocksCount,evt,'missionLocks','missionLock');
});
$(document).on("change","#safetyBarrier",function(evt){
  safetyBarriersCount += 1;
  creator(safetyBarriersCount,evt,'safetyBarriers','safetyBarrier');
});
$(document).on("change","#object",function(evt){
  objectsCount += 1;
  creator(objectsCount,evt,'objects','object');
});
$(document).on("change","#obstacle",function(evt){
  obstaclesCount += 1;
  creator(obstaclesCount,evt,'obstacles','obstacle');
});
$(document).on("change","#violation",function(evt){
  violationsCount += 1;
  creator(violationsCount,evt,'violations','violation');
});

$(document).on("click","[data-close]",function(){
  $(`#${this.dataset.close}`).remove();
});


function getUsers(){
  $.ajax({
    url: '/consultants',
    data: {getData:""},
    type: 'GET',
    success: function(res) {
      document.getElementById("usersList").innerHTML = "";
      res.data.forEach(d => {
        $(".list").append("<button data-assay="+rettext(d[0])+" class='btn'><p>"+rettext(d[0])+"</p><div>"+rettext(d[1])+"</div></button>");
      });
    }
  });
}
function getOperations(){
  $.ajax({
    url: '/operations',
    data: {getData:""},
    type: 'GET',
    success: function(res) {
      document.getElementById("operationsList").innerHTML = "";
      res.data.forEach(d => {
        $(".list").append("<p class='list-header'>"+rettext(d[0])+"</p>");
        d[1].forEach(f => {
          $(".list").append("<button data-operation="+rettext(f[0])+" class='btn'><p>"+rettext(f[1])+"</p><div>"+rettext(f[2])+"</div><span>"+rettext(f[3])+"</span></button>");
        });
      });
    }
  });
}

$(document).on("submit","form[data-form]",function(e){
  e.preventDefault();
  this_el = this;
  this_el.style.opacity = "0.7";
  var formData = new FormData(this);
  if(this_el.id == "addUserForm"){
    $.ajax({
      url: "/consultants",
      data: formData,
      type: 'POST',
      dataType: 'json',
      mimeType: 'multipart/form-data',
      contentType: false,
      cache: false,
      processData: false,
      success: function(res) {
        this_el.removeAttribute("style");
        this_el.scrollTo(0,0);
        document.getElementsByName("consultantName")[0].value = "";
        document.getElementsByName("jobNum")[0].value = "";
        document.getElementsByName("phoneNumber")[0].value = "";
        document.getElementsByName("password")[0].value = "";
        closeUserForm();
        getUsers();
      }
    });
  }
  else if(this_el.id == "emergencyForm" || this_el.id == "substitutionForm" || this_el.id == "reinforcementForm" || this_el.id == "effortForm" || this_el.id == "violationsForm"){
    $.ajax({
      url: "/operations",
      data: formData,
      type: 'POST',
      dataType: 'json',
      mimeType: 'multipart/form-data',
      contentType: false,
      cache: false,
      processData: false,
      success: function(res) {
        this_el.removeAttribute("style");
        this_el.scrollTo(0,0);
        document.getElementsByName("malfunctionNumber")[0].value = "";
        document.getElementsByName("malfunctionType")[0].value = "";
        document.getElementsByName("contractor")[0].value = "";
        document.getElementsByName("date")[0].value = "";
        document.getElementsByName("materials")[0].value = "";
        document.getElementsByName("consultantName")[0].value = "";
        document.getElementsByName("workNumber")[0].value = "";
        document.getElementsByName("contractor")[1].value = "";
        document.getElementsByName("employmentType")[0].value = "";
        document.getElementsByName("location")[0].value = "";
        document.getElementsByName("date")[1].value = "";
        document.getElementsByName("consultantName")[1].value = "";
        document.getElementsByName("workNumber")[1].value = "";
        document.getElementsByName("contractor")[2].value = "";
        document.getElementsByName("location")[1].value = "";
        document.getElementsByName("consultantName")[2].value = "";
        document.getElementsByName("workNumber")[2].value = "";
        document.getElementsByName("contractor")[3].value = "";
        document.getElementsByName("date")[2].value = "";
        document.querySelectorAll(".selected-images").forEach(e => {
          e.innerHTML = "";
        });
        closeOperationForm();
        getOperations();
      }
    });
  }
  else{
  $.ajax({
    url: "/",
    data: formData,
    type: 'POST',
    dataType: 'json',
    mimeType: 'multipart/form-data',
    contentType: false,
    cache: false,
    processData: false,
    success: function(res) {
      this_el.removeAttribute("style");
      this_el.scrollTo(0,0);
      document.getElementById("new").checked = true;
      document.getElementsByName("assayNum")[0].value = "";
      document.getElementsByName("missionNum")[0].value = "";
      document.getElementsByName("permitType")[0].value = "";
      document.getElementsByName("contractorName")[0].value = "";
      document.getElementsByName("station")[0].value = "";
      document.getElementsByName("neighborhood")[0].value = "";
      document.getElementsByName("depthOfExcavation")[0].value = "";
      document.getElementsByName("fossilView")[0].value = "";
      document.getElementsByName("cableLength")[0].value = "";
      document.querySelectorAll(".selected-images").forEach(e => {
        e.innerHTML = "";
      });
      permitsCount = 0;
      emergencyFileCount = 0;
      substitutionFileCount = 0;
      reinforcementFileCount = 0;
      effortFileCount = 0;
      violationsFileCount = 0;
      teamModelsCount = 0;
      preWorkMeetingsCount = 0;
      riskAssessmentsCount = 0;
      safeWorkProceduresCount = 0;
      paramedicsCount = 0;
      fightersCount = 0;
      assignedTasksCount = 0;
      artificialSecurityCardsCount = 0;
      recipientsCount = 0;
      sourcesCount = 0;
      tuvForEquipmentAndDriversCount = 0;
      fireExtinguishersCount = 0;
      firstAidsCount = 0;
      workTeamsCount = 0;
      picturesOfSitesCount = 0;
      subscriptionNumbersCount = 0;
      cutterCapacitysCount = 0;
      countersCount = 0;
      missionLocksCount = 0;
      safetyBarriersCount = 0;
      objectsCount = 0;
      obstaclesCount = 0;
      violationsCount = 0;
      closeAssayForm();
      getAssays();
    }
  });
}
});

$(document).on("submit",".login-form",function(e){
  e.preventDefault();
  this_el = this;
  this_el.style.opacity = "0.7";
  var formData = new FormData(this);
  $.ajax({
    url: location.href,
    data: formData,
    type: 'POST',
    dataType: 'json',
    mimeType: 'multipart/form-data',
    contentType: false,
    cache: false,
    processData: false,
    success: function(res) {
      this_el.removeAttribute("style");
      if(res.ierr == "snack"){
        snackBar(res.errtitle);
      }else{
        location.href="/";
      }
    }
  });
});

function rettext(value) {
	if (value) {
		return $('<div/>').text(value).html();
	} else {
		return '';
	}
}

snack_wit = false;
added_snack = [];
snacks = 0;
function snackBar(title , tp="0"){
	if(tp == "1"){
		if(snack_wit == false){
			snack_wit = true;
			document.getElementById("snackbar").removeAttribute("style");
			setTimeout(function(){
				document.getElementById("snackbar").style.bottom="20px";
				document.getElementById("snackbarText").innerHTML = String(rettext(title));
				setTimeout(function(){
					document.getElementById("snackbar").removeAttribute("style");
					snack_wit = false;
					snacks -= 1;
					if(snacks == 0){}
					else{
						otherSnackbar(added_snack[snacks]);
					}
				} , 5000);
			},250);
		}
	}else{
		added_snack.push(String(rettext(title)));
		snacks += 1;
		if(snack_wit == false){
			snack_wit = true;
			document.getElementById("snackbar").removeAttribute("style");
			setTimeout(function(){
				document.getElementById("snackbar").style.bottom="20px";
				document.getElementById("snackbarText").innerHTML = String(rettext(title));
				setTimeout(function(){
					document.getElementById("snackbar").removeAttribute("style");
					snack_wit = false;
					snacks -= 1;
					if(snacks == 0){}
					else{
						otherSnackbar(added_snack[snacks]);
					}
				} , 5000);
			},250);
		}
	}
}
function otherSnackbar(title){
	if(snack_wit == false){
		snack_wit = true;
		document.getElementById("snackbar").removeAttribute("style");
		setTimeout(function(){
			document.getElementById("snackbar").style.bottom="20px";
			document.getElementById("snackbarText").innerHTML = String(title);
			setTimeout(function(){
				document.getElementById("snackbar").removeAttribute("style");
				snack_wit = false;
				snacks -= 1;
				if(snacks <= 0){}
				else{
					snackBar(added_snack[snacks],"1");
				}
			} , 5000);
		},250);
	}
}

$(document).on("click","#temp",function(){
  document.getElementById("checkType").value = "temp";
});
$(document).on("click","#new",function(){
  document.getElementById("checkType").value = "new";
});

function getAssays(){
  $.ajax({
    url: '/',
    data: {getData:""},
    type: 'GET',
    success: function(res) {
      document.getElementById("assaysList").innerHTML = "";
      res.data.forEach(d => {
        $(".list").append("<p class='list-header'>"+rettext(d[0])+"</p>");
        d[1].forEach(f => {
          $(".list").append("<button data-assay="+rettext(f[0])+" class='btn'><p>"+rettext(f[0])+"</p><div>"+rettext(f[1])+"</div><span>"+rettext(f[2])+"</span></button>");
        });
      });
    }
  });
}

$(document).on("click","[data-href]",function(){
  location.href = this.dataset.href;
});

function getViewAssay(assayId){
  // success
  $.ajax({
    url: '/',
    data: {getAssayData:assayId},
    type: 'GET',
    success: function(res) {
      document.getElementById("orderType").innerHTML = res.data[0];
      document.getElementById("missionNumber").innerHTML = res.data[1];
      document.getElementById("perType").innerHTML = res.data[2];
      document.getElementById("conName").innerHTML = res.data[3];
      document.getElementById("station").innerHTML = res.data[4];
      document.getElementById("neighborhood").innerHTML = res.data[5];
      document.getElementById("depthOfExcavation").innerHTML = res.data[6];
      document.getElementById("fossilView").innerHTML = res.data[7];
      document.getElementById("cableLength").innerHTML = res.data[8];
      closeAssayForm();
      closeSettings();
      closeSearch();
      closeUserForm();
      viewAssay = document.querySelector("#assayForm");
      viewAssay.style.display="block";
      setTimeout(function(){
          viewAssay.style.marginBottom="0";
          viewAssay.style.opacity="1";
          viewAssay.style.transform="scale(1)";
      }, 200);
      document.querySelector(".selected").classList.remove("selected");
      document.getElementById("home").classList.add("selected");
      document.getElementById("imagesCard").innerHTML = "";
      res.data[9].forEach(d => {
        $(".image-card").append("<img src='"+rettext(d)+"'><div class='line'></div>");
      });
      document.getElementById("assayNum").innerHTML = rettext(res.data[10]);
      document.getElementById("exportBtn").dataset.href = "/export/"+res.data[11];
    }
  });
}



function getViewOperation(operationID){
  // success
  $.ajax({
    url: '/operations',
    data: {getOperationData:operationID},
    type: 'GET',
    success: function(res) {
      document.querySelectorAll(".labels").forEach(labels => {
        labels.removeAttribute("style");
      });
      if(res.data[0] == "emergency"){
        document.getElementById("emergencyLabels").style.display="block";
        document.getElementById("assayNum").textContent= res.data[1];
        document.getElementById("malfunctionNumber").textContent = res.data[2];
        document.getElementById("malfunctionType").textContent = res.data[3];
        document.getElementById("contractor").textContent = res.data[4];
        document.getElementById("date").textContent = res.data[5];
        document.getElementById("materials").textContent = res.data[6];
        document.getElementById("consultantName").textContent = res.data[7];
      }
      else if(res.data[0] == "substitution"){
        document.getElementById("substitutionLabels").style.display="block";
        document.getElementById("assayNum").textContent= res.data[1];
        document.getElementById("workNumber").textContent = res.data[2];
        document.getElementById("contractor1").textContent = res.data[3];
        document.getElementById("employmentType").textContent = res.data[4];
        document.getElementById("site").textContent = res.data[5];
        document.getElementById("date1").textContent = res.data[6];
        document.getElementById("consultantName1").textContent = res.data[7];
      }
      else if(res.data[0] == "reinforcement"){
        document.getElementById("reinforcementLabels").style.display="block";
        document.getElementById("assayNum").textContent= res.data[1];
        document.getElementById("workNumber1").textContent = res.data[2];
        document.getElementById("contractor2").textContent = res.data[3];
        document.getElementById("site1").textContent = res.data[4];
        document.getElementById("date2").textContent = res.data[5];
        document.getElementById("consultantName2").textContent = res.data[6];
      }
      else if(res.data[0] == "effort"){
        document.getElementById("effortLabels").style.display="block";
        document.getElementById("assayNum").textContent= res.data[1];
        document.getElementById("workNumber2").textContent = res.data[2];
        document.getElementById("contractor3").textContent = res.data[3];
        document.getElementById("site2").textContent = res.data[4];
        document.getElementById("date3").textContent = res.data[5];
      }else{
        document.getElementById("assayNum").textContent= res.data[1];
      }
      // document.getElementById("orderType").innerHTML = res.data[0];
      // document.getElementById("missionNumber").innerHTML = res.data[1];
      // document.getElementById("perType").innerHTML = res.data[2];
      // document.getElementById("conName").innerHTML = res.data[3];
      // document.getElementById("station").innerHTML = res.data[4];
      // document.getElementById("neighborhood").innerHTML = res.data[5];
      // document.getElementById("depthOfExcavation").innerHTML = res.data[6];
      // document.getElementById("fossilView").innerHTML = res.data[7];
      // document.getElementById("cableLength").innerHTML = res.data[8];
      // closeAssayForm();
      // closeSettings();
      // closeSearch();
      // closeUserForm();
      viewAssay = document.querySelector("#assayForm");
      viewAssay.style.display="block";
      setTimeout(function(){
          viewAssay.style.marginBottom="0";
          viewAssay.style.opacity="1";
          viewAssay.style.transform="scale(1)";
      }, 200);
      document.getElementById("pdfAttachments").innerHTML = "";
      res.data[res.data.length-1].forEach(pdfAttachment => {
        $(".image-card").append("<a target='_blank' href='"+rettext(pdfAttachment[0])+"'>"+rettext(pdfAttachment[1])+"</a>");
      });

      // res.data[-1].forEach(d => {
      //   $(".image-card").append("<img src='"+rettext(d)+"'><div class='line'></div>");
      // });
      // document.getElementById("assayNum").innerHTML = rettext(res.data[10]);
    }
  });
}


$(document).on("click","[data-assay]",function(){
  getViewAssay(this.dataset.assay);
});
$(document).on("click","[data-operation]",function(){
  getViewOperation(this.dataset.operation);
});

$(document).on("keydown","#searchInput",function(){
  setTimeout(function(){
    searchAssay(document.getElementById("searchInput").value);
  },1);
});

$(document).on("change","#searchInput",function(){
  setTimeout(function(){
    getViewAssay(document.getElementById("searchInput").value);
  },1);
});

function searchAssay(assayId){
  $.ajax({
    url: '/',
    data: {search:assayId},
    type: 'GET',
    success: function(res) {
      document.getElementById("searchBox").innerHTML = "";
      res.data.forEach(d => {
        $(".search-box").append("<button data-assay=\""+rettext(d[0])+"\" class='btn list-button'><p>"+rettext(d[0])+"</p><div>"+rettext(d[1])+"</div><span>"+rettext(d[2])+"</span></button>");
      });
    }
  });
}

$(document).on("click","#addUser",function(){

});