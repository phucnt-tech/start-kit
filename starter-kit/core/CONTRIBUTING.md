# CONTRIBUTING

## Branch & commit
- Branch: `feature/<id>-<desc>`
- Commit: conventional (feat/fix/chore/docs/test/refactor), nhỏ gọn.

## Review
- PR template bắt buộc (WHAT/WHY/TEST/RISK/ROLLBACK/FLAG).
- CI (lint+test) phải pass. Không merge nếu thiếu test cho logic mới (trừ khi ghi chú rõ).

## Coding standards
- Formatter + linter bắt buộc (xem Makefile). Pre-commit chạy tự động.
- Không commit secret. Dùng vault/secret manager.
- Không đụng prod config/URL trong dev.

## Tests
- Viết unit cho logic, smoke/e2e nếu chạm IO.
- Giữ test deterministic; seed random khi cần.

## Decision log
- Nếu quyết định lớn/trade-off: thêm ADR trong DECISIONS/.

## Release/Deploy
- Nêu rõ flag, migration, rollback plan trong PR.
- Feature flag default off; dọn flag sau khi stable.
