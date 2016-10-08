package faith.stufinite.time2eat.time2eat;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button btnmenu=(Button)findViewById(R.id.btnmenu);
        btnmenu.setOnClickListener(new Button.OnClickListener(){
            public void onClick(View v){
                Intent it = new Intent();
                it.setClass(MainActivity.this,Menu.class);
                //2跳到3
                startActivity(it);
            }
        });
        EditText editText = findViewById(R.id.et);
        Button btnquest=(Button)findViewById(R.id.btnquest);
        btnquest.setOnClickListener(new Button.OnClickListener(){
            public void onClick(View v){
                Toast toast = Toast.makeText(MainActivity.this,
                        "這是查詢", Toast.LENGTH_LONG);
                toast.show();
            }
        });
    }
}
