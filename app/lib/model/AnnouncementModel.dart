class Announcementmodel {
  final String type;
  final String title;
  final String description;
  final DateTime createdOn;
  final String? file;   
  final String? image; 
  Announcementmodel({
    required this.type,
    required this.title,
    required this.description,
    required this.createdOn,
    this.file,
    this.image,
  });

  //! JSON → Data
  factory   Announcementmodel.fromJson(Map<String, dynamic> json) {
    return  Announcementmodel(
      type: json['type'],
      title: json['title'],
      description: json['description'],
      createdOn: DateTime.parse(json['createdon']),
      file: json['file'],
      image: json['image'],
    );
  }

  //! Data to  → JSON
  Map<String, dynamic> toJson() {
    return {
      'type': type,
      'title': title,
      'description': description,
      'createdon': createdOn.toIso8601String(),
      'file': file,
      'image': image,
    };
  }
}
