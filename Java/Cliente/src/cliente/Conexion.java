package cliente;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;

/**
 *
 * @author moramaz
 */
public class Conexion {
    
    private OkHttpClient webClient;
    private RequestBody rb;

    public Conexion() {
        this.webClient = new OkHttpClient();
    }
    
    public void L_Insertar(String dato){
        rb = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/insertintolist");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void M_Insertar(String dato){
        String[] separado = dato.split("@");
        RequestBody rb = new FormEncodingBuilder()
                .add("inicial", dato.charAt(0) + "")
                .add("dominio", separado[1])
                .add("nombre", separado[0])
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/insertintomatrix");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void C_Insertar(int dato){
        rb = new FormEncodingBuilder()
                .add("dato", dato + "")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/insertintoqueue");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void P_Insertar(String dato){
        rb = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/insertintostak");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
}