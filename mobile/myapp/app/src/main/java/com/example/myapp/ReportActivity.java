package com.example.myapp;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.ListView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class ReportActivity extends AppCompatActivity {

    private ListView studentListView;
    private ArrayAdapter<Student> adapter;
    private ArrayList<Student> students;
    private ImageView reportIcon;

    @SuppressLint("ResourceType")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.report);

        // Initialize ListView and adapter
        studentListView = findViewById(R.id.studentList);

        students = new ArrayList<>();
        // Add dummy student data
        students.add(new Student("Student 1", false));
        students.add(new Student("Student 2", false));
        students.add(new Student("Student 3", false));
        // Initialize adapter
        adapter = new ArrayAdapter<Student>(this, R.id.studentNameTextView,R.id.report, students) {
            @NonNull
            @Override
            public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
                View view = super.getView(position, convertView, parent);
                // Get current student
                Student student = students.get(position);
                // Find the CheckBox in the item layout
                CheckBox checkBox = view.findViewById(R.id.attendanceCheckbox);
                // Set checked state based on student's attendance
                checkBox.setChecked(student.isAttended());
                // Handle checkbox click to update student's attendance
                checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
                    @Override
                    public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                        student.setAttended(isChecked);
                    }
                });
                return view;
            }
        };
        // Set adapter to ListView
        studentListView.setAdapter(adapter);
    }
}
