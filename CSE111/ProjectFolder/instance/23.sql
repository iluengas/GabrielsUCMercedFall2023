SELECT p_name
FROM region, pokemon
WHERE r_gen = 3 AND 
        (r_box_1 == p_name OR 
            r_box_2 == p_name OR
                r_box_3 == p_name);
