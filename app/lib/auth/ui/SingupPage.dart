import 'package:app/auth/repo/AuthRepository.dart';
import 'package:app/widgets/Textfield.dart';
import 'package:app/widgets/elevated.dart';
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:lottie/lottie.dart';

class Singuppage extends StatefulWidget {
  const Singuppage({super.key});

  @override
  State<Singuppage> createState() => _SinguppageState();
}
//! controlar  
TextEditingController gmail= TextEditingController();
TextEditingController password = TextEditingController();
TextEditingController name = TextEditingController();

class _SinguppageState extends State<Singuppage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      extendBodyBehindAppBar: false,
         appBar: AppBar(title: Text("Narrow"),),



         body: SingleChildScrollView(
          physics: NeverScrollableScrollPhysics(),
           child: Column(
            children: [
           
              
        
            
             
               Lottie.asset("animation/Login.json",height: 300.h,width: 300.w), //! animation 
               
               SizedBox(height: 5.h,),

           
           
             Padding(
               padding: const EdgeInsets.all(10),
               child: Container(
                
                child: Column(
                  children: [
                    CustomTextField(hintText: "Email", prefixIcon: Icons.email_outlined,controller: gmail,), //! gmail
               
                    SizedBox(height: 35.h,),
                    CustomTextField(hintText: "Password", suffixIcon:Icons.visibility,isPassword: true,prefixIcon: Icons.lock_outline,controller: password,), //! password 
                    CustomTextField(hintText: "name", suffixIcon:Icons.visibility,isPassword: true,prefixIcon: Icons.lock_outline,controller: name,), //! password 
                  ],
                )),
             ),
             SizedBox(height: 25.h,),
             //~ button  
              CustomButton(text: "SingUp", onPressed: (){
                 
               Authrepository().singup(email: gmail.text, password: password.text,name: name.text );

              })

          
           
                
           ],),
         ),
       
    );
  }
}