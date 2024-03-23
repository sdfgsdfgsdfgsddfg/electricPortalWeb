function openNav(){
    const aside = document.querySelector("aside");
    const w = window.innerWidth;
    if(aside.style.display == "none"){
        aside.style.display = "";
    }
    setTimeout(function(){
        if(aside.dir == ""){
            if(aside.style.left == "-100%"){
                if(w <= 600){
                    document.querySelector(".nd").style.display="block";
                    document.querySelector(".nd").style.backgroundColor="rgb(0,0,0,.5)";
                }
                document.querySelector("main").removeAttribute("style");
                document.querySelector("aside").style.left="0";
            }else{
                if(w <= 600){
                    document.querySelector(".nd").removeAttribute("style");
                }
                document.querySelector("main").style.left="0";
                document.querySelector("aside").style.left="-100%";
            }
        }else{
            if(aside.style.right == "-100%"){
                if(w <= 600){
                    document.querySelector(".nd").style.display="block";
                    document.querySelector(".nd").style.backgroundColor="rgb(0,0,0,.5)";
                }
                document.querySelector("main").removeAttribute("style");
                document.querySelector("aside").style.right="0";
            }else{
                if(w <= 600){
                    document.querySelector(".nd").removeAttribute("style");
                }
                document.querySelector("main").style.right="0";
                document.querySelector("aside").style.right="-100%";
            }
        }
    },.01);
}

$(document).on("click","#menu",function(){
    openNav();
});
const w = window.innerWidth;
if(w <= 600){
    const aside = document.querySelector("aside");
    aside.style.display = "none";
    if(aside.dir == ""){
        if(aside.style.left == "-100%"){
            document.querySelector("aside").style.left="0";
        }else{
            document.querySelector("aside").style.left="-100%";
        }
    }else{
        if(aside.style.right == "-100%"){
            document.querySelector("aside").style.right="0";
        }else{
            document.querySelector("aside").style.right="-100%";
        }
    }
}
$(document).on("click","aside ,.nd",function(){
    winWidth = $(window).width();
    if(winWidth <= 600){
        openNav();
    }
});


// function viewLoading(){
//     setTimeout(function(){
//         document.querySelector(".progress").style.transform = "scaleY(1)";
//         document.querySelector(".content").style.opacity = "0";
//     },.2);
// }


$(document).on("click","#addOperationBtn",function(){
    closeAssayViewer();
    closeSettings();
    closeAssayForm();
    addOperation = document.querySelector("#addOperationForm");
    addOperation.style.display="block";
    setTimeout(function(){
        addOperation.style.marginBottom="0";
        addOperation.style.opacity="1";
        addOperation.style.transform="scale(1)";
    }, 200);
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("operations").classList.add("selected");
});

$(document).on("click","#addUser",function(){
    closeAssayViewer();
    closeSettings();
    closeAssayForm();
    addUser = document.querySelector("#addUserForm");
    addUser.style.display="block";
    setTimeout(function(){
        addUser.style.marginBottom="0";
        addUser.style.opacity="1";
        addUser.style.transform="scale(1)";
    }, 200);
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("consultants").classList.add("selected");
});
$(document).on("click","#addAssay",function(){
    closeAssayViewer();
    closeSettings();
    addAssay = document.querySelector("#addAssayForm");
    addAssay.style.display="block";
    setTimeout(function(){
        addAssay.style.marginBottom="0";
        addAssay.style.opacity="1";
        addAssay.style.transform="scale(1)";
    }, 200);
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("addAssay").classList.add("selected");
});
function closeAssayForm(){
    addAssay = document.querySelector("#addAssayForm");
    addAssay.style.marginBottom="-120px";
    addAssay.style.opacity="0";
    addAssay.style.transform="scale(.7)";
    setTimeout(function(){
        addAssay.style.display="none";
    }, 200);
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("home").classList.add("selected");
}
function closeUserForm(){
    try{
        addUser = document.querySelector("#addUserForm");
        addUser.style.marginBottom="-120px";
        addUser.style.opacity="0";
        addUser.style.transform="scale(.7)";
        setTimeout(function(){
            addUser.style.display="none";
        }, 200);
        document.querySelector(".selected").classList.remove("selected");
        document.getElementById("consultants").classList.add("selected");
    }catch{}
}
function closeAssayViewer(){
    viewAssay = document.querySelector("#assayForm");
    viewAssay.style.marginBottom="-120px";
    viewAssay.style.opacity="0";
    viewAssay.style.transform="scale(.7)";
    setTimeout(function(){
        viewAssay.style.display="none";
    }, 200);
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("home").classList.add("selected");
}
function closeOperationForm(){
    document.querySelectorAll(".fpage").forEach(fpage=>{
        fpage.removeAttribute("style");
    });
    try{
        document.getElementById("page1").removeAttribute("style");
        operationForm = document.querySelector("#addOperationForm");
        operationForm.style.marginBottom="-120px";
        operationForm.style.opacity="0";
        operationForm.style.transform="scale(.7)";
        setTimeout(function(){
            operationForm.style.display="none";
        }, 200);
        document.querySelector(".selected").classList.remove("selected");
        document.getElementById("operations").classList.add("selected");
    }catch{}
}
function closeSettings(){
    settings = document.querySelector("#settingsForm");
    settings.style.marginBottom="-120px";
    settings.style.opacity="0";
    settings.style.transform="scale(.7)";
    setTimeout(function(){
        settings.style.display="none";
    }, 200);
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("home").classList.add("selected");
}
$(document).on("click",".back-btn,#home",function(){
    closeAssayForm();
    closeAssayViewer();
    closeSettings();
    closeUserForm();
    closeOperationForm();
});
$(document).on("click",".back-btn2,#consultants",function(){
    closeAssayForm();
    closeAssayViewer();
    closeSettings();
    closeUserForm();
    closeOperationForm();
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("consultants").classList.add("selected");
});

$(document).on("click",".back-btn3,#operations",function(){
    closeAssayForm();
    closeAssayViewer();
    closeSettings();
    closeUserForm();
    closeOperationForm();
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("operations").classList.add("selected");
});

$(document).on("click","#settings",function(){
    closeAssayForm();
    closeAssayViewer();
    closeUserForm();
    closeOperationForm();
    settings = document.querySelector("#settingsForm");
    settings.style.display="block";
    setTimeout(function(){
        settings.style.marginBottom="0";
        settings.style.opacity="1";
        settings.style.transform="scale(1)";
    }, 200);
    document.querySelector(".selected").classList.remove("selected");
    document.getElementById("settings").classList.add("selected");
});


$(document).on("click","#searchBtn",function(){
    document.getElementById("searchInput").value = "";
    document.querySelector(".search-group").style.display="block";
    document.querySelector(".search-box").classList.add("show-sb");
    document.getElementById("searchInput").focus();
});

function closeSearch(){
    document.querySelector(".search-group").removeAttribute("style");
    document.querySelector(".search-box").classList.remove("show-sb");
}
$(document).on("click",".close-search",function(){
    closeSearch();
});

$(document).on("click","#emergency",function(){
    document.querySelectorAll(".fpage").forEach(fpage=>{
        fpage.removeAttribute("style");
    });
    document.getElementById("emergencyForm").style.display = "block";
    document.getElementById("page1").style.marginLeft="-100%";
});
$(document).on("click","#substitution",function(){
    document.querySelectorAll(".fpage").forEach(fpage=>{
        fpage.removeAttribute("style");
    });
    document.getElementById("substitutionForm").style.display = "block";
    document.getElementById("page1").style.marginLeft="-100%";
});

$(document).on("click","#reinforcement",function(){
    document.querySelectorAll(".fpage").forEach(fpage=>{
        fpage.removeAttribute("style");
    });
    document.getElementById("reinforcementForm").style.display = "block";
    document.getElementById("page1").style.marginLeft="-100%";
});
$(document).on("click","#effort",function(){
    document.querySelectorAll(".fpage").forEach(fpage=>{
        fpage.removeAttribute("style");
    });
    document.getElementById("effortForm").style.display = "block";
    document.getElementById("page1").style.marginLeft="-100%";
});
$(document).on("click","#violations",function(){
    document.querySelectorAll(".fpage").forEach(fpage=>{
        fpage.removeAttribute("style");
    });
    document.getElementById("violationsForm").style.display = "block";
    document.getElementById("page1").style.marginLeft="-100%";
});