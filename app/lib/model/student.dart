class studentmodel{
  final int ?id;
  final String ?name;
  final String ?password;

  studentmodel({required this.id,required this.name,required this.password});


     
    
  factory studentmodel.fromJson(Map<String, dynamic> json) {
    return studentmodel(
      id: json['id'],
      name: json['username'],
      password: json['passwod'],
    );
  }


}