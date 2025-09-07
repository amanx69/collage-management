import 'dart:developer';
import 'package:app/core/service.dart';
import 'package:app/model/Usermodel.dart';
import 'package:flutter/material.dart';
import 'package:dio/dio.dart';


class StudentPage extends StatefulWidget {
  const StudentPage({super.key});

  @override
  State<StudentPage> createState() => _StudentPageState();
}

class _StudentPageState extends State<StudentPage> {
  final dio = Dio();

  Future<List<UserModel>> fetchStudents() async {
    try {
      final response = await dio.get("${apis.api}/data");
      log("Response: ${response.data}");

      if (response.data is List) {
        return (response.data as List)
            .map((e) => UserModel.fromJson(e))
            .toList();
      } else {
        log("Error: Response is not a List");
        return [];
      }
    } catch (e) {
      log("Error fetching students: $e");
      return [];
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Students")),
      body: FutureBuilder<List<UserModel>>(
        future: fetchStudents(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text("Error: ${snapshot.error}"));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return const Center(child: Text("No students found"));
          } else {
            final students = snapshot.data!;
            return ListView.builder(
              itemCount: students.length,
              itemBuilder: (context, index) {
                final student = students[index];
                return Card(
                  margin: const EdgeInsets.all(8),
                  child: ListTile(
                    title: Text(student.email),
                    subtitle: Text("Password: ${student.createdAt}"),
                    trailing: Text(student.createdAt.toString()),
                  ),
                );
              },
            );
          }
        },
      ),
    );
  }
}
