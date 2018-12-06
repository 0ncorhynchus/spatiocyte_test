from ecell4 import *
from ecell4.spatiocyte import *

def main():
    radius, D = 5.0e-3, 1.0

    with species_attributes():
        A | {'radius': str(radius), 'D': str(D)}

    model = get_model()

    rng = GSLRandomNumberGenerator()
    rng.seed(1)

    w = SpatiocyteWorld(Real3(1.0, 1.0, 1.0), voxel_radius=radius, rng=rng)
    w.bind_to(model)

    coord = w.position2coordinate(Real3(0.5, 0.5, 0.5))
    ((pid, voxel), is_succeeded) = w.new_voxel(Species('A'), coord)

    # w.add_space(OfflatticeSpace)

    sim = SpatiocyteSimulator(w)
    obs = FixedIntervalTrajectoryObserver(0.01)

    sim.initialize()

    sim.run(10.0, obs)

    for pos in obs.data()[0]:
        x, _y, _z = tuple(pos)
        # assert(x > 0.25 and x < 0.75)

if __name__ == '__main__':
    main()
