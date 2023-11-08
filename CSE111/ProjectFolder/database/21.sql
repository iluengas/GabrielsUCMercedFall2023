SELECT t_name, t_type
from pokemon, typeChart, trainers
WHERE p_name = 'Bulbasaur' AND
        p_type1 = tc_type AND 
            tc_effectiveness > 1 AND 
                tc_type_against = t_type AND 
                    p_gen = t_gen;
