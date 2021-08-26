from typing import Optional, overload

import torch


class Tensor(object):
    @overload
    def __init__(self):
        """Create an empty ragged tensor."""
        pass

    @overload
    def __init__(self, data: list, dtype: Optional[torch.dtype] = None) -> None:
        """Create a ragged tensor with two axes.

        Args:
          data:
            A list-of-list of integers or real numbers.
          dtype:
            Optional. If None, it infers the dtype from `data`
            automatically, which is either `torch.int32` or
            `torch.float32.
        """
        pass

    @property
    def dtype(self) -> torch.dtype:
        """Return the dtype of this tensor."""
        pass

    @property
    def device(self) -> torch.device:
        """Return the device of this tensor."""
        pass

    @property
    def data(self) -> torch.Tensor:
        """Return the underlying memory as a 1-D tensor."""

        pass

    def __str__(self) -> str:
        """Return a string representation of this tensor"""
        pass

    def __eq__(self, other: "Tensor") -> bool:
        """Compare two ragged tensors.

        Caution::
          The two tensors MUST have the same dtype. Otherwise,
          it throws.

        Args:
          other:
            The tensor to be compared.
        Returns:
          Return True if the two tensors are equal.
          Return False otherwise.

        """
        pass

    def __ne__(self, other: "Tensor") -> bool:
        """Compare two ragged tensors.

        Caution::
          The two tensors MUST have the same dtype. Otherwise,
          it throws.

        Args:
          other:
            The tensor to be compared.
        Returns:
          Return True if the two tensors are NOT equal.
          Return False otherwise.

        """
        pass

    def clone(self) -> "Tensor":
        """Return a copy of this tensor."""
        pass

    @overload
    def to(self, o: torch.device) -> "Tensor":
        """Transfer this tensor to a given device.

        Note::
          If `self` is already on the specified device, return a
          ragged tensor sharing the underlying memory with `self`.
          Otherwise, a new tensor is returned.

        Args:
          o:
            The target device to move this tensor.

        Returns:
          Return a tensor on the given device.
        """
        pass

    @overload
    def to(self, o: torch.dtype) -> "Tensor":
        """Convert this tensor to a specific dtype.

        Note::
          If `self` is already of the specified `dtype`, return
          a ragged tensor sharing the underlying memory with `self`.
          Otherwise, a new tensor is returned.

        Caution::
          Currently, only for dtypes torch.int32, torch.float32, and
          torch.float64 are implemented. We can support other types
          if needed.

        Args:
          o:
            The `dtype` this tensor should be converted to.

        Returns:
          Return a tensor of the given `dtype`.
        """
        pass
