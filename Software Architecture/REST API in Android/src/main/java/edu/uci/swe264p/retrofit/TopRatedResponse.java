package edu.uci.swe264p.retrofit;

import java.util.List;
import com.google.gson.JsonObject;
import com.google.gson.annotations.SerializedName;

// Resources:
// https://stackoverflow.com/questions/28957285/what-is-the-basic-purpose-of-serializedname-annotation-in-android-using-gson


public class TopRatedResponse {
    // @SerializedName("results") --> don't need since my list name matches the api's response "results"
    // Reference: https://api.themoviedb.org/3/movie/top_rated?api_key=18d116f1f3ca3dc2e7970df2074c6d92
    private List<JsonObject> results;

    public TopRatedResponse(List<JsonObject> list_of_results) {
        this.results = list_of_results;
    }

    // Getter for private variable "results"
    public List<JsonObject> getListOfMovies() {
        return results;
    }
}