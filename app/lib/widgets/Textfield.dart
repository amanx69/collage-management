import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:google_fonts/google_fonts.dart';

class CustomTextField extends StatefulWidget {
  final String hintText;
  final IconData? prefixIcon;
  final IconData? suffixIcon;
  final bool isPassword;
  final TextEditingController controller;
  

  const CustomTextField({
    Key? key,
    required this.hintText,
     this.prefixIcon,
    this.suffixIcon,
    this.isPassword = false,
    required   this.controller
  }) : super(key: key);

  @override
  State<CustomTextField> createState() => _CustomTextFieldState();
}

class _CustomTextFieldState extends State<CustomTextField> {
  bool _obscureText = true;

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: widget.controller,
      style:GoogleFonts.lato(color:  Colors.white),
      obscureText: widget.isPassword ? _obscureText : false,
      decoration: InputDecoration(
        
        hintText: widget.hintText,
        prefixIcon: Icon(widget.prefixIcon ,),
        suffixIcon: widget.isPassword
            ? IconButton(
                icon: Icon(
                  _obscureText ? Icons.visibility_off : Icons.visibility,
                  
                ),
                onPressed: () {
                  setState(() {
                    _obscureText = !_obscureText;
                  });
                },
              )
            : (widget.suffixIcon != null
                ? Icon(widget.suffixIcon, )
                : null),
      

        contentPadding: EdgeInsets.symmetric(vertical:15.h, horizontal: 20.w),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(15),
          borderSide: BorderSide.none,
        ),
      ),
    );
  }
}
