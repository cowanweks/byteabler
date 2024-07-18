package com.example.myapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.activity.compose.setContent
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column

import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.Text
import androidx.compose.material.TextField
import androidx.compose.material.TextFieldDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color


import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.constraintlayout.compose.ConstraintLayout
import androidx.constraintlayout.compose.Dimension

class ClassRepDashboard: AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        setContent {
            dashboard()
        }
    }

    @Preview
    @Composable
    fun dashboard() {
        Column(
            Modifier
                .fillMaxHeight()
                .fillMaxWidth()
                .background(color = Color(android.graphics.Color.parseColor("#EEEEFB"))),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            ConstraintLayout() {
                val (topImg, profile2) = createRefs()
                Box(

                    Modifier
                        .fillMaxWidth()
                        .height(245.dp)

                        .constrainAs(topImg) {
                            top.linkTo(parent.top)
                            start.linkTo(parent.start)
                        }
                        .background(
                            color = Color(android.graphics.Color.parseColor("#5E3BEE")),
                            shape = RoundedCornerShape(bottomEnd = 40.dp, bottomStart = 40.dp)
                        ))

                Row(
                    modifier = Modifier
                        .padding(top = 48.dp, start = 24.dp, end = 24.dp)
                        .fillMaxWidth()
                ) {

                    Column(
                        modifier = Modifier
                            .height(100.dp)
                            .padding(start = 14.dp)
                            .weight(0.7f),
                        verticalArrangement = Arrangement.Center,
                        horizontalAlignment = Alignment.Start
                    ) {
                        Text(
                            text = "Hello",
                            color = Color.White,
                            fontSize = 18.sp,

                            )
                        Text(
                            text = "David Friedman ",
                            color = Color.White,
                            fontSize = 22.sp,
                            fontWeight = FontWeight.Bold,
                            modifier = Modifier.padding(top = 14.dp)

                        )
                    }
                    Image(
                        painter = painterResource(id = R.drawable.profile),
                        contentDescription = null,
                        modifier = Modifier
                            .width(100.dp)
                            .height(100.dp)
                            .clickable { }
                    )
                }

                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.Center,
                    modifier = Modifier
                        .fillMaxWidth()

                        .padding(top = 24.dp, start = 24.dp, end = 24.dp)
                        .shadow(3.dp, shape = RoundedCornerShape(20.dp))
                        .background(
                            color = Color.White,
                            shape = RoundedCornerShape(20.dp)
                        )

                        .constrainAs(profile2) {
                            top.linkTo(topImg.bottom)
                            bottom.linkTo(topImg.bottom)
                            start.linkTo(parent.start)
                            end.linkTo(parent.end)
                        }

                ) {


                    Column(
                        modifier = Modifier
                            .padding(top = 12.dp, bottom = 12.dp, end = 12.dp)
                            .height(90.dp)
                            .width(90.dp)

                            .background(
                                color = Color(android.graphics.Color.parseColor("#B6C2FE")),
                                shape = RoundedCornerShape(20.dp)
                            ),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Image(
                            painter = painterResource(id = R.drawable.video_call),
                            contentDescription = null,
                            Modifier
                                .padding(top = 8.dp, bottom = 4.dp),
                        )
                        Text(
                            text = "Video Call",
                            fontSize = 14.sp,
                            fontWeight = FontWeight.Bold,
                            fontStyle = FontStyle.Italic,
                            color = Color(android.graphics.Color.parseColor("#5E3BEE"))
                        )
                    }
                    Column(
                        modifier = Modifier
                            .padding(top = 12.dp, bottom = 12.dp, end = 8.dp, start = 8.dp)
                            .height(90.dp)
                            .width(90.dp)
                            .background(
                                color = Color(android.graphics.Color.parseColor("#B6C2FE")),
                                shape = RoundedCornerShape(20.dp)
                            ),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Image(
                            painter = painterResource(id = R.drawable.notification),
                            contentDescription = null,
                            Modifier
                                .padding(top = 8.dp, bottom = 4.dp),
                        )
                        Text(
                            text = "Notification",
                            fontSize = 14.sp,
                            fontWeight = FontWeight.Bold,
                            fontStyle = FontStyle.Italic,
                            color = Color(android.graphics.Color.parseColor("#5E3BEE"))
                        )
                    }
                    Column(
                        modifier = Modifier
                            .padding(top = 12.dp, bottom = 12.dp, start = 12.dp)
                            .height(90.dp)
                            .width(90.dp)
                            .background(
                                color = Color(android.graphics.Color.parseColor("#B6C2FE")),
                                shape = RoundedCornerShape(20.dp)
                            ),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Image(
                            painter = painterResource(id = R.drawable.voice_call),
                            contentDescription = null,
                            Modifier
                                .padding(top = 8.dp, bottom = 4.dp),
                        )
                        Text(
                            text = "Voice Call",
                            fontSize = 14.sp,
                            fontWeight = FontWeight.Bold,
                            fontStyle = FontStyle.Italic,
                            color = Color(android.graphics.Color.parseColor("#5E3BEE"))
                        )
                    }

                }

            }
            ConstraintLayout(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(top = 15.dp, end = 15.dp, start = 24.dp)
                    .shadow(3.dp, shape = RoundedCornerShape(25.dp))
                    .height(160.dp)
                    .background(
                        brush = Brush.horizontalGradient(
                            colors = listOf(
                                Color(android.graphics.Color.parseColor("#7787F9")),
                                Color(android.graphics.Color.parseColor("#B6C2FE"))
                            )
                        ), shape = RoundedCornerShape(25.dp)
                    )

            ) {
                val (text1, table) = createRefs()
                Row {
                    Text(text = "Here are your classes today:",
                        fontSize = 18.sp, fontWeight = FontWeight.Bold,
                        color = Color.White,
                        modifier = Modifier
                            .padding(top = 8.dp,start = 8.dp, end = 8.dp)

                    )
                }

                LazyVerticalGrid(
                    columns = GridCells.Fixed(3),
                    modifier = Modifier
                        .constrainAs(table) {
                            top.linkTo(text1.bottom, margin = 16.dp)
                            start.linkTo(parent.start)
                            end.linkTo(parent.end)
                            bottom.linkTo(parent.bottom)
                        }
                        .fillMaxWidth()
                        .padding(16.dp)
                ) {
                    val tableData = listOf(
                        "Units", "Time", "Room",
                        "Math", "9:00 AM", "101",
                        "Science", "10:00 AM", "102",
                        "History", "11:00 AM", "103"
                    )
                    items(tableData) { item ->
                        Box(
                            contentAlignment = Alignment.Center,
                            modifier = Modifier
                                .padding(4.dp)
                                .background(Color.White, shape = RoundedCornerShape(8.dp))
                                .fillMaxSize()
                        ) {
                            Text(text = item, fontSize = 16.sp, color = Color.Black)
                        }
                    }
                }
            }
            var text by rememberSaveable { mutableStateOf("") }
            TextField(
                value = text, onValueChange = {
                    text = it
                },
                label = { Text(text = "Searching for....") },
                trailingIcon = {

                    Image(
                        painter = painterResource(id = R.drawable.search_icon),
                        contentDescription = null,
                        modifier = Modifier
                            .size(43.dp)
                            .padding(end = 6.dp)
                    )
                },
                shape = RoundedCornerShape(50.dp),
                colors = TextFieldDefaults.outlinedTextFieldColors(
                    backgroundColor = Color.White,
                    focusedBorderColor = Color.Transparent,
                    unfocusedBorderColor = Color.Transparent,
                    textColor = Color(android.graphics.Color.parseColor("#5e5e5e")),
                    unfocusedLabelColor = Color(android.graphics.Color.parseColor("#5e5e5e"))
                ),
                modifier = Modifier
                    .fillMaxWidth()

                    .padding(top = 24.dp, end = 24.dp, start = 24.dp)
                    .shadow(3.dp, shape = RoundedCornerShape(50.dp))
                    .background(Color.White, CircleShape)

            )

            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.Center,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(start = 16.dp, end = 16.dp, top = 24.dp)

            ) {


                Column(
                    modifier = Modifier

                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_1),
                        contentDescription = null,
                        Modifier
                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "Feed",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }
                Column(
                    modifier = Modifier
                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_2),
                        contentDescription = null,
                        Modifier
                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "Maps",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }
                Column(
                    modifier = Modifier

                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_3),
                        contentDescription = null,
                        Modifier
                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "Chats",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }
                Column(
                    modifier = Modifier

                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_4),
                        contentDescription = null,
                        Modifier
                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "Report",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }


            }
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.Center,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(start = 16.dp, end = 16.dp, top = 12.dp)

            ) {


                Column(
                    modifier = Modifier
                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_5),
                        contentDescription = null,
                        Modifier
                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "Calender",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }
                Column(
                    modifier = Modifier

                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_6),
                        contentDescription = null,
                        Modifier
                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "Tips",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }
                Column(
                    modifier = Modifier

                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_7),
                        contentDescription = null,
                        Modifier
                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "Settings",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }
                Column(
                    modifier = Modifier
                        .weight(0.25f),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Image(
                        painter = painterResource(id = R.drawable.ic_8),
                        contentDescription = null,
                        Modifier

                            .padding(top = 8.dp, bottom = 4.dp)
                            .background(
                                color = Color.White,
                                shape = RoundedCornerShape(10.dp)
                            )
                            .padding(16.dp),

                        )
                    Text(
                        text = "More",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        modifier = Modifier.padding(top = 8.dp),
                        color = Color(android.graphics.Color.parseColor("#2E3D6D"))
                    )
                }


            }
        }
    }
}