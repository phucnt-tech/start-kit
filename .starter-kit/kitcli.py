#!/usr/bin/env python3
"""
Starter Kit CLI
Commands:
  init [--preset python|java-maven] [--target DIR] [--dry-run]
  validate [--preset python|java-maven] [--target DIR]
  test -> alias of validate

Behavior:
- Copies kit files into target dir. If a file exists, writes .new sibling.
- Validate checks that expected files from core and selected preset exist.
"""
import argparse
import shutil
import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent
CORE_DIR = KIT_ROOT / "core"
PRESETS = {
    "python": KIT_ROOT / "presets" / "python",
    "java-maven": KIT_ROOT / "presets" / "java-maven",
}


def copy_tree(src: Path, dest_root: Path, dry_run: bool) -> None:
    for src_file in src.rglob("*"):
        if src_file.is_dir():
            continue
        rel = src_file.relative_to(src)
        dest_file = dest_root / rel
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        if dest_file.exists():
            dest_file = dest_file.with_suffix(dest_file.suffix + ".new")
        if dry_run:
            print(f"[dry-run] copy {rel} -> {dest_file.relative_to(dest_root)}")
        else:
            shutil.copy2(src_file, dest_file)
            print(f"copied: {dest_file.relative_to(dest_root)}")


def cmd_init(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    dry_run = args.dry_run
    copy_tree(CORE_DIR, target, dry_run)
    if args.preset:
        preset_dir = PRESETS.get(args.preset)
        if not preset_dir:
            print(f"Invalid preset: {args.preset}", file=sys.stderr)
            return 1
        copy_tree(preset_dir, target, dry_run)
    if not dry_run:
        print("Done. Review any *.new files and run make setup && make check.")
    return 0


def expected_files(preset: str | None) -> list[Path]:
    core_expected = [
        Path("README.md"),
        Path("CONTRIBUTING.md"),
        Path("STRUCTURE.template.md"),
        Path("PITFALLS.md"),
        Path("CONTEXT_PACK.md"),
        Path("CONTEXT_GUIDE.md"),
        Path("AI-GUIDELINES.md"),
        Path(".editorconfig"),
        Path(".gitignore"),
        Path(".pre-commit-config.yaml"),
        Path("Makefile"),
        Path("contexts/README.md"),
        Path("scripts/bootstrap.sh"),
        Path("scripts/context-pack.sh"),
        Path("scripts/resume.sh"),
        Path("scripts/smoke.sh"),
    ]
    preset_expected: list[Path] = []
    if preset == "python":
        preset_expected = [
            Path("Makefile"),
            Path("pyproject.toml"),
            Path("requirements-dev.txt"),
            Path(".env.example"),
            Path("scripts/smoke.sh"),
            Path(".pre-commit-config.yaml"),
        ]
    elif preset == "java-maven":
        preset_expected = [
            Path("Makefile"),
            Path("pom.template.additions.xml"),
            Path("config/checkstyle/checkstyle.xml"),
            Path(".env.example"),
            Path("scripts/smoke.sh"),
        ]
    return core_expected + preset_expected


def cmd_validate(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    missing: list[Path] = []
    for rel in expected_files(args.preset):
        if not (target / rel).exists():
            alt = rel.with_suffix(rel.suffix + ".new")
            if not (target / alt).exists():
                missing.append(rel)
    if missing:
        print("Missing files:")
        for m in missing:
            print(f"  {m}")
        return 1
    print("Validate OK")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Starter Kit CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="copy kit into target directory")
    p_init.add_argument("--preset", choices=list(PRESETS.keys()), help="preset to apply")
    p_init.add_argument("--target", default=".", help="target directory (default: cwd)")
    p_init.add_argument("--dry-run", action="store_true")
    p_init.set_defaults(func=cmd_init)

    p_val = sub.add_parser("validate", help="check required kit files exist")
    p_val.add_argument("--preset", choices=list(PRESETS.keys()), default=None, nargs="?")
    p_val.add_argument("--target", default=".", help="target directory (default: cwd)")
    p_val.set_defaults(func=cmd_validate)

    p_test = sub.add_parser("test", help="alias of validate")
    p_test.add_argument("--preset", choices=list(PRESETS.keys()), default=None, nargs="?")
    p_test.add_argument("--target", default=".", help="target directory (default: cwd)")

    def _test(args):
        return cmd_validate(args)

    p_test.set_defaults(func=_test)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
