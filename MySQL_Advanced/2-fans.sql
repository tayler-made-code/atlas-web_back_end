-- Assuming the table name is 'metal_bands'
-- and it has columns 'origin' and 'nb_fans'
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;