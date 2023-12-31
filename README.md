# Description
I created this script to automate structural engineering design work back in 2019. This script imports a spreadsheet of a building's piled foundation coordinates from a Building Information Model and checks the centre-to-centre distances between all the piles. This allows us to quickly ensure that minimum clearance is fulfilled and non-compliances are picked up early. The minimum clearance required is usually between 2.5 to 3 times the average diameter of the two piles being checked. As it is quite common for a building to have more than a hundred piles, relying on the manual checking processes often result in non-compliances. The later these are discovered, the more costly it is to re-engineer the structure.

Input Required: Diameter Multiplier for horizontal clearance (Typically 2.5 or 3), Formatted Excel Spreadsheet

Output Expected: List of Non-compliances

## Workflow Diagram
![README_Diagram](https://github.com/jeraldhan92/pilespacechecker/assets/49491450/217a393c-81fa-490e-942d-75507e6e6cd2)

## Output
Values in "Limit" and "Actual" are in millimeters. You can also see that there was a duplicate modeling of a single pile in the same location with a return of 0mm horizontal distance.

![output](https://github.com/jeraldhan92/pilespacechecker/assets/49491450/f64ec1cd-c382-4034-b4d2-ea7c3d709411)

