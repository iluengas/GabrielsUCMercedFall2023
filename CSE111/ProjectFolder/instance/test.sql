SELECT DISTINCT tp_pokemon
 FROM trainers, trainer_to_pokemon, pokemon
    WHERE t_type == 'water' AND 
            t_name = tp_trainer AND
                tp_pokemon = p_name AND 
                        p_attack > 100;