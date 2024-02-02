function po(){
    name=document.getElementById("name").value 
    email=document.getElementById("email").value
     number=document.getElementById("number").value 
    password=document.getElementById("password").value 
    comformpassword=document.getElementById("comformpassword").value 
    if(name==""){
        document.getElementById('pa').innerHTML="pls enter username"
        return false
    }
    else if(email==""){
        document.getElementById('pa').innerHTML="pls enter email"
        return false

    }else if(number==""){
        document.getElementById('pa').innerHTML= "enter 6 digits"
        return false
    }else if (password==""){
        document.getElementById('pa').innerHTML= "pls enter password"
        return false
    }else if(comformpassword==""){
        document.getElementById('pa').innerHTML="pls enter comform password"
        return false
    }else if(password.length<6){
        document.getElementById('pa').innerHTML="pls enter max 6 charater"
        return false
    }else if(password!=comformpassword){
        document.getElementById('pa').innerHTML="password must be same"
        return false
        
    }
    else{ 
        
        return true
    }
}
