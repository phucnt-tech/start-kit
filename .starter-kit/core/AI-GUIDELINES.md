# AI Usage Guidelines

- Không đưa secret/token/PII/prod URL vào prompt. Dùng placeholder/redaction.
- Yêu cầu: tuân thủ style (formatter/linter), không tạo code từ nguồn không rõ license. Nếu trích dẫn, ghi nguồn và kiểm license (MIT/Apache ok; tránh GPL nếu repo không tương thích).
- Temperature thấp khi sinh code; giữ deterministic.
- Luôn review: logic, edge cases, security (authz, input validation, injection), hiệu năng.
- Phải thêm/điều chỉnh test cho code sinh ra.
- Không merge nếu thiếu test hoặc CI fail.
- Prompt nên kèm context (interface, type, config) để tránh bịa API.
- Log prompt/response nếu dùng tự động, tuân thủ privacy (không log PII).
