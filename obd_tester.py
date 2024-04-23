import obd
import logging
import csv
import time

data_counter = 1
obd.logger.setLevel(logging.DEBUG)
connection = obd.OBD(portstr="COM5", baudrate=38400)
print(f"Protocol: {connection.protocol_name()}" )

rpm_request = obd.commands.RPM
speed_request = obd.commands.SPEED
maf_request = obd.commands.MAF

filepath = "csv_output.csv"
# Usage of open for better handling of the file
with open(filepath, "a", newline="") as output_file:
    file_writer = csv.writer(output_file)
    # Writing the header if the file is empty
    if output_file.tell() == 0:
        header = ["Speed", "RPM", "MAF", "Duration [s]"]
        file_writer.writerow(header)
        print(f"Wrote header: {header}")
    try:
        while connection.status() == obd.OBDStatus.CAR_CONNECTED:
            start_time = time.time()
            speed_response = connection.query(speed_request)
            rpm_response = connection.query(rpm_request)
            maf_response = connection.query(maf_request)
            print("Engine RPM:", rpm_response.value)
            print("Speed:", speed_response.value)
            print("MAF:", maf_response.value)
            data_counter = data_counter + 1
            end_time = time.time()

            data = [
                speed_response.value,
                rpm_response.value,
                maf_response.value,
                float(end_time - start_time),
            ]

            file_writer.writerow(data)
    except KeyboardInterrupt:
        print("While-Loop interrupted by keyboard input ctrl+c.")

print("Left data collection loop. Amount of collected data: ", data_counter - 1)
connection.close()
