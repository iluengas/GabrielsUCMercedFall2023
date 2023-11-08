--Select all pokemon with a given ability
SELECT DISTINCT pa_pokemon
FROM abilities, pokemon_to_abilities
WHERE a_name = 'Overgrow' AND 
        (a_name = pa_ability1 OR 
            a_name = pa_ability2 OR 
                a_name = pa_hidden_ability); 

--Select all trainers in a region that have a type weakness against your pokemon
SELECT t_name, t_type
from pokemon, typeChart, trainers
WHERE p_name = 'Bulbasaur' AND
        p_type1 = tc_type AND 
            tc_effectiveness > 1 AND 
                tc_type_against = t_type AND 
                    p_gen = t_gen;

--Select all pokemon belonging to a specific trainer
SELECT DISTINCT t1.tp_pokemon
FROM trainer_to_pokemon t1
WHERE t1.tp_trainer == 'Blaine';

-- Select all box legendaries from a gen
SELECT p_name
FROM region, pokemon
WHERE r_gen = 3 AND 
        (r_box_1 == p_name OR 
            r_box_2 == p_name OR
                r_box_3 == p_name);





