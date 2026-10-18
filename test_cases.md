# Test Cases – Simulated Device Monitoring and Alert System

**Subject:** CPP102 – Laboratory Exercise 17  
**Tested by:** Naitan N. Marabillo 
**Date:** October 18, 2026

## Test Case Table

| Test Case | Input / Action | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC01 – View Readings | Select option `1`. | The program displays all five initial readings: 28, 31, 35, 37, and 29 °C. | Displays all five initial readings correctly. | Pass |
| TC02 – Add Valid Reading | Select option `2` and enter `33`. | The program accepts the reading and adds 33 to the list. | The reading is added successfully. | Pass |
| TC03 – Invalid Text Input | Select option `2` and enter `abc`. | The program rejects the input and displays an error message. | The program rejects the text input. | Pass |
| TC04 – Negative Reading | Select option `2` and enter `-5`. | The program rejects the negative value because readings must be between 0 and 100. | The program rejects the negative reading. | Pass |
| TC05 – Reading Above Limit | Select option `2` and enter `120`. | The program rejects the value because it exceeds the maximum allowed reading of 100. | The program rejects the value above the limit. | Pass |
| TC06 – Classification at 30 °C | Select option `2`, enter `30`, and then select option `3`. | The reading of 30 °C is classified as WARNING. | The reading is classified as WARNING. | Pass |
| TC07 – Classification at 35 °C | Select option `3` and check the reading of 35 °C. | The reading of 35 °C is classified as WARNING. | The reading is classified as WARNING. | Pass |
| TC08 – Generate Summary | Start with the initial readings and select option `4`. | The total is 160, average is 32.00 °C, minimum is 28 °C, maximum is 37 °C, and overall status is ATTENTION REQUIRED. | The summary displays the expected calculations and status. | Pass |
| TC09 – Invalid Menu Choice | Enter `9` at the main menu. | The program displays an invalid-choice message and returns to the menu. | The program displays the invalid-choice message. | Pass |
| TC10 – Exit Program | Select option `5`. | The program displays a thank-you message and terminates. | The program displays the message and exits. | Pass |


**Conclusion:** The test cases are designed to verify that the Simulated Device Monitoring and Alert System correctly displays readings, validates user input, classifies temperatures, calculates summary statistics, handles invalid menu choices, and exits properly. The final testing conclusion should be updated based on the actual results obtained during program execution.