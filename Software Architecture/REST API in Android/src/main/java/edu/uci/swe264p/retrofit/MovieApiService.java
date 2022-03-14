package edu.uci.swe264p.retrofit;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface MovieApiService {
    @GET("movie/{id}")
    Call<Movie> getMovie(@Path("id") int id, @Query("api_key") String apiKey);

    @GET("movie/top_rated") // REST resource --> the result is a large complex JSON type object of an array list
    // Reference: https://api.themoviedb.org/3/movie/top_rated?api_key=18d116f1f3ca3dc2e7970df2074c6d92
    Call<TopRatedResponse> getListOfTopMovies(@Query("api_key") String apiKey);
}