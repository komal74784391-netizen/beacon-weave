# Beacon Weave

Status: **Released** - v1.1.0 (2026-10-05)

Fault-tolerant time synchronisation for mesh nodes.  The implementation tolerates
dropped beacons and transient clock skew while keeping a bounded error envelope.

## Layout

- `src/beacon_weave/sync.py` - beacon filtering and clock correction
- `data/topology.yaml` - example mesh topology
- `experiments/latency.md` - latency experiment notes
