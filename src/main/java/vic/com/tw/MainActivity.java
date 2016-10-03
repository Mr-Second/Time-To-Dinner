package vic.com.tw;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

public class MainActivity extends Activity {
    Spinner spinner;
    ArrayAdapter<String> lunchList;
    String[] lunch = {"雞腿飯", "魯肉飯", "排骨飯", "水餃", "陽春麵"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btn=(Button)findViewById(R.id.btnlogin);
        btn.setOnClickListener(new Button.OnClickListener(){
            public void onClick(View v){
                Intent it = new Intent();
                it.setClass(MainActivity.this,login.class);
                startActivity(it);
            }
        });
        Button btn2=(Button)findViewById(R.id.btnsign);
        btn2.setOnClickListener(new Button.OnClickListener(){
            public void onClick(View v){
                Intent it = new Intent();
                it.setClass(MainActivity.this,sign.class);
                startActivity(it);
            }
        });
        spinner = (Spinner)findViewById(R.id.sp);
        lunchList = new ArrayAdapter<String>(MainActivity.this, android.R.layout.simple_spinner_item, lunch);
        spinner.setAdapter(lunchList);
    }
}
