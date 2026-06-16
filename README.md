US Net Metering Analysis 2015–2024

Analysis of U.S. commercial and residential solar adoption using EIA net metering data.

View the live dashboard here →


Show Image
(Replace this line with a screenshot of your dashboard)


Overview

This project explores how commercial solar capacity has grown across U.S. states from 2015 to 2024. Built as a portfolio project to demonstrate data analysis skills for roles in clean energy sales and market development.

Data Source


EIA Form 861 – Annual Electric Power Industry Report, Net Metering data (2015–2024)


Tools

ToolPurposePython (pandas)Combined 10 annual EIA files, fixed column mismatches, exported clean CSVTableau PublicDashboard and visualizations

Key Findings


Total U.S. net metering capacity reached 44,309 MW in 2024, up from ~10,000 MW in 2015
California accounts for the largest share of commercial solar capacity by a wide margin
Commercial solar has grown faster than residential since 2020
Massachusetts, New Jersey, and New York lead among non-California states


Files


combine_net_metering.py – script to combine annual EIA files and fix the 2015 column order mismatch
combined_net_metering.csv – cleaned dataset used in Tableau


Data Notes

Filtered to AC-type entries only. Adjustment rows excluded. 2015 through 2024 files combined into one table of approximately 11,000 rows.
