package PythonConexion;

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
public class PythonConexion {
    
    private final OkHttpClient webClient;
    private RequestBody rb;

    public PythonConexion() {
        this.webClient = new OkHttpClient();
    }
    
    public void list_add(String dato){
        rb = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/list_add");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void matrix_add(String dato){
        String[] separado = dato.split("@");
        RequestBody rb = new FormEncodingBuilder()
                .add("inicial", dato.charAt(0) + "")
                .add("dominio", separado[1])
                .add("nombre", separado[0])
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/matrix_add");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void queue_add(int dato){
        rb = new FormEncodingBuilder()
                .add("dato", dato + "")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/queue_add");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void stak_add(int dato){
        rb = new FormEncodingBuilder()
                .add("dato", dato + "")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/stak_add");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void list_remove(int indice){
        rb = new FormEncodingBuilder()
                .add("dato", indice + "")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/list_remove");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public void matrix_remove(String dato){
        String[] separado = dato.split("@");
        RequestBody rb = new FormEncodingBuilder()
                .add("inicial", dato.charAt(0) + "")
                .add("dominio", separado[1])
                .add("nombre", separado[0])
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/matrix_remove");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    public String queue_remove(){
        rb = new FormEncodingBuilder()
                .add("dato", "")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/queue_remove");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            return response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
        return null;
    }
    
    public String stak_remove(){
        rb = new FormEncodingBuilder()
                .add("dato", "")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/stak_remove");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            return response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
        return null;
    }
    
    public String list_search(int indice){
        rb = new FormEncodingBuilder()
                .add("indice", indice + "")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/list_search");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            return response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
        return null;
    }
    
    public String matrix_search_letter(String dato){
        RequestBody rb = new FormEncodingBuilder()
                .add("inicial", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/matrix_search_letter");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            return response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
        return null;
    }
    
    public String matrix_search_domain(String dato){
        RequestBody rb = new FormEncodingBuilder()
                .add("dominio", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/matrix_search_domain");
            Request request = new Request.Builder().url(url).post(rb).build();
            Response response = webClient.newCall(request).execute();
            return response.body().string();
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
        return null;
    }    
}