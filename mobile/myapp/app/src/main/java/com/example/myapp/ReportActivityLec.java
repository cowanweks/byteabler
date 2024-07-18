package com.example.myapp;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class ReportActivityLec extends AppCompatActivity {

    private ListView studentListView;
    private StudentAdapter adapter;
    private ArrayList<Student> students;
    private ImageView report_lec;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.report_lec_attend);

        studentListView = findViewById(R.id.studentList);
        Button submitButton = findViewById(R.id.submitButton);
        TextView dateTextView = findViewById(R.id.dateTextView);
        TextView unitTextView = findViewById(R.id.unitTextView);
        report_lec = findViewById(R.id.report_lec);

        // Set the date and unit text (you may fetch this data dynamically)
        dateTextView.setText("Date: 12/06/2024");
        unitTextView.setText("Unit: Mathematics");

        // Initialize student list
        students = new ArrayList<>();
        students.add(new Student("Student 1", false));
        students.add(new Student("Student 2", false));
        students.add(new Student("Student 3", false));

        // Set up the adapter
        adapter = new StudentAdapter(this, students);
        studentListView.setAdapter(adapter);

        // Set up the submit button listener
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                handleAttendanceSubmission();
            }
        });
    }

    private void handleAttendanceSubmission() {
        // Collect attendance data
        StringBuilder attendanceReport = new StringBuilder("Attendance Report:\n");
        for (Student student : students) {
            attendanceReport.append(student.getName())
                    .append(": ")
                    .append(student.isAttended() ? "Present" : "Absent")
                    .append("\n");
        }

        // Show a Toast message or handle the submission logic here
        Toast.makeText(this, attendanceReport.toString(), Toast.LENGTH_LONG).show();

        // You can also send this data to a server or save it in a database
    }
}
