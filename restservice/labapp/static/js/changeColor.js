
var massivSpecialists = [];
var positionSpecialists = [];
function createRequestObject()   
{  
    try { return new XMLHttpRequest() }  
    catch(e)   
    {  
        try { return new ActiveXObject('Msxml2.XMLHTTP') }  
        catch(e)   
        {  
            try { return new ActiveXObject('Microsoft.XMLHTTP') }  
            catch(e) { return null; }  
        }  
    }  
}  
var link='/mas/json/specialists'
var http = createRequestObject();  
    if( http )   
    {  
        http.open('get', link);  
        http.onreadystatechange = function ()   
        {  
            if(http.readyState == 4)   
            {  
                console.log(JSON.parse(http.responseText));
                massivSpecialists=JSON.parse(http.responseText).specialists;
                console.log(massivSpecialists);
                for(var i=0;i<massivSpecialists.length;i++){
                    positionSpecialists[i]=massivSpecialists[i].position;
                    
                }
                console.log(positionSpecialists);
                var select = document.getElementById("selectSpec");
                for(var i=0; i<positionSpecialists.length;i++){
                    select.options[i]= new Option(positionSpecialists[i], i);
                }
            }  
        }  
        http.send(null);      
    }  
    else   
    {  
        document.location = link;  
    }
var massivTime=[];
var massivTimeTemp=[];
var massivData=[];
var massivVremya=[];
var massivDataVremyaTemp=[];
var linkD ='/mas/json/schedule'
var httpD = createRequestObject();  
    if( httpD )   
    {  
        httpD.open('get', linkD);  
        httpD.onreadystatechange = function ()   
        {  
            if(httpD.readyState == 4)   
            {  
                console.log(JSON.parse(httpD.responseText).Schedule);
                massivTimeTemp=JSON.parse(httpD.responseText).Schedule;
                for (var i=4;i<massivTimeTemp.length;i++){
                    massivTime[i-4]=massivTimeTemp[i]
                }
                console.log(massivTime)
            }  
        }  
        httpD.send(null);      
    }  
    else   
    {  
         document.location = link;  
    }      

    

function Change(){
    massivData=[]
    massivVremya=[]
    massivDataVremyaTemp=[]
    var vrachValue=parseInt(document.getElementById('selectSpec').value)+parseInt(1)
    console.log(vrachValue)
    for (var i=0;i<massivTime.length;i++){
        if (massivTime[i].ids==vrachValue){
            //console.log(massivTime[i])
            massivDataVremyaTemp.push(massivTime[i].date)
        }
    }
    for (var i=0; i<massivDataVremyaTemp.length;i++){

    
    //"Tue, 29 Jun 2021 11:00:00 GMT"
    var dateTemp=massivDataVremyaTemp[i].split('2021 ')
    dateTemp[0]=dateTemp[0]+'2021'
    //место для исправления часов

    massivData.push(dateTemp[0])
    massivVremya.push(dateTemp[1])
    }


    var selectDate = document.getElementById("selectDate");
    var length = selectDate.options.length;
    for (i = length-1; i >= 0; i--) {
      selectDate.options[i] = null;
    }

    var selectTime = document.getElementById("selectTime");
    var length = selectTime.options.length;
    for (i = length-1; i >= 0; i--) {
      selectTime.options[i] = null;
    }
    //console.log(massivDataVremyaTemp)
    //console.log(dateTemp)
    console.log(massivData)
    console.log(massivVremya)
    var objSelTime = document.getElementById("selectTime");
    var objSelDate = document.getElementById("selectDate");
    for (i=0;i<massivData.length;i++){

        //objSelTime.options[i] = new Option(massivVremya[i],i)
        objSelDate.options[i] = new Option(massivData[i],massivData[i]);
    }
    
}

function ChangeSelectDate(){
    var tempVremya=[]
    var objSelTime = document.getElementById("selectTime");
    var n = document.getElementById("selectDate").options.selectedIndex;
    console.log(n)
    var mdTemp= massivData[n]
    for (i=0;i<massivData.length;i++){
        if (massivData[i]==mdTemp){
            //objSelTime.options[i] = new Option(massivVremya[i],i);
            tempVremya.push(massivVremya[i])
            console.log(mdTemp,massivVremya[i])
        }
    }
    for(i=0; i<tempVremya.length;i++){
        objSelTime.options[i] = new Option(tempVremya[i],tempVremya[i]);
    }


}



function sendForm(){
    
    var date = document.getElementById('date').value;
    console.log(date);
    var time = document.getElementById('time').value;
    console.log(time)
    var n = document.getElementById("selectSpec").options.selectedIndex;
    var specialist = document.getElementById("selectSpec").options[n].text;
    console.log(specialist);
}
/*
<div>
    <label for="selectDate">Дата</label>
    <input id='selectDate' type="date" required='required' name='date' id='date'>
</div>

<div>
    <label for="selectTime">Время</label>
    <input id='selectTime' type="time" required='required' name='time' id='time'>
</div>
-->
    
    <div class='custom-dropdown big'>
                <select name="day" required="required">
                    <option value="">Дата</option>
                    <option value="1">Дерматолог</option>
                    <option value="2">Стоматолог</option>
                    <option value="3">Терапевт</option>
                    <option value="4">Травматолог</option>
                    <option value="5">25 июня</option>
                    <option value="6">26 июня</option>
                    <option value="7">27 июня</option>
                </select>
            </div>
            <div class='custom-dropdown big'>
                <select name="time" required="required">
                    <option value="">Время</option>
                    <option value="1">9:00</option>
                    <option value="2">10:00</option>
                    <option value="3">11:00</option>
                    <option value="4">12:00</option>
                </select>
            </div>
            */