#!/usr/bin/env python3
"""Check whether a Hugging Face model repository can be accessed.

This script does not download model weights. It queries model metadata through
huggingface_hub and reports whether the repository appears accessible.

Example:
    python scripts/check_hf_access.py Qwen/Qwen3-0.6B
    python scripts/check_hf_access.py facebook/sam3
"""

from __future__ import annotations

import argparse

from huggingface_hub import HfApi
from huggingface_hub.utils import GatedRepoError, RepositoryNotFoundError, HfHubHTTPError


def check_model(model_id: str) -> None:
    api = HfApi()
    try:
        info = api.model_info(model_id)
    except GatedRepoError:
        print(f"Gated model: {model_id}")
        print("Access is restricted. Accept the license and request access on Hugging Face.")
        return
    except RepositoryNotFoundError:
        print(f"Repository not found or private: {model_id}")
        return
    except HfHubHTTPError as error:
        print(f"Hugging Face request failed: {error}")
        return

    print(f"Model: {info.modelId}")
    print(f"Private: {info.private}")
    print(f"Gated: {info.gated}")
    print(f"Downloads: {info.downloads}")
    print("Access check completed.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Check Hugging Face model access.")
    parser.add_argument("model_id", help="Hugging Face model id, for example Qwen/Qwen3-0.6B")
    args = parser.parse_args()

    check_model(args.model_id)


if __name__ == "__main__":
    main()
