import 'package:app/auth/ui/SingupPage.dart';
import 'package:app/helper/ThemeData.dart';
import 'package:app/screen/home.dart';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

void main() {
  ProviderScope(child:const MyApp());
        runApp(const MyApp());
  
} 

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  
  @override
  Widget build(BuildContext context) {
    return ScreenUtilInit(
      designSize: const Size(375, 812),  
      minTextAdapt: true,
      splitScreenMode: true,
      builder: (context, child) {
        return MaterialApp(
          
         debugShowCheckedModeBanner: false,
          theme: AppTheme.lightTheme,   // ! light
          darkTheme: AppTheme.darkTheme, //! dark
             themeMode: ThemeMode.system,  // !auto switch with system

             
            
        
          home: child,
        );
      },
      child: const Singuppage(),
    );
  }
}



