"""Regression checks for private-source release exclusions."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import package_release


class PackagePrivacyTests(unittest.TestCase):
    def test_private_sources_excluded_at_any_depth(self):
        with tempfile.TemporaryDirectory(dir=package_release.ROOT) as tmp:
            root = Path(tmp)
            with patch.object(package_release, "ROOT", root):
                for folder in ("private-research", "private-sources", "discord-downloads"):
                    for prefix in (Path(), Path("assets")):
                        source = root / prefix / folder / "sample.png"
                        source.parent.mkdir(parents=True, exist_ok=True)
                        source.touch()
                        self.assertFalse(package_release.should_include(source))

    def test_original_public_asset_is_included(self):
        with tempfile.TemporaryDirectory(dir=package_release.ROOT) as tmp:
            root = Path(tmp)
            source = root / "assets" / "original.png"
            source.parent.mkdir()
            source.touch()
            with patch.object(package_release, "ROOT", root):
                self.assertTrue(package_release.should_include(source))


if __name__ == "__main__":
    unittest.main()
