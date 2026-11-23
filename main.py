"""One-line pitch: convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

Writes exactly one sentence (<=240 characters) to /output/entry.txt.
Standard library only, no network, no randomness.
"""

import os

TEXT = (
    "Tell make.fun's AI agent your app idea in plain words \u2014 no coding, "
    "no jargon \u2014 and it will turn it into a real working app you can tap, "
    "use and share today, so the idea you've carried for years finally gets "
    "its first chance."
)


def main():
    assert 1 <= len(TEXT) <= 240, "entry must be 1-240 characters"
    assert TEXT.endswith("."), "entry must end with a full stop"
    assert ". " not in TEXT, "entry must be exactly one sentence"
    assert TEXT == TEXT.strip(), "entry must not have leading/trailing space"
    assert "  " not in TEXT, "entry must not contain double spaces"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
