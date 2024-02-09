package com.example.myapp;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.google.android.material.textfield.TextInputEditText;
import com.vishnusivadas.advanced_httpurlconnection.PutData;

public class Fragment_login extends Fragment {
    TextInputEditText textInputEditTextEmail, textInputEditTextPassword;
    Button btn_login;
    ProgressBar progressBar;

    public Fragment_login() {
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_login, container, false);

        textInputEditTextEmail = view.findViewById(R.id.et_email);
        textInputEditTextPassword = view.findViewById(R.id.Password);
        btn_login = view.findViewById(R.id.btn_login); // Initialize btn_login

        progressBar = view.findViewById(R.id.progressBar_login);

        btn_login.setOnClickListener(view1 -> {
            String email = String.valueOf(textInputEditTextEmail.getText());
            String password = String.valueOf(textInputEditTextPassword.getText());

            if (!email.equals("") && !password.equals("")) {
                progressBar.setVisibility(View.VISIBLE);
                Handler handler = new Handler();
                handler.post(() -> {
                    String[] field = new String[2];
                    field[0] = "email";
                    field[1] = "password";

                    String[] data = new String[2];
                    data[0] = email;
                    data[1] = password;

                    PutData putData = new PutData("http://localhost:63343/LoginRegiste/login.php", "POST", field, data);
                    if (putData.startPut()) {
                        if (putData.onComplete()) {
                            progressBar.setVisibility(View.GONE);
                            String result = putData.getResult();

                            if (result.equals("Login Success")) {
                                Toast.makeText(getContext(), result, Toast.LENGTH_SHORT).show();
                                Intent intent = new Intent(getContext(), MainActivity.class);
                                startActivity(intent);
                            } else {
                                Toast.makeText(getContext(), result, Toast.LENGTH_SHORT).show();
                            }

                            Log.i("PutData", result);
                        }
                    }
                });
            } else {
                Toast.makeText(getContext(), "Email and Password are required", Toast.LENGTH_SHORT).show();
            }
        });

        return view; // Return the inflated view
    }
}
