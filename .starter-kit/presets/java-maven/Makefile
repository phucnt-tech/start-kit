SHELL := /bin/bash
MVN ?= ./mvnw

.PHONY: setup fmt lint test check run smoke

setup:
	$(MVN) -q -DskipTests install -pl !:unused || true

fmt:
	$(MVN) spotless:apply

lint:
	$(MVN) -DskipTests verify -DskipITs=true -P check

test:
	$(MVN) test

check: fmt lint test

run:
	$(MVN) spring-boot:run

smoke:
	@./scripts/smoke.sh
