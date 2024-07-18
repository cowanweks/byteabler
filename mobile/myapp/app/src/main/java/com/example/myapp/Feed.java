package com.example.myapp;

import android.content.Context;
import android.content.Intent;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;

public class Feed extends LinearLayout {

    public Feed(Context context, AttributeSet attrs) {
        super(context, attrs);
        init(context);
    }
    ListView smsListView;
    TextView feedText;
    ImageView feedIcon;
    public Feed(Context context) {
        super(context);
        init(context);
    }

    private void init(final Context context) {
        LayoutInflater.from(context).inflate(R.layout.activity_messages, this, true);
        smsListView = findViewById(R.id.SMSList);
        feedText = findViewById(R.id.textView);
        feedIcon = findViewById(R.id.feedIcon);

        // Set a click listener to open MessagesActivity
        this.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(context, MessagesActivity.class);
                context.startActivity(intent);
            }
        });
    }
}
