# services/

Government Operations Modules — department-facing capabilities, each owned by its respective domain team.

See Section 13 (Three-Layer Architecture, Layer 2) and Section 14 (System Modules) of the root README.

Every service here is a bounded module. No service directly accesses another service's private data store — cross-module interaction happens through `libs/shared-contracts`, the API Gateway (`platform/api-gateway`), or the enterprise event backbone.

Module ownership is assigned by office/role, not by individual, and confirmed by the City Administrator's Department during Phase 0 governance setup (see Section 27, Risk Management).
