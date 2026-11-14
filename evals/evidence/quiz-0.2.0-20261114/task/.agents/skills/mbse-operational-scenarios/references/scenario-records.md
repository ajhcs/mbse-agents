# Scenario records

Optional record: ID and title; purpose; source; actors; trigger; initial conditions and mode; action/response sequence; exchanges; timing or resource constraints; exception paths; final conditions; evaluation observations; assumptions and open decisions.

A scenario such as a communication outage should distinguish detection, operator notification, the functions still available, safe or degraded operation, and restoration. Recovery is not complete just because a connection reappears: stale commands, synchronization, authorization, and resumption can change the result.

When using a sequence diagram, name exchanged items and identify timeouts. When using a state model, define the transition guard and responsible actor. Neither notation replaces missing scenario facts.

For a set, summarize coverage by actor, environment, mode, outcome, and critical exception. Use gaps to guide further elicitation, rather than claiming exhaustive coverage.
