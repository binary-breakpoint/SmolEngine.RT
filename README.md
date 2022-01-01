# SmolEngine SDK
![SmolEngine](https://i.imgur.com/ZSfnTCi.png)

SmoEngine is an experimental 3D game engine based on the idea of creating a high-performance, easy to use ray tracing only game engine. The project is being actively developed by one person, and at the moment it should be considered only as a tech demo. Also currently only precompiled binaries are available, but this may change in the future.

## Features
### Rendering
- [x] Disney PBR
- [x] Real-Time Path Tracer
- [x] Own abstraction layer on top of Vulkan API
- [x] [FidelityFX Super Resolution](https://www.amd.com/en/technologies/radeon-software-fidelityfx-super-resolution)
- [x] [Dear ImGUI](https://github.com/ocornut/imgui) integration
- [x] In-Game UI (text, buttons, input fields, etc)
- [x] Raytracing/Graphics/Compute pipelines
- [x] Bloom
- [ ] Skeleton animations (some support)
- [ ] Custom materials (shaders)
- [ ] [Real-Time Denoiser](https://developer.nvidia.com/nvidia-rt-denoiser)
- [ ] Particle system

### Core

- [x] C#/C++ Scripting API
- [x] Jobs System
- [x] Audio
- [x] Entity Component System
- [x] Prefabs
- [x] Level Editor
- [x] Physics: 2D ([Box2D](https://github.com/erincatto/box2d)), 3D ([Bullet3](https://github.com/bulletphysics/bullet3))
- [x] Profilers: [Optick](https://github.com/bombomby/optick), [Nsight Graphics](https://developer.nvidia.com/nsight-graphics/)
- [x] C++ 20
- [ ] Networking
- [ ] Pathfinding
- [ ] Docs


## Requirements
- Ray tracing capable GPU (RTX 20 series or higher)
- Visual Studio 2022 (full C++20 support)
- Python 3.x

## Extensions
- VK_KHR_16BIT_STORAGE_EXTENSION_NAME
- VK_KHR_SHADER_FLOAT16_INT8_EXTENSION_NAME
- VK_KHR_ACCELERATION_STRUCTURE_EXTENSION_NAME
- VK_KHR_RAY_TRACING_PIPELINE_EXTENSION_NAME
- VK_KHR_BUFFER_DEVICE_ADDRESS_EXTENSION_NAME
- VK_KHR_DEFERRED_HOST_OPERATIONS_EXTENSION_NAME
- VK_KHR_SPIRV_1_4_EXTENSION_NAME
- VK_KHR_SHADER_FLOAT_CONTROLS_EXTENSION_NAME

## Building
### Windows
1. Clone the repository: ```git clone https://github.com/Floritte/SmolEngine-SDK```
2. Install [Vulkan SDK 1.2.198.1](https://vulkan.lunarg.com/sdk/home#windows) or higher
3. Install [Python 3.9](https://www.python.org/downloads/) or higher
4. Install [gdown](https://github.com/wkentaro/gdown) package: ```pip install gdown```
5. Run `scripts/download_sdk.bat` to download SDK installer
