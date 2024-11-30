--1.database diagram
-- Write a query that will display the results below (Note: some columns might be renamed
-- but use the column names above). It should only show 2020 data and order by driver
-- points.


SELECT 
    driver_name,  
    driver_points, 
    race_year,  
    team_name  
FROM 
    drivers_table 
WHERE 
    race_year = 2020 
ORDER BY 
    driver_points DESC; 
