# Object Tracking Notes

This document collects early ideas for object tracking and spatial AI experiments on Apple platforms.

## Target Scenarios

- Track objects in camera frames on iPhone or iPad
- Use object tracking in visionOS spatial applications
- Combine image segmentation with user interaction
- Explore local inference for privacy-sensitive visual workflows

## Possible Pipeline

A practical object tracking pipeline may include:

1. Input frame acquisition
2. Object detection or segmentation
3. Tracking state initialization
4. Frame-to-frame tracking update
5. Result visualization in SwiftUI / RealityKit
6. Optional export of tracking data for debugging

## Related Tasks

- Image recognition
- Object detection
- Promptable segmentation
- Mask tracking
- Spatial anchoring
- Visual interaction in mixed reality

## Apple Platform Topics to Explore

- Vision framework
- Core ML / Core AI model integration
- Metal performance considerations
- RealityKit entity updates
- ARKit anchors and coordinate transforms

## Open Questions

- How small can the model be while still being useful on-device?
- What is the latency difference between CPU, GPU, and Neural Engine execution?
- How should masks or bounding boxes be mapped into spatial coordinates?
- How can object tracking be combined with hand gestures in visionOS?
