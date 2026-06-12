# Apple Core AI Experiments

This repository contains personal learning notes and small experiments around on-device AI on Apple platforms.

The current focus is on:

- Apple Core AI and Core ML model export workflows
- Running open-source models locally on Apple Silicon
- Computer vision tasks such as image recognition, segmentation, and object tracking
- Swift, iOS, macOS, and visionOS application prototyping
- Responsible local inference and privacy-preserving AI applications

## Motivation

Modern foundation models are increasingly useful on local devices. This repository is a practical notebook for exploring how open-source models can be prepared, tested, and integrated into native Apple applications.

The goal is not to redistribute model weights. Instead, the repository documents reproducible experiments, export commands, environment notes, and small utility scripts for learning and prototyping.

## Current Experiments

### 1. Core AI LLM export notes

Experiments with Apple `coreai-models`, including small Qwen models for iOS/macOS deployment.

Example topics:

- Listing supported model presets
- Running dry-run exports
- Comparing iOS model compression options
- Recording output bundle structure

See: [`docs/coreai-model-export-notes.md`](docs/coreai-model-export-notes.md)

### 2. Image processing utilities

Small scripts for preparing images before segmentation or recognition experiments.

See: [`scripts/prepare_image.py`](scripts/prepare_image.py)

### 3. Object tracking notes

Early notes about object tracking workflows for mobile and spatial computing applications.

See: [`docs/object-tracking-notes.md`](docs/object-tracking-notes.md)

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── coreai-model-export-notes.md
│   ├── object-tracking-notes.md
│   └── segmentation-research-notes.md
├── examples/
│   └── sample_prompts.md
├── notes/
│   └── environment.md
├── scripts/
│   ├── prepare_image.py
│   ├── inspect_model_folder.py
│   └── check_hf_access.py
├── requirements.txt
└── .gitignore
```

## Disclaimer

This repository is for personal learning, research, and prototyping. It does not include proprietary model weights or gated model files. Any third-party model should be downloaded from its official source and used according to its license and usage restrictions.
