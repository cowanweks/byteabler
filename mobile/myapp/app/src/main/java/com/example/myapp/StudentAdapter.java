package com.example.myapp;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.CheckBox;
import android.widget.TextView;

import java.util.ArrayList;

public class StudentAdapter extends BaseAdapter {

    private Context context;
    private ArrayList<Student> students;

    public StudentAdapter(Context context, ArrayList<Student> students) {
        this.context = context;
        this.students = students;
    }

    @Override
    public int getCount() {
        return students.size();
    }

    @Override
    public Object getItem(int position) {
        return students.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.students_item_layout, parent, false);
        }

        Student student = students.get(position);

        TextView studentNameTextView = convertView.findViewById(R.id.studentNameTextView);
        CheckBox attendanceCheckbox = convertView.findViewById(R.id.attendanceCheckbox);

        studentNameTextView.setText(student.getName());
        attendanceCheckbox.setChecked(student.isAttended());

        attendanceCheckbox.setOnCheckedChangeListener((buttonView, isChecked) -> {
            student.setAttended(isChecked);
        });

        return convertView;
    }
}
