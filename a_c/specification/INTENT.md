# Intent

Provide concrete implementations of the STDO axiomatic calculus that preserve
source-owned identities, constraints, permitted variation and unresolved meaning
while making declared symbolic models easier to inspect and acquire.

The shared specification defines the required behavior independently of a graph
library, authoring format, model provider or execution stack. A build tenant
chooses its computational realization and demonstrates the required preservation.
The first tenant uses Graphify's graph representation and tools. F_P remains
responsible for semantic interpretation; mechanical tools check only declared
properties and retain the evidence needed for further judgment.
