package com.brickforge.theme;

import android.app.Activity;
import android.os.Bundle;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.content.Intent;
import android.net.Uri;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

public class MainActivity extends Activity {
    private int dp(float value) { return (int)(value * getResources().getDisplayMetrics().density + .5f); }
    private GradientDrawable bg(int color, int radius) {
        GradientDrawable drawable = new GradientDrawable();
        drawable.setColor(color); drawable.setCornerRadius(dp(radius)); return drawable;
    }
    private TextView text(String value, int size, int color, boolean bold) {
        TextView t = new TextView(this); t.setText(value); t.setTextSize(size); t.setTextColor(color);
        t.setPadding(dp(8),dp(10),dp(8),dp(10));
        if (bold) t.setTypeface(Typeface.DEFAULT, Typeface.BOLD); return t;
    }
    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        getWindow().setStatusBarColor(Color.rgb(12,15,21));
        getWindow().setNavigationBarColor(Color.rgb(12,15,21));
        ScrollView scroll = new ScrollView(this);
        scroll.setBackgroundColor(Color.rgb(12,15,21));
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(dp(20),dp(26),dp(20),dp(32));
        scroll.addView(root);
        root.addView(text("BRICKFORGE",32,Color.WHITE,true));
        root.addView(text("Build your world, one brick at a time.",16,0xffcbd5e1,false));
        TextView heading = text("Icon pack preview",23,Color.WHITE,true);
        root.addView(heading);
        int[] colors = {0xff854bd3,0xff1673d1,0xffe8a61d,0xffe34e91,0xff119da9,0xff1f9a63};
        String[] names = {"Apps","Tasks","Photos","Social","Shopping","Maps"};
        for (int row=0;row<2;row++) {
            LinearLayout strip = new LinearLayout(this);
            strip.setOrientation(LinearLayout.HORIZONTAL);
            for (int i=0;i<3;i++) {
                int index=row*3+i;
                LinearLayout tile=new LinearLayout(this);
                tile.setOrientation(LinearLayout.VERTICAL); tile.setGravity(Gravity.CENTER);
                tile.setPadding(dp(5),dp(8),dp(5),dp(8));
                LinearLayout.LayoutParams lp=new LinearLayout.LayoutParams(0,dp(135),1);
                lp.setMargins(dp(3),dp(4),dp(3),dp(4));
                tile.setBackground(bg(colors[index],20));
                TextView studs=text("●    ●",22,0x99ffffff,true);
                studs.setGravity(Gravity.CENTER); tile.addView(studs);
                TextView symbol=text(new String[]{"▣","☑","▣","✦","▤","◆"}[index],39,Color.WHITE,true);
                symbol.setGravity(Gravity.CENTER);tile.addView(symbol);
                TextView name=text(names[index],12,Color.WHITE,true);
                name.setGravity(Gravity.CENTER);tile.addView(name);
                strip.addView(tile,lp);
            }
            root.addView(strip);
        }
        root.addView(text("Starter preview only — full photorealistic icon artwork is not yet installed.",13,0xffffd166,false));
        root.addView(text("Apply your icon pack",23,Color.WHITE,true));
        root.addView(text("On compatible Samsung devices: Good Lock → Theme Park → Icon → import a third-party icon pack. Support varies by One UI version.",15,0xffcbd5e1,false));
        Button help=new Button(this);help.setText("Open Samsung Good Lock information");
        help.setOnClickListener(v -> startActivity(new Intent(Intent.ACTION_VIEW,Uri.parse("https://galaxystore.samsung.com/detail/com.samsung.android.goodlock"))));
        root.addView(help);
        root.addView(text("Compatibility: this APK cannot directly replace every installed app icon. More mappings, high-resolution assets, widgets and wallpapers are planned.",14,0xffcbd5e1,false));
        setContentView(scroll);
    }
}
