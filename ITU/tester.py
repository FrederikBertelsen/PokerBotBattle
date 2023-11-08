from math import sqrt

bet_size = 60
pot_size = 300
max_pot_size = 1000

risk = sqrt(
            (4 / 3.0) *
            ((bet_size * (2 * bet_size + pot_size)) /
             (max_pot_size * (bet_size + pot_size)))
        )

print(risk)
