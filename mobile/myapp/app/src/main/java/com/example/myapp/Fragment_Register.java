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

public class Fragment_Register extends Fragment {
    TextInputEditText textInputEditTextFullname, textInputEditTextEmail, textInputEditTextPassword, textInputEditTextRetypePassword;
    Button btn_register;
    ProgressBar progressBar;

    public Fragment_Register() {
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment__register, container, false);

        textInputEditTextFullname = view.findViewById(R.id.Fullname);
        textInputEditTextEmail = view.findViewById(R.id.Email);
        textInputEditTextPassword = view.findViewById(R.id.Password);
        textInputEditTextRetypePassword = view.findViewById(R.id.RetypePassword);
        btn_register = view.findViewById(R.id.btn_register); // Initialize btn_register

        progressBar = view.findViewById(R.id.progressBar);

        btn_register.setOnClickListener(view1 -> {
            String fullname = String.valueOf(textInputEditTextFullname.getText());
            String email = String.valueOf(textInputEditTextEmail.getText());
            String password = String.valueOf(textInputEditTextPassword.getText());
            String confirm_password = String.valueOf(textInputEditTextRetypePassword.getText());

            if (!fullname.equals("") && !email.equals("") && !password.equals("") && !confirm_password.equals("")) {
                progressBar.setVisibility(View.VISIBLE);
                Handler handler = new Handler();
                handler.post(() -> {
                    String[] field = new String[4];
                    field[0] = "fullname";
                    field[1] = "email";
                    field[2] = "password";
                    field[3] = "confirm_password";

                    String[] data = new String[4];
                    data[0] = fullname;
                    data[1] = email;
                    data[2] = password;
                    data[3] = confirm_password;

                    PutData putData = new PutData("http://localhost:63343/LoginRegister/signup.php", "POST", field, data);
                    if (putData.startPut()) {
                        if (putData.onComplete()) {
                            progressBar.setVisibility(View.GONE);
                            String result = putData.getResult();

                            if (result.equals("Sign Up Success")) {
                                Toast.makeText(getContext(), result, Toast.LENGTH_SHORT).show();
                                Intent intent = new Intent(getContext(), Fragment_login.class);
//                                startActivity(intent);

                                if (getActivity() != null) {
                                    getActivity().finish();
                                }
                            } else {
                                Toast.makeText(getContext(), result, Toast.LENGTH_SHORT).show();
                            }

                            Log.i("PutData", result);
                        }
                    }
                });
            } else {
                Toast.makeText(getContext(), "All fields required", Toast.LENGTH_SHORT).show();
            }
        });

        return view; // Return the inflated view
    }
}
