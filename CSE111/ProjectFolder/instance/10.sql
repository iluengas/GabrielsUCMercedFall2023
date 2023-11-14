-- SELECT ALL EVOLUTION STAGES FROM A GIVEN POKEMON

SELECT p2.p_name
FROM pokemon p1, pokemon p2 
WHERE p1.p_name = 'Eevee' AND 
        p1.p_evo_species = p2.p_evo_species;


