package com.example.myapp;

public class Student {
    private String name;
    private boolean attended;

    public Student(String name, boolean attended) {
        this.name = name;
        this.attended = attended;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isAttended() {
        return attended;
    }

    public void setAttended(boolean attended) {
        this.attended = attended;
    }
}
