--NOT VERY EFFECTIVE AGAINST (DOUBLE TYPE POKEMON): Single Type disadvantage


    SELECT DISTINCT p2.p_name
    FROM pokemon p1, typeChart t1, typeChart t2, pokemon p2
    WHERE p1.p_name == 'Emboar' AND
                p1.p_type1 = t1.tc_type AND
                    p1.p_type2 = t2.tc_type AND
                        t1.tc_effectiveness < 1 AND
                        t2.tc_effectiveness < 1 AND 
                        (t1.tc_type_against = p2.p_type1 OR
                            t1.tc_type_against = p2.p_type2 OR
                                t2.tc_type_against = p2.p_type1 OR
                                    t2.tc_type_against = p2.p_type2);