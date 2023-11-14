--SUPER EFFECTIVE AGAINST(DOUBLE TYPE POKEMON): Double type advantage, CAN ONLY USE ON POKEMON WHERE p_type2 IS NOT NULL


    SELECT DISTINCT p2.p_name
    FROM pokemon p1, typeChart, pokemon p2
    WHERE p1.p_name == 'Emboar' AND
                p1.p_type1 = tc_type AND
                tc_effectiveness > 1 AND
                    (tc_type_against = p2.p_type1 OR
                        tc_type_against = p2.p_type2)

    INTERSECT

    SELECT DISTINCT p2.p_name
        FROM pokemon p1, typeChart, pokemon p2
        WHERE p1.p_name == 'Emboar' AND
                    p1.p_type2 = tc_type AND
                    tc_effectiveness > 1 AND
                        (tc_type_against = p2.p_type1 OR
                            tc_type_against = p2.p_type2);