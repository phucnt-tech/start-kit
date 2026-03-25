# Context management checklist

## Khi bắt đầu task/feature
- Tạo context pack: `scripts/context-pack.sh <project> <feature>` -> điền context.md (WHAT/WHY/Scope/API/Test/Blockers/Next/Flag).
- Tạo notes file ngày: notes-YYYYMMDD.md.
- Ghi rõ issue/PR ID, branch name.

## Khi đang làm
- Sau mỗi chặng: cập nhật context.md (Next steps, test status, blockers).
- Log nhanh vào notes-YYYYMMDD.md: thay đổi chính, test đã chạy/kết quả, quyết định nhỏ.
- Nếu dùng AI: lưu prompt quan trọng, API/contract đã nhắc.

## Khi tạm dừng/chuyển task
- Ghi TODO còn lại, test fail/skip, file đang dở, giả thuyết cần kiểm chứng.
- Push branch; note commit hash/branch vào context.md.
- Link mọi tài liệu tham chiếu (ADR, API spec) vào context.md.

## Khi quay lại (resume)
- Chạy `scripts/resume.sh <project> <feature>` để xem context + notes gần nhất.
- `git status`, `git diff` nhanh; xem notes cuối; rerun test fail gần nhất.
- Đánh dấu tiến độ mới và cập nhật Next steps.

## Khi đóng task
- Cập nhật context.md: kết quả, test pass, flag/migration đã gỡ/chưa.
- Thêm tóm tắt WHAT/WHY/HOW/ROLLBACK vào PR.
- Nếu có quyết định/trade-off mới: ghi ADR trong DECISIONS/.
- Xoá/đóng flag tạm thời nếu không cần.

## Thực hành tốt
- Mỗi feature có folder riêng: contexts/<project>/<feature>/.
- Mỗi ngày có notes riêng; không trộn ngày để dễ tìm.
- Ngắn gọn, dạng bullet; đủ để người khác resume sau 5 phút đọc.
- Không dán secret/PII vào context/notes.
- Feature flags: ghi trạng thái và điều kiện gỡ.
