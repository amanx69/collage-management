import 'package:app/model/Usermodel.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';

part 'SingUp.g.dart';
  @riverpod 
class Singup  extends _$Singup {
  @override

  AsyncValue<UserModel> build() {
    

    return const AsyncValue.loading();
  } 



 
}