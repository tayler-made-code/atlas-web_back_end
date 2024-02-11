-- Assuming the table name is 'metal_bands' and it has columns 'band_name' and 'lifespan'
-- You should use attributes formed and split for computing the lifespan or the Glam Rock bands
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC;