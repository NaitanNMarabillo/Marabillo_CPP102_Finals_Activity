
# Simulated Device Monitoring and Alert System

**Student Name:** Naitan N. Marabillo  
**Student Number:** 2600707  
**Section:** 1CPE-A

## 1. Project Description

This program simulates a device monitoring system by storing temperature readings in a Python list. It allows the user to view readings, add valid readings, classify temperatures, and generate a numerical summary. The program uses loops, functions, conditional statements, and input validation to process the readings and determine an overall status.

## 2. Features

- View all stored temperature readings.
- Add a new reading using a whole number from 0 to 100.
- Reject empty, non-numeric, negative, decimal, and out-of-range inputs.
- Classify readings as NORMAL, WARNING, or CRITICAL.
- Calculate the total, average, minimum, and maximum using loops.
- Display category counts and percentages.
- Determine an overall status.
- Keep displaying the menu until the user chooses Exit.

## 3. Requirements

- Python 3
- No external Python packages are required.
- The following files should be inside the `Week17` folder:
  - `device_monitor.py`
  - `README.md`
  - `test_cases.md`

## 4. How to Run

1. Open a terminal in the `Week17` folder.
2. Run the program using the following command:

   ```bash
   python device_monitor.py
   ```

3. On macOS or Linux, use:

   ```bash
   python3 device_monitor.py
   ```

4. Enter a menu number from 1 to 5.
5. Select option 5 to exit the program.

## 5. Sample Output

```text
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Readings
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 1

CURRENT READINGS
----------------
Reading 1 28 °C
Reading 2 31 °C
Reading 3 35 °C
Reading 4 37 °C
Reading 5 29 °C

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Readings
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice:
```

## 6. Known Limitations

- Readings are stored in memory only and are lost when the program closes.
- The program uses simulated temperature values; it does not connect to a real sensor or device.
- The allowed range and classification thresholds are for this classroom project, not real-world safety guidance.

## 7. Reflection

Through this project, I learned how to use lists, loops, functions, and conditional statements to create a simple device monitoring system. One of the challenging parts was understanding how to process the readings and classify them correctly, especially when handling boundary values such as 30°C and 35°C. I also learned the importance of input validation to prevent invalid readings from being added to the list. This project helped me improve my understanding of Python programming and showed me how different programming concepts can work together to solve a problem.
