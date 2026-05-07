"""Tests for the project_name package.

This module demonstrates how to write tests using pytest
with type hints and the Arrange-Act-Assert pattern.
"""

import pytest

from project_name import __version__


class TestVersion:
    """Tests for the version module."""

    def test_version_is_string(self) -> None:
        """Test that __version__ is a string.

        Arrange: Import the version constant.
        Act: Check its type.
        Assert: It should be a string.
        """
        # Arrange
        expected_type = str

        # Act
        version_type = type(__version__)

        # Assert
        assert version_type is expected_type

    def test_version_matches_expected(self) -> None:
        """Test that the version matches the expected value.

        Arrange: Define the expected version string.
        Act: Compare with the actual version.
        Assert: They should be equal.
        """
        # Arrange
        expected_version = "0.1.0"

        # Act
        actual_version = __version__

        # Assert
        assert actual_version == expected_version

    def test_version_is_not_empty(self) -> None:
        """Test that the version string is not empty."""
        # Arrange + Act + Assert combined for simple checks
        assert __version__, "Version should not be empty"


class TestMath:
    """Example tests for basic math operations (demonstration)."""

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (10, -5, 5),
        ],
    )
    def test_addition(self, a: int, b: int, expected: int) -> None:
        """Test that addition works correctly with various inputs.

        Args:
            a: First operand.
            b: Second operand.
            expected: Expected result.
        """
        result = a + b
        assert result == expected

    def test_subtraction(self) -> None:
        """Test basic subtraction."""
        # Arrange
        x = 10
        y = 3

        # Act
        result = x - y

        # Assert
        assert result == 7
