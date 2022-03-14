import java.io.FileWriter;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

/******************************************************************************************************************
 * File:MiddleFilter.java
 * Project: Lab 1
 * Copyright:
 * Copyright (c) 2020 University of California, Irvine
 * Copyright (c) 2003 Carnegie Mellon University
 * Versions:
 * 1.1 January 2020 - Revision for SWE 264P: Distributed Software Architecture,
 * Winter 2020, UC Irvine.
 * 1.0 November 2008 - Sample Pipe and Filter code (ajl).
 *
 * Description:
 * This class serves as an example for how to use the FilterRemplate to create a
 * standard filter. This particular
 * example is a simple "pass-through" filter that reads data from the filter's
 * input port and writes data out the
 * filter's output port.
 * Parameters: None
 * Internal Methods: None
 ******************************************************************************************************************/

public class MiddleFilter extends FilterFramework {

	
	public void buildWP(List<List<String>> data) { // This method is used to build the CSV file at the end of the run

		try {
			FileWriter csvWriter = new FileWriter("./WildPoints.csv"); // make filename
			csvWriter.append("Time"); // headings
			csvWriter.append(","); // next cell
			csvWriter.append("Velocity");  // headings
			csvWriter.append(","); // next cell
			csvWriter.append("Altitude");  // headings
			csvWriter.append(","); // next cell
			csvWriter.append("Pressure");  // headings
			csvWriter.append(",");// next cell
			csvWriter.append("Temperature");  // headings
			csvWriter.append("\n"); // new row

			for (List<String> rowData : data) { // for each row append the data
				csvWriter.append(String.join(",", rowData));
				csvWriter.append("\n"); // new row
			}

			csvWriter.close();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}


	public void run() {
		int bytesread = 0; // Number of bytes read from the input file.
		int byteswritten = 0; // Number of bytes written to the stream.
		byte databyte = 0; // The byte of data read from the file

		int id;
		int IdLength = 4;
		int i;
		long measurement;
		int MeasurementLength = 8;
		
		Double altitude2 = 0.0;
		Double altitude1 = 0.0;
		Double actual = 0.0;

		double getVelocity = 0.0; // create varaible of type double to get the velocity
		double getAltitude = 0.0;
		double getPressure = 0.0; // create varaible of type double to get the pressure
		double getTemperature = 0.0; // create varaible of type double to get the temperature
		
		boolean aWildAltitude = false; // if I get a wild value "flag" this as true
		int frames = 0;

		// rows to hold the data
		List<List<String>> row_data = new ArrayList<>(); 


		// Next we write a message to the terminal to let the world know we are alive...
		System.out.print("\n" + this.getName() + "::Middle Reading ");
		Calendar TimeStamp = Calendar.getInstance();
		SimpleDateFormat TimeStampFormat = new SimpleDateFormat("yyyy:dd:hh:mm:ss");

		// NOTES from TA Meeting:
		// compare current altitude with altitude2 and if the variation is > 100 feet, replace the value with the average of alt1 and alt2
		// only modify current frame

		while (true) {
			try{
				// First four bytes read the Integer ID
				id = 0;
				for (i = 0; i < IdLength; i++) {
					databyte = ReadFilterInputPort(); // This is where we read the byte from the stream...
					id = id | (databyte & 0xFF); // We append the byte on to ID...
					if (i != IdLength - 1) // If this is not the last byte, then slide the
					{ // previously appended byte to the left by one byte
						id = id << 8; // to make room for the next byte we append to the ID
					}
					bytesread++; // Increment the byte count
				}

				// Next 8 Bytes reads the Measurement Data
				measurement = 0;
				for (i = 0; i < MeasurementLength; i++) {
					databyte = ReadFilterInputPort();
					measurement = measurement | (databyte & 0xFF); // We append the byte on to measurement...
					if (i != MeasurementLength - 1) // If this is not the last byte, then slide the
					{ // previously appended byte to the left by one byte
						measurement = measurement << 8; // to make room for the next byte we append to the
														// measurement
					}
					bytesread++; // Increment the byte count
				}

				// Implemented Functionality
				if (id == 0) {
					TimeStamp.setTimeInMillis(measurement); // id of 0 is time (reference chart)
				
				} else if (id == 1) {
					getVelocity = Double.longBitsToDouble(measurement); // id of 1 is velocity (reference chart)
				}

				// process measurement
				else if (id == 2) {

					altitude2 = altitude1; 
					altitude1 = actual; 	
					actual = Double.longBitsToDouble(measurement); 


					// System.out.println("Actual: " + actual +  "\n");
					// System.out.println("Altitude 1: " + altitude1);

					frames++;
					if(frames == 2){ // must be two since I am comparing the first two frames in the beginning 
						if(Math.abs(actual - altitude1) > 100){
							getAltitude = actual; // keep original first for WildPoints.csv
							actual = altitude1; // REPLACEMENT
							aWildAltitude = true;
						}
					}

					else if (Math.abs(actual - altitude1) > 100 && frames > 2){ // frame must be > 2 to check the previous two frames
						getAltitude = actual; // keep original first for WildPoints.csv
						actual = ((altitude1 + altitude2))/2; // average of the previous two altitudes (REPLACEMENT)
						aWildAltitude = true;
					}

					if(aWildAltitude){ // if a wild point
						ByteBuffer toID = ByteBuffer.allocate(4); // allocate 4 bytes for integer
						toID.putInt(6); // id 6 will indicate that a wild altitude is encountered
						for (i = 0; i < IdLength; i++) {
							WriteFilterOutputPort(toID.get(i)); // do the same thing as the original middle filter to write data to the output source
						
							byteswritten++; // increase bytes written orignally
						}	

						ByteBuffer wildPoint = ByteBuffer.allocate(8); // alocated 8 bytes for the measurement value
						wildPoint.putDouble(actual); // put the replacement value
						for (i = 0; i < MeasurementLength; i++) {
							WriteFilterOutputPort(wildPoint.get(i)); // do the same thing as the original middle filter to write data to the output source
						
							byteswritten++; // increase bytes written orignally
						}	
						continue; // continue the next iteration so ID and measurement are correctly sent to the sink filter
					}
	
										
				}else if (id == 3) {
					getPressure = Double.longBitsToDouble(measurement); // id of 3 is pressure (reference chart)
					
				} else if (id == 4) {
					getTemperature = Double.longBitsToDouble(measurement); // id of 4 is temp (reference chart)			

					if(aWildAltitude){ // save a csv file that only contains wild altitude data

						List<String> curr_data = new ArrayList<>(); // new list (row) for each iteration
		
						curr_data.add(TimeStampFormat.format(TimeStamp.getTime()));
						curr_data.add(String.format("%.5f", getVelocity)); // convert to string and format to 5 sig figs
						curr_data.add(String.format("%.5f", getAltitude)); // convert to string and format to 5 sig figs
						curr_data.add(String.format("%.5f", getPressure)); // convert to string and format to 5 sig figs
						curr_data.add(String.format("%.5f", getTemperature)); // convert to string and format to 5 sig figs
						
						row_data.add(curr_data); // this adds the row of data to the List<List> where <List> is the row of data
						aWildAltitude = false;
					}
					
				}	
				
				// Write Measurements and ID to Sink Filter without Wild Points	

				ByteBuffer toID = ByteBuffer.allocate(4); // allocate 4 bits for integer
				toID.putInt(id);
				for (i = 0; i < IdLength; i++) {
				WriteFilterOutputPort(toID.get(i)); // do the same thing as the original middle filter to write data to the output source
			
				byteswritten++; // increase bytes written orignally
				}	

				ByteBuffer toMMMT = ByteBuffer.allocate(8); // allocate 8 bits for double
				toMMMT.putDouble(Double.longBitsToDouble(measurement));
				for (int j = 0; j < MeasurementLength; j++) {
				WriteFilterOutputPort(toMMMT.get(j)); // do the same thing as the original middle filter to write data to the output source
			
				byteswritten++; // increase bytes written orignally
				}
				
				
			} catch (EndOfStreamException e) {
				ClosePorts();
				System.out.print("\n" + this.getName() + "::Middle Exiting; bytes read: " +
						bytesread
						+ " bytes written: " + byteswritten);
				break;
					
			}
		}// while

		buildWP(row_data);
		
	}// run
}