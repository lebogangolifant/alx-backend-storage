-- List bands with Glam rock as their main style 
-- ranked by longevity
SELECT DISTINCT `band_name`,
                IFNULL(`split`, 2020) - `formed` as `lifespan`
    FROM `metal_bands` WHERE FIND_IN_SET('Glam rock', style)
    ORDER BY `lifespan` DESC;
