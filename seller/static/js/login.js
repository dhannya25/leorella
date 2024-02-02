function po(){
        
            email=document.getElementById("email").value 
        
            password=document.getElementById("password").value 
            
            
            if(email==""){
                document.getElementById('pa').innerHTML="pls enter email"
                return false

            
            }else if (password==""){
                document.getElementById('pa').innerHTML= "pls enter password"
                return false
            
            // }else if(password.length<6){
            //     document.getElementById('pa').innerHTML="pls enter max 6 charater"
            //     return false
            }
            else{
                return true
            }
                
        }  
