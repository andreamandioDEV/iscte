$(document).ready(function(){

    //Todas as ucs do plano de estudos começam escondidads
    $("[id*='uc-details-']").css('display', 'none');  

    //Mostra os detalhes da uc após o clique na seta e muda a orientação da seta
    if (location.pathname.substring(1) == "plano-estudos"){
        $("i.clickable").click(function(element){  
            id = element.target.id;
            if(element.target.className  == "fa fa-arrow-down clickable"){
                $("#uc-details-"+id).show(800);
                element.target.className = "fa fa-arrow-up clickable";
            }else{
                $("#uc-details-"+id).hide(300);
                element.target.className = "fa fa-arrow-down clickable";
            }
        });
    }

    sliderToggle("cv-arrow", "resume");
    sliderToggle("academic-arrow", "academic");
    sliderToggle("uc-arrow", "uc");
    sliderToggle("pub-arrow", "publications");

    if (location.pathname.substring(1) == "estatisticas"){
        $("i.clickable").click(function(element){  
            id = element.target.id;
            if (id.match(/etcs-ucs/)){
                graphManagement("etcs-ucs", element, "etcs_uc");
            }else if (id.match(/pub-year/)){
                graphManagement("pub-year", element, "publications_year");
            }else if (id.match(/teacher-ct/)){
                graphManagement("teacher-ct", element, "teacher_ct");
            }
            
            
        });
    }

});

/*
Função para a página do docentes
para slowDown slowUp do conteúdo
*/
function sliderToggle(arrow, content){
    $("#"+arrow).click(function(element){ 
        $("#"+content).slideToggle("slow"); 
        if(element.target.className == "fa fa-arrow-up clickable"){
            element.target.className = "fa fa-arrow-down clickable";
        }else{
            element.target.className = "fa fa-arrow-up clickable";
        }
    });
}

/*
Função para a página das estatísticas
para trocar gráficos após o clique
*/
function graphManagement(mainName,element,imageName){
    id = element.target.id;
    image = document.getElementById(mainName+"-img")
    console.log(mainName+" "+imageName+" "+id)
    if(id  == mainName+"-bar-chart"){
         element.target.className = "fa fa-bar-chart clickable graph-btn active";
         document.getElementById(mainName+"-line-chart").className = "fa fa-line-chart clickable graph-btn";
         image.src = "static/images/plot/"+imageName+"_bar.png";
    }else{
         element.target.className = "fa fa-line-chart clickable graph-btn active";
         document.getElementById(mainName+"-bar-chart").className = "fa fa-bar-chart clickable graph-btn";
         image.src = "static/images/plot/"+imageName+"_linear.png";
    }
}