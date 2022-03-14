import java.util.Observable;
import java.util.Observer;

public class ConflictComponent implements Observer {
    
    public ConflictComponent() {
        EventBus.subscribeTo(EventBus.EV_CONFLICT, this);
    }

    public void update(Observable o, Object arg) {
        // Announce a schedule conflict
        EventBus.announce(EventBus.EV_SHOW, "** Schedule Conflict! **");
    }
}