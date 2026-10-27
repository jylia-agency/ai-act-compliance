"""Veille « intelligence économique » : liens saisis à la main par les bibliothécaires."""
LINKS: list[str] = []


def add_link(url: str) -> None:
    LINKS.append(url)
