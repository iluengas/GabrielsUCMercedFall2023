--NO EFFECT (DOUBLE TYPE POKEMON): Has no effect on pokemon type
    SELECT DISTINCT p2.p_name
    FROM pokemon p1, typeChart, pokemon p2
    WHERE p1.p_name == 'Emboar' AND
                p1.p_type1 = tc_type AND
                tc_effectiveness == 0 AND
                    (tc_type_against = p2.p_type1 OR
                        tc_type_against = p2.p_type2)

    UNION

    SELECT DISTINCT p2.p_name
        FROM pokemon p1, typeChart, pokemon p2
        WHERE p1.p_name == 'Emboar' AND
                    p1.p_type2 = tc_type AND
                    tc_effectiveness == 0 AND
                        (tc_type_against = p2.p_type1 OR
                            tc_type_against = p2.p_type2);