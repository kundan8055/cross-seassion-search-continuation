var domain="";
var myUrl="";
chrome.tabs.query({'active':true,'windowId':chrome.windows.WINDOW_ID_CURRENT},
          function(tabs){
                  myUrl=tabs[0].url;
		//document.write(myUrl);
		dom();	
		//document.write(myUrl);
		

		bhejophp();
           }
 );





function dom(){


var flag=0;

for(var i=0;i<myUrl.length;i++){
	//document.write(myUrl[i]);
if(myUrl[i]=='/' && myUrl[i-1]=='/')
{flag=1;
	continue;
}
if(flag==1)
{	//document.write(myUrl[i]);
	domain=domain+myUrl[i];
}
if(myUrl[i+1]=='/' && flag==1)
{
break;
}
}
 
}




function bhejophp() {
	
     var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     // document.write(this.responseText);
    }
  };
  xhttp.open("POST","http://localhost/stp/inter.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send('a='+myUrl+'&'+'b='+domain); 
}
