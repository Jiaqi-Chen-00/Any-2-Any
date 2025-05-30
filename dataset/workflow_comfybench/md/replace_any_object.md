- Nodes:
    - N33:
        - node_type: "LoadImage"
        - image: "cat_stand.jpg"
    - N38:
        - node_type: "VAEEncodeForInpaint"
        - grow_mask_by: 0
    - N59:
        - node_type: "CLIPTextEncode"
        - text: "text, watermark"
    - N60:
        - node_type: "CLIPTextEncode"
        - text: "a dog"
    - N101:
        - node_type: "GroundingDinoSAMSegment (segment anything)"
        - prompt: "cat"
        - threshold: 0.2
    - N102:
        - node_type: "GroundingDinoModelLoader (segment anything)"
        - model_name: "GroundingDINO_SwinT_OGC (694MB)"
    - N103:
        - node_type: "SAMModelLoader (segment anything)"
        - model_name: "sam_vit_l (1.25GB)"
    - N105:
        - node_type: "KSamplerAdvanced"
        - add_noise: "enable"
        - noise_seed: 858603438156931
        - control_after_generate: "randomize"
        - steps: 20
        - cfg: 8
        - sampler_name: "dpmpp_2m"
        - scheduler: "normal"
        - start_at_step: 0
        - end_at_step: 10000
        - return_with_leftover_noise: "disable"
    - N106:
        - node_type: "VAEDecode"
    - N109:
        - node_type: "KSamplerAdvanced"
        - add_noise: "enable"
        - noise_seed: 576713408471301
        - control_after_generate: "randomize"
        - steps: 20
        - cfg: 8
        - sampler_name: "dpmpp_2m"
        - scheduler: "normal"
        - start_at_step: 0
        - end_at_step: 10000
        - return_with_leftover_noise: "disable"
    - N112:
        - node_type: "CheckpointLoaderSimple"
        - ckpt_name: "dreamshaper_8Inpainting.safetensors"
    - N113:
        - node_type: "GrowMask"
        - expand: 5
        - tapered_corners: True
    - N115:
        - node_type: "SaveImage"
        - filename_prefix: "ComfyUI"

- Links:
    - L21: N33.image -> N38.pixels
    - L22: N112.vae -> N38.vae
    - L23: N113.mask -> N38.mask
    - L24: N112.clip -> N59.clip
    - L25: N112.clip -> N60.clip
    - L26: N103.sam_model -> N101.sam_model
    - L27: N102.grounding_dino_model -> N101.grounding_dino_model
    - L28: N33.image -> N101.image
    - L29: N112.model -> N105.model
    - L30: N60.conditioning -> N105.positive
    - L31: N59.conditioning -> N105.negative
    - L32: N38.latent -> N105.latent_image
    - L33: N109.latent -> N106.samples
    - L34: N112.vae -> N106.vae
    - L35: N112.model -> N109.model
    - L36: N60.conditioning -> N109.positive
    - L37: N59.conditioning -> N109.negative
    - L38: N105.latent -> N109.latent_image
    - L39: N101.mask -> N113.mask
    - L40: N106.image -> N115.images
