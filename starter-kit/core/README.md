# Project README (template)

## Mục tiêu
Tóm tắt ngắn (2-3 câu) về sản phẩm/ service.

## Chạy nhanh
```bash
make setup
make run   # hoặc make dev
```

## Kiến trúc
- Entry points: (liệt kê main app, CLI, worker)
- Modules chính:
- Data/DB:
- External deps/APIs:

## Dev workflow
- Branch: main protected; feature/<id>-<desc>
- CI: lint + test must pass trước merge.
- Review: >=1 reviewer; check WHAT/WHY/TEST/ROLLBACK.

## Env
- Copy `.env.example` -> `.env.local`, điền secret từ vault.
- Profiles: dev/staging/prod tách biệt.

## Liên hệ
- Owners: …
- On-call: …
