- Nodes:
    - N3:
        - node_type: "KSampler"
        - seed: 52117596413767
        - control_after_generate: "randomize"
        - steps: 20
        - cfg: 7
        - sampler_name: "dpmpp_3m_sde_gpu"
        - scheduler: "sgm_uniform"
        - denoise: 1
    - N5:
        - node_type: "EmptyLatentImage"
        - width: 768
        - height: 768
        - batch_size: 1
    - N6:
        - node_type: "CLIPTextEncode"
        - text: "a beautiful photograph of an old European city"
    - N7:
        - node_type: "CLIPTextEncode"
        - text: ""
    - N8:
        - node_type: "VAEDecode"
    - N9:
        - node_type: "SaveImage"
        - filename_prefix: "Result"
    - N12:
        - node_type: "unCLIPCheckpointLoader"
        - ckpt_name: "sd21-unclip-l.ckpt"
    - N13:
        - node_type: "CLIPVisionEncode"
    - N14:
        - node_type: "unCLIPConditioning"
        - strength: 1
        - noise_augmentation: 0.1
    - N15:
        - node_type: "LoadImage"
        - image: "budapest.jpg"

- Links:
    - L14: N5.latent -> N3.latent_image
    - L15: N12.model -> N3.model
    - L16: N7.conditioning -> N3.negative
    - L17: N14.conditioning -> N3.positive
    - L18: N12.clip -> N6.clip
    - L19: N12.clip -> N7.clip
    - L20: N3.latent -> N8.samples
    - L21: N12.vae -> N8.vae
    - L22: N8.image -> N9.images
    - L23: N12.clip_vision -> N13.clip_vision
    - L24: N15.image -> N13.image
    - L25: N13.clip_vision_output -> N14.clip_vision_output
    - L26: N6.conditioning -> N14.conditioning
