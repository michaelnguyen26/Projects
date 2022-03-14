package edu.uci.swe264p.retrofit;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class MovieListActivity extends AppCompatActivity {

    // MainActivity.java implementation

    private RecyclerView recyclerView;

    final static String TAG = MovieListActivity.class.getSimpleName();
    final static String BASE_URL = "https://api.themoviedb.org/3/";
    static Retrofit retrofit = null;
    final static String API_KEY = "18d116f1f3ca3dc2e7970df2074c6d92"; // my generated api key

    // Lists to store the values from onResponse()
    static List<String> valueOfTitles = new ArrayList<>();
    static List<String> valueOfImage = new ArrayList<>();
    static List<String> valueOfVote = new ArrayList<>();
    static List<String> valueOfRelease = new ArrayList<>();
    static List<String> valueOfOverview = new ArrayList<>();

    public MovieListActivity recyclerObject = this; // need this object to be passed to the recycler

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_movie_list); // set the content view to be the movie_list button

        // Creates the retrofit object and adds items to the RecyclerView
        connect();
    }

    private void connect() {
        if (retrofit == null) { // build my retrofit object
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
        }
        // Create an implementation of the API endpoints defined by the service interface in MovieApiService.class
        MovieApiService movieApiService = retrofit.create(MovieApiService.class);

        // Returns a Call<TopRatedResponse> from the REST API endpoint at getListOfTopMovies() --> list
        Call<TopRatedResponse> topMovies = movieApiService.getListOfTopMovies(API_KEY); // call my new API endpoint

        // Enqueue the top movies asynchronously (Android does NOT allow synchronous calls)
        topMovies.enqueue(new Callback<TopRatedResponse>() {
            @Override
            public void onResponse(Call<TopRatedResponse> topMovies, Response<TopRatedResponse> getApiResponse) {

                // get list of values from TopRatedResponse list
                for(JsonObject value : getApiResponse.body().getListOfMovies()){
                    valueOfTitles.add(value.get("title").toString());
                    valueOfRelease.add(value.get("release_date").toString());
                    valueOfVote.add(value.get("vote_average").toString());
                    valueOfOverview.add(value.get("overview").toString());

                    // NOTE: getAsString() is used here to get the actual element property as a string
                    valueOfImage.add(value.get("poster_path").getAsString());
                }

                // ProgramListActivity.java implementation

                /* RecyclerView Notes:
                https://developer.android.com/guide/topics/ui/layout/recyclerview?gclid=EAIaIQobChMIwIy5vrSU9gIVhyCtBh2clQgXEAAYASAAEgIMB_D_BwE&gclsrc=aw.ds

                    RecyclerView makes it easy to efficiently display large sets of data. You supply the data and define
                    how each item looks, and the RecyclerView library dynamically creates the elements when they're needed.
                    As the name implies, RecyclerView recycles those individual elements. When an item scrolls off the screen,
                    RecyclerView doesn't destroy its view. Instead, RecyclerView reuses the view for new items that have
                    scrolled onscreen.

                */

                recyclerView  = findViewById(R.id.rvMovieList);
                recyclerView.setHasFixedSize(true);
                recyclerView.setLayoutManager(new LinearLayoutManager(recyclerObject));
                recyclerView.setAdapter(new MovieListAdapter(valueOfImage, valueOfTitles, valueOfRelease, valueOfVote, valueOfOverview));

                // END of ProgramListActivity.java implementation
            }

            @Override
            public void onFailure(Call<TopRatedResponse> call, Throwable throwable) {
                Log.e(TAG, throwable.toString());
            }
        });

    }
    // END of MainActivity.java implementation
}