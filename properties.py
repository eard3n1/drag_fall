class Properties:
    def __init__(
                self, ground, x, y, mass,
                acceleration, velocity, apply_force, 
                ground_absorption, wind_resistance
                ):
        self.ground = ground
        self.y = y
        self.x = x

        self.mass = mass
        self.acceleration = acceleration
        self.velocity = velocity
        self.apply_force = apply_force
        self.ground_absorption = ground_absorption
        self.wind_resistance = wind_resistance

    def apply_upward_force(self):
        self.velocity += -self.apply_force / self.mass

    def apply_downward_force(self):
        self.velocity += self.apply_force / self.mass

    def advance(self, dt):
        self.velocity += self.acceleration * dt # gravity

        drag_acceleration = (-self.wind_resistance * self.velocity * abs(self.velocity)) / self.mass
        self.velocity += drag_acceleration * dt # wind resistance

        self.y += self.velocity * dt * 60

        if self.y >= self.ground:
            self.y = self.ground
            self.velocity *= -self.ground_absorption

        if abs(self.velocity) < 0.1:
            self.velocity = 0