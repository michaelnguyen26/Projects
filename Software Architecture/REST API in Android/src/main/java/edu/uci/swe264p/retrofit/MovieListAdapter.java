package edu.uci.swe264p.retrofit;

import androidx.recyclerview.widget.RecyclerView;
import com.squareup.picasso.Picasso;

import java.util.List;

import android.view.LayoutInflater;
import android.widget.ImageView;
import android.widget.TextView;
import android.view.ViewGroup;
import android.view.View;


public class MovieListAdapter extends RecyclerView.Adapter<MovieListAdapter.ViewHolder>{

    private List<String> image;
    private List<String> title;
    private List<String> date;
    private List<String> vote;
    private List<String> overview;

    // Constructor
    public MovieListAdapter(List<String> image_data, List<String> title_data,
                            List<String> date_data, List<String> vote_data, List<String> overview_data) {
        this.image = image_data;
        this.title = title_data;
        this.date = date_data;
        this.vote = vote_data;
        this.overview = overview_data;
    }



    private static final String pathToImage = "https://image.tmdb.org/t/p/w500/";

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView textTitle;
        TextView textOverview;
        TextView textVote;
        TextView textDate;

        ImageView image_view;

        ViewHolder(View itemView) {
            super(itemView);

            // Assign values to the layout in ivMovie (movie_row.xml)
            image_view = itemView.findViewById(R.id.ivMovie);
            textOverview = itemView.findViewById(R.id.tvOverview);
            textTitle = itemView.findViewById(R.id.tvTitle);
            textDate = itemView.findViewById(R.id.tvReleaseDate);
            textVote = itemView.findViewById(R.id.tvVote);


        }
    }

    // ProgramListAdapter.java implementation

    @Override
    public MovieListAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.movie_row, parent, false);
        return new MovieListAdapter.ViewHolder(view);
    }

    @Override
    public int getItemCount() {
        return title.size();
    }

    @Override
    public void onBindViewHolder(MovieListAdapter.ViewHolder holder, int position) {
        String image_url = pathToImage + image.get(position);

        Picasso.get().load(image_url).into(holder.image_view); // Load image from picasso

        // IMPORTANT: Add data to the layout here
        holder.textOverview.setText(overview.get(position));
        holder.textVote.setText(vote.get(position));

        holder.textTitle.setText(title.get(position));
        holder.textDate.setText(date.get(position));

    }
    // End of ProgramListAdapter.java implementation
}