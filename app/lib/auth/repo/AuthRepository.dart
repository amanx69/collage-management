

import 'dart:developer';

import 'package:app/core/service.dart';
import 'package:dio/dio.dart';




class  Authrepository {
   final  dio=  Dio(
     BaseOptions(
      
       connectTimeout: Duration(seconds: 10),
       receiveTimeout: Duration(seconds: 10),
       headers: {"Content-Type": "application/json"}
     )
   );


    Future<String>singup({required String email,required String password ,required String name})async{


        try {
           
            final  api= "${apis.api}/signup";

            log(name);
            log(email);
            log(password);


       final  response  =  await dio.post(api,
       data: {
        
         "email":email,
        "password":password,
        "full_name":name
       
       }
       );
       if(response.statusCode == 200){
        
        return "Singup successful";
         
       }else{
         return "Singup failed";
       }
              
    }
         catch (e) {
          print(e);
          log(e.toString());
          return e.toString();
        }
      
    
    }
}
     
      
       

         
    
    