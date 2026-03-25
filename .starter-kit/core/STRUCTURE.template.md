# STRUCTURE (fill with real repo map)

- entrypoints:
  - app: ...
  - worker: ...
- modules:
  - moduleA: purpose, deps
  - moduleB: ...
- config: path + description (env, feature flags)
- data/DB: migrations path, seeds, test fixtures
- api/schema: OpenAPI/GraphQL/proto paths
- scripts: common scripts (bootstrap, smoke, migration)
- tests: layout and conventions
- legacy: legacy areas & how to touch safely
