# Core AI Model Export Notes

These notes document experiments with Apple's `coreai-models` repository and on-device model export workflows.

## Environment

Initial local environment:

```bash
git --version
brew --version
xcodebuild -version
uv --version
```

Example tools used:

- macOS on Apple Silicon
- Xcode Beta / Xcode with Core AI support
- Homebrew
- `uv` for Python project execution
- Hugging Face Hub for model access

## Listing Supported Models

From the `coreai-models` repository:

```bash
uv run coreai.model.registry --list-models
```

Useful filters:

```bash
uv run coreai.model.registry --type llm --platform iOS --list-models
uv run coreai.model.registry --type utility --task segmentation --list-models
```

## Qwen3 0.6B iOS Export Dry Run

The following command resolves the export configuration without exporting the model:

```bash
uv run coreai.llm.export Qwen/Qwen3-0.6B \
  --compression-config models/qwen3/qwen3_0_6b_mixed_4bit_8bit.yaml \
  --compute-precision float16 \
  --max-context-length 4096 \
  --platform iOS \
  --dry-run
```

Expected resolved configuration fields:

- model: `Qwen/Qwen3-0.6B`
- platform: `iOS`
- compression: mixed 4-bit / 8-bit configuration
- compute precision: `float16`
- max context length: `4096`

## Qwen3 0.6B iOS Export

```bash
mkdir -p ~/Documents/learning/coreai-exports

uv run coreai.llm.export Qwen/Qwen3-0.6B \
  --compression-config models/qwen3/qwen3_0_6b_mixed_4bit_8bit.yaml \
  --compute-precision float16 \
  --max-context-length 4096 \
  --platform iOS \
  --output-dir ~/Documents/learning/coreai-exports
```

## Notes on Model Choice

For iOS experiments:

- `Qwen3-0.6B` is better for learning, fast iteration, and smaller devices.
- `Qwen3-4B` is more suitable when output quality matters, but it has higher storage, memory, and runtime cost.

## Gated Models

Some models, such as `facebook/sam3`, may require Hugging Face access approval. This repository does not include gated model files. Access should be requested from the official model page and used according to the model license.
