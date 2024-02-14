-- selects max temperature for each state
SELECT city, MAX(value) AS max_temp FROM temperatures
GROUP BY city ORDER BY max_temp
