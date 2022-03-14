import java.util.ArrayList;
import java.util.Observable;
import java.util.Observer;

public final class CourseConflictHandler implements Observer{

    // boolean to check if a scheduling conflict occurs
    static boolean isASchedulingConflict;

    public CourseConflictHandler(){
        EventBus.subscribeTo(EventBus.EV_CHECK_FOR_CONFLICT, this);
    }

    // Part C:

    /* Receive objStudent and objCourse from the RegisterStudentHandler to check if there is a 
    *  schedule conflict 
    */

    public void update(Observable event, Object param) {
        ArrayList vCourse = RegisterStudentHandler.objStudent.getRegisteredCourses();

        for (int i=0; i<vCourse.size(); i++) {
            // course class contains the conflicts method --> check if it is true or false
            isASchedulingConflict = (((Course) vCourse.get(i)).conflicts(RegisterStudentHandler.objCourse)) ? true: false; 
        }
        if (isASchedulingConflict){
            RegisterStudentHandler.isAConflict = true; // let RegisterStudentHandler know to NOT register the student
            isASchedulingConflict = false; // reset flag or infinite scheduling conflict will occur
            EventBus.announce(EventBus.EV_CONFLICT, null);
        }
    }   

    // END OF PART C 
}