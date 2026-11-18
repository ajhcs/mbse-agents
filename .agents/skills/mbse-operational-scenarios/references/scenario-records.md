# Scenario records

Use the project scenario format when available. Carry enough information to replay the path, including ID, purpose, source, actors, trigger, initial conditions and mode, actions and responses, exchanges, constraints, exception paths, final conditions, observations, and open decisions.

A scenario such as a communication outage should distinguish detection, operator notification, the functions still available, safe or degraded operation, and restoration. Recovery is not complete just because a connection reappears: stale commands, synchronization, authorization, and resumption can change the result.

When using a sequence diagram, check that the exchanged items and timeouts agree with the scenario. In a state model, check the guard and responsible actor at each consequential transition. Render a diagram at the size intended for review and trace a representative path through the labels and arrows.

For a scenario set, identify which actors, environments, modes, outcomes, and critical exceptions were covered. Use unexamined consequential paths to guide further elicitation.
