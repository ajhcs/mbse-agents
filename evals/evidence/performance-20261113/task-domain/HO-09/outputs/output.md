# District drinking-water service — concept decision draft

**Preserve reliable drinking-water service as the objective. Investigate outage buffering and maintenance isolation before choosing a larger plant.** The stated failure is loss of service while the only treatment plant is maintained. Extra production capacity alone does not remove that dependence. The sponsor's preference for low unit production cost is legitimate, but it is not evidence that the preferred plant will keep water available during its own shutdown.

This comparison uses only `../request.md`. No demand volumes, outage durations, water-quality results, costs, spare capacity or staffing productivity are supplied. The recommendation is provisional; it is a direction for investigation, not a sized or accepted design.

## Outcome, boundary and constraints

The service boundary runs from raw-water access through treatment, usable storage, distribution and delivery to customers, including power, control, consumables, operators, maintenance and storm access. A treatment plant's output is an intermediate result; reliable customer supply also depends on water quality, delivery pressure and distribution availability.

- **Hard staffing constraint as stated:** operators can staff only two locations. A concept requiring more staffed locations is infeasible without an explicit change to that constraint. This does not automatically prohibit more physical units, but unattended units cannot be assumed feasible: maintenance visits, competence, alarms and storm recovery still require a staffing/access case.
- **Operating facts to design around:** seasonal demand and storm road closures. Treat road access during closures as unavailable, not merely inconvenient. Whether closures coincide with high demand or maintenance needs is unknown.
- **Unspecified outcome limits:** acceptable interruption duration/frequency, minimum service and water-quality basis, critical-user needs, storm design conditions and recovery time. The service owner must set these from the district's actual obligations and needs; none is invented here.
- **Preference:** the sponsor favors the largest plant for its claimed lower unit production cost. That cost comparison is supplied as the sponsor's rationale, with no costing evidence. It must be reconciled with lifecycle service cost and continuity, not treated as a hard constraint or a verified economic result.

## Useful concepts

| Concept | How it could maintain service | What must be true; principal exposure | Evidence needed before selection |
| --- | --- | --- | --- |
| **C-01 Larger central plant** | More capacity can meet seasonal peaks and replenish reserves faster. Independently isolatable treatment trains could permit partial operation during maintenance. | Simply replacing one plant with a larger single shutdown dependency leaves the stated outage mechanism. Train isolation is an added concept, not a supplied feature. Common intake, power, chemicals, controls or distribution may still stop all output. One site may ease staffing, but its workload and support needs are unknown. | Why current maintenance interrupts all treatment; capacity available during each maintenance task; common dependencies; seasonal throughput and full service-cost estimate |
| **C-02 Distributed treatment at up to two staffed locations** | One location may continue producing when the other is maintained; proximity may serve areas cut off by a distribution failure. | The surviving unit plus storage must meet the agreed service demand, and water must reach affected customers. Independence is not established by geography: source, power, consumables, operators, flood exposure and pipelines can be shared. Road closures may strand repairs and supplies at either location. More than two staffed sites violates the current constraint. | Hydraulic/service zones and interconnection; remaining capacity with one site out; common-cause exposure; actual two-site staffing/shift and maintenance plan; resupply during closures |
| **C-03 Additional clean-water storage with the existing plant** | Buffer already treated water so delivery continues while treatment is unavailable. May fit current staffed-site capacity if operation/maintenance is supportable. | Storage covers a finite deficit; it does not create water or repair inadequate seasonal production. Usable volume, initial fill, water quality/turnover, pumping and delivery must remain adequate. Long or repeated outages can exhaust it; refill before the next outage matters. A tank at a third location is not assumed unattended without review. | Outage and road-closure durations; seasonal demand trace; usable reserve and pressure/power; refill headroom; water-quality management and maintenance burden; siting/access |
| **C-04 Hybrid: storage plus maintenance isolation/operational changes** | Schedule planned work when feasible, isolate maintainable plant sections and use a reserve for residual downtime. Could remove the particular maintenance interruption without a full replacement. | Scheduling alone cannot protect against unplanned failure or storm overlap. Isolation depends on existing topology and serviceability. Storage remains finite and common distribution dependencies remain. | Maintenance work breakdown, isolation survey, restoration times with/without road access, operable remaining production and reserve needs |

Retaining the current arrangement is a useful cost/reference case, but it retains the reported interruption problem. Trucked emergency water cannot be presumed an effective substitute while access roads are closed. Remote control does not itself solve physical maintenance or resupply.

## First investigation and the question that can reverse the direction

**The most consequential question is: during the longest credible treatment interruption, including storm-delayed restoration at seasonal demand, can maintainable clean-water storage cover the net service deficit until treatment recovers and reserves can be replenished?**

If yes, C-03 or C-04 may directly address the failure with a supportable operating arrangement. If no—because the outage is too long, storage cannot be kept usable/delivered, refilling is insufficient, or production itself is inadequate—remaining treatment capacity during maintenance becomes central. C-02 or independently maintainable central trains then deserve priority. This is a conditional recommendation, not a claim that storage is already cheaper or sufficient.

Start with the existing system because it can reveal that distinction at low commitment:

1. **Operations and maintenance:** reconstruct each service interruption from maintenance/failure start to restored customer service, including mobilization, road access, repair, restart and refill. Identify which tasks actually force a whole-plant stop and which could be isolated. Include unplanned failures; do not assume their durations equal scheduled work.
2. **Demand and delivery:** collect seasonal demand time series, critical-user service needs, current usable storage and start-of-outage fill, treatment output/headroom, distribution constraints and outages. Use consistent time windows; annual average demand can hide the seasonal limiting case.
3. **Joint scenarios:** compare normal maintenance, peak-demand maintenance, storm without access, and a plausible overlap. Establish scenario credibility with local records and operators rather than assigning invented probabilities. Inspect power, source, chemicals, pumping and communications as shared dependencies.
4. **Feasibility screen:** check both staffing locations and total operating/maintenance workload, water-quality management, delivery continuity and recovery for each concept before a cost ranking. Obtain comparable acquisition, energy, chemicals, staffing, replacement, reserve upkeep, logistics and interruption-cost estimates only for concepts that can meet the outcome.

A transparent water-balance check can use `dV/dt = Q_available − D − L`, where `V` is usable clean-water reserve, `D` is time-varying service demand and `L` is relevant distribution/storage loss. Across each scenario, reserve must remain above the agreed operational minimum; restoration must provide enough spare output to recover it. Integrating the net deficit gives a preliminary required buffer. This is an unpopulated analysis plan: no volumes or sizing result can be calculated from the supplied facts. Hydraulic delivery and water quality require their own checks; a positive volume balance alone is insufficient.

## Decision and measures

Authorize a bounded outage/demand/maintainability study and keep C-02–C-04 open. Do not authorize a plant size solely from unit production cost. The first decision is whether the problem is primarily a bridgeable interruption, insufficient remaining treatment capacity, inadequate overall seasonal production, or a combination.

Compare concepts using customer interruption frequency and duration, people/critical users affected, unmet service volume, water-quality conformance under the adopted local basis, coverage through the agreed no-access interval, time to restore reserve, two-location staffing feasibility, and lifecycle cost per unit of compliant water actually delivered. Set targets and trade weights with the sponsor and operators after establishing the evidence. A hard continuity or staffing failure cannot be averaged away by a favorable cost score.

No performance, cost, reliability or staffing estimates have been invented, and no simulation or field test was executed.
