# crm_talktime_automation
Python-based automation for daily CRM counselor talk-time reporting using Pandas and Excel.

**1. Project Introduction**

The Python-Based Call Talktime Report Automation project is a data processing and reporting solution designed to simplify daily counsellor calling performance analysis.

In admission operations, counsellors make calls to prospective students, and their calling data is exported from the calling system into Excel or CSV files. This data contains information such as agent names, call status, talktime, customer-connected duration, and call dispositions.

The purpose of this project is to automate the processing of this raw calling data and generate a consolidated, agent-wise performance report using Python and Pandas.

The project focuses on improving reporting efficiency, reducing repetitive manual work, and making calling performance data easier to analyse.

**2. Problem Statement**

The existing manual reporting process involves several time-consuming activities:

Manual data selection: Selecting and filtering individual records from daily calling reports requires repetitive effort.

Connected talktime calculation: Identifying the relevant connected-call records and calculating their talktime separately can be tedious and prone to errors.

Disposition-based classification: Call dispositions must be interpreted according to predefined business rules to identify connected and non-connected calls correctly.

Daily reporting workload: Processing reports every day consumes time that could otherwise be spent on analysis and operational improvement.

Monthly reporting challenges: Maintaining a consolidated sheet covering an entire month requires repeatedly handling daily reports, updating records, and checking calculations.

Reporting consistency: Manual calculations and filtering can lead to inconsistencies, particularly when large volumes of calling data are involved.

These challenges create an opportunity to automate repetitive calculations and standardise the reporting process.

**3. Project Objectives**

The main objectives are:

Automate the calculation of key calling performance metrics.

Reduce manual filtering and repetitive Excel operations.

Apply predefined disposition mapping rules consistently.

Generate a structured, agent-wise performance summary.

Simplify daily report preparation and support consolidated reporting.

Improve the efficiency and reliability of operational data analysis.

**4. Proposed Solution**

To address these challenges, I developed a Python-based solution using Pandas to process calling data and calculate performance metrics automatically.

The solution uses a predefined disposition mapping to determine whether a call should be classified as connected or non-connected. It then processes the available calling records, calculates the relevant metrics, and consolidates the results agent-wise.

The report can include the following metrics:

Total Calls

Total Talktime

Connected Talktime

Connected Calls

The approach replaces repetitive manual calculations with a consistent, reusable process. The same workflow can be used for daily reports, while monthly consolidation depends on combining or processing the relevant daily data together.

**5. Workflow**

Input: Export the calling data into an Excel or CSV file.

Data Processing: Read the input data using Python and Pandas.

Disposition Mapping: Apply the predefined mapping rules to classify call records.

Metric Calculation: Calculate total calls, total talktime, connected talktime, and connected calls.

Agent-Wise Consolidation: Group the processed data by agent and summarise the results.

Output: Generate a structured report for operational monitoring and performance analysis.

**6. Key Performance Metrics**

Total Calls: Total number of call records counted for each agent

Total Talktime: Aggregate calling time, including wait, talk, and disposition time, according to the reporting logic

Connected Talktime: Aggregate customer-connected talktime based on the source data

Connected Calls: Number of call records classified as connected according to the disposition mapping

The exact calculation depends on the source report's column definitions and the mapping rules configured in the code.

**7. Tools and Technologies Used**

Python: Core programming language used to automate the reporting workflow.

Pandas: Used for reading, filtering, transforming, grouping, and summarising calling data.

Excel/CSV: Used as the input data format and for reviewing structured reports.

Google Colab: Used as the development and execution environment.

GitHub: Used for source-code storage, version control, and project documentation.

**8. Skills Demonstrated**

Data Cleaning and Data Processing

Data Aggregation and Grouping

Business Rule Implementation

Disposition Mapping

Reporting Automation

Operational Data Analysis

Python Programming

Pandas Data Manipulation

Excel/CSV Data Handling

Problem-Solving and Process Improvement

GitHub-Based Project Documentation

**9. Business Value**

This project demonstrates how programming can be applied to solve a practical operational reporting problem.

By automating repetitive calculations and standardising disposition-based classification, the solution can reduce manual reporting effort, improve consistency, and make agent-wise performance information easier to prepare and review.

It also establishes a reusable foundation for more advanced reporting, such as monthly performance summaries, trend analysis, and dashboards.

**10. Future Scope**

Potential enhancements include:

Automated monthly consolidation of daily calling reports.

Interactive dashboards for performance monitoring.

Agent-wise and day-wise trend analysis.

Automated report generation and export.

Scheduled processing of new calling data.

Integration with additional reporting systems.

**11. Conclusion**

The Python-Based Call Talktime Report Automation project applies data analytics and process automation to a real-world reporting challenge.

It combines business understanding with Python-based data processing to transform raw calling records into meaningful performance metrics. The project demonstrates my practical learning in Python, Pandas, reporting automation, and operational data analysis.
