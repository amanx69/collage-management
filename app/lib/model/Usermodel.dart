class UserModel {
  final String email;
  final String fullName;
  final String? phone;
  final String? bio;
  final String? profileImage;
  final String? branch;
  final DateTime? createdAt;
  final DateTime? dateOfBirth;
  final bool isActive;
  final bool isStaff;

  UserModel({
    required this.email,
    required this.fullName,
    this.phone,
    this.bio,
    this.profileImage,
    this.branch,
    this.createdAt,
    this.dateOfBirth,
    required this.isActive,
    required this.isStaff,
  });

  // Factory method to create a UserModel from JSON
  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      email: json['email'] ?? '',
      fullName: json['full_name'] ?? '',
      phone: json['phone'],
      bio: json['bio'],
      profileImage: json['profile_image'],
      branch: json['branch'],
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'])
          : null,
      dateOfBirth: json['dateofbirth'] != null
          ? DateTime.tryParse(json['dateofbirth'])
          : null,
      isActive: json['is_active'] ?? true,
      isStaff: json['is_staff'] ?? false,
    );
  }

  // Convert UserModel to JSON (optional, useful for POST/PUT)
  Map<String, dynamic> toJson() {
    return {
      "email": email,
      "full_name": fullName,
      "phone": phone,
      "bio": bio,
      "profile_image": profileImage,
      "branch": branch,
      "created_at": createdAt?.toIso8601String(),
      "dateofbirth": dateOfBirth?.toIso8601String(),
      "is_active": isActive,
      "is_staff": isStaff,
    };
  }
}
