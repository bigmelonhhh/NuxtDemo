import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def assert_contains(path: str, needle: str) -> None:
    content = read(path)
    if needle not in content:
        raise AssertionError(f"{path} does not contain {needle!r}")


def main() -> None:
    package_json = json.loads(read("package.json"))
    dependencies = package_json.get("dependencies", {})

    if dependencies.get("@nuxt/ui") != "4.8.1":
        raise AssertionError("package.json must depend on @nuxt/ui@4.8.1")

    if "tailwindcss" not in dependencies:
        raise AssertionError("package.json must depend on tailwindcss")

    assert_contains("nuxt.config.ts", "'@nuxt/ui'")
    assert_contains("app/assets/styles/main.css", '@import "tailwindcss";')
    assert_contains("app/assets/styles/main.css", '@import "@nuxt/ui";')
    assert_contains("app/app.vue", "<UApp>")
    assert_contains("app/pages/index.vue", "<UButton")
    assert_contains("app/pages/index.vue", "<UCard")
    assert_contains("app/pages/index.vue", "<UIcon")


if __name__ == "__main__":
    main()
