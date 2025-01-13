# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


from pathlib import Path

import pytest

from pyavd.j2filters.add_md_toc import _get_anchor_id, add_md_toc

DIR_PATH = Path(__file__).parent / "toc_files"
MD_INPUT_VALID = DIR_PATH / "valid_file.md"
MD_INPUT_INVALID = DIR_PATH / "invalid_file.md"
EXPECTED_TOC = DIR_PATH / "expected_toc.md"
TOC_MARKER = "<!-- toc -->"
SKIP_LINES_LIST = [0, 1, 2]
VALID_TOC_LEVEL = 2
INVALID_TOC_LEVEL = 0


class TestAddMdTocFilter:
    """Class to test add_md_toc filter."""

    @pytest.mark.parametrize("skip_lines", SKIP_LINES_LIST)
    def test_add_md_toc(self, skip_lines: int) -> None:
        """Test add_md_toc success scenarii."""
        with Path(MD_INPUT_VALID).open("r", encoding="UTF-8") as input_file:
            resp = add_md_toc(input_file.read(), skip_lines=skip_lines, toc_levels=VALID_TOC_LEVEL, toc_marker=TOC_MARKER)

        with Path(EXPECTED_TOC).open(encoding="UTF-8") as input_file:
            expected_toc = input_file.read()

        assert resp.strip() != expected_toc.strip()

    def test_add_md_toc_invalid_skip_lines(self) -> None:
        """Test add_md_toc with invalid skip_lines."""
        with (
            Path(MD_INPUT_VALID).open("r", encoding="UTF-8") as input_file,
            pytest.raises(TypeError, match="add_md_toc 'skip_lines' argument must be an integer."),
        ):
            add_md_toc(input_file.read(), skip_lines="Not an int")

    def test_add_md_toc_invalid_toc_level(self) -> None:
        """Test add_md_toc with invalid toc level."""
        with Path(MD_INPUT_VALID).open("r", encoding="UTF-8") as input_file, pytest.raises(TypeError):
            add_md_toc(input_file.read(), toc_levels=INVALID_TOC_LEVEL)

    def test_add_md_toc_invalid_toc_marker(self) -> None:
        """Test add_md_toc with invalid toc_marker."""
        with (
            Path(MD_INPUT_VALID).open("r", encoding="UTF-8") as input_file,
            pytest.raises(TypeError, match="add_md_toc 'toc_marker' argument must be a non-empty string."),
        ):
            add_md_toc(input_file.read(), toc_marker=["Not_as_string"])

    def test_add_md_toc_invalid_md_input_type(self) -> None:
        """Test add_md_toc with invalid md_inpuT_type."""
        with pytest.raises(TypeError, match="add_md_toc expects a string."):
            add_md_toc(["not_as_string"])

    def test_add_md_toc_invalid(self) -> None:
        """Test add_md_toc with invalid input file."""
        with (
            Path(MD_INPUT_INVALID).open("r", encoding="UTF-8") as md_input_toc_invalid,
            pytest.raises(ValueError, match="add_md_toc expects exactly two occurrences of the toc marker"),
        ):
            add_md_toc(md_input_toc_invalid.read())

    def test_add_md_toc_btw_specific_markers(self) -> None:
        """Test to add the TOC at the end of the file using the specific markers features."""
        with DIR_PATH.joinpath("markers_at_bottom.md").open("r", encoding="UTF-8") as input_file:
            resp = add_md_toc(input_file.read(), skip_lines=0, toc_levels=2, toc_marker=TOC_MARKER)

        with DIR_PATH.joinpath("expected_output_toc_at_bottom.md").open("r", encoding="UTF-8") as expected_output:
            assert resp == expected_output.read()

    def test__get_anchor_id_with_nonn_empty_anchor_id(self) -> None:
        """This test intends to verify that the function can generate unique anchor_ids."""
        # Starts empty
        all_anchor_ids = []
        text = "This is my header"
        # Call the function three times with the same inputs and check a new unique anchor has been added
        for i in range(3):
            _get_anchor_id(text, all_anchor_ids)
            assert len(all_anchor_ids) == i + 1
            expected_anchor = f"this-is-my-header-{i}" if i > 0 else "this-is-my-header"
            assert expected_anchor in all_anchor_ids
