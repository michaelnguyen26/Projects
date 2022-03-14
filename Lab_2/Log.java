import java.util.Observable;
import java.util.Observer;
import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

/* author : Michael Nguyen
* Helpful Resources: https://www.edureka.co/blog/logger-in-java
*/

// This class will observe the event for the ID @ EV_SHOW
public class Log implements Observer {
    
    // create a logger object for this class
    private final static Logger LOGGER = Logger.getLogger(Log.class.getName()); 

    /* Constructor to subscribe this object to the EV_SHOW event for outputs on the event bus and create
    * my FileHandler object to log events
    */
    public Log() {
        EventBus.subscribeTo(EventBus.EV_SHOW, this);

        try {
            FileHandler outputLog = new FileHandler("OutputLog.log"); // create a logging file
            LOGGER.setUseParentHandlers(false); // remove the output to the parent logger (console screen)

            SimpleFormatter textFormat = new SimpleFormatter(); // format logger so it is not in XML
            outputLog.setFormatter(textFormat); // apply the formatter
            LOGGER.addHandler(outputLog); // add a the file handler to the LOGGER to receive logging messages.
        
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    /* From the obserable class, when the EVENT BUS announces
    * a change, this update method will be invoked and add logging
    * infos to the logger object
    */

    public void update(Observable event, Object param) {
        LOGGER.log(Level.INFO, param.toString() + "\n");  // Log the output as an info and convert the passed param to a string
    }
}