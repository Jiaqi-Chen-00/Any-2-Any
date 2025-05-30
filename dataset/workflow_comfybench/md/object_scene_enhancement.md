- Nodes:
    - N4:
        - node_type: "CheckpointLoaderSimple"
        - ckpt_name: "majicmixRealistic_v7.safetensors"
    - N6:
        - node_type: "CLIPTextEncode"
        - text: "Urban roadside night view"
    - N7:
        - node_type: "CLIPTextEncode"
        - text: "Person"
    - N11:
        - node_type: "LoadImage"
        - image: "titled_book.png"
    - N12:
        - node_type: "easy imageRemBg"
        - image_output: "RMBG-1.4"
        - save_prefix: "Preview"
        - torchscript_jit: "ComfyUI"
    - N14:
        - node_type: "ImageResize+"
        - width: 1024
        - height: 1024
        - interpolation: "nearest"
        - method: "keep proportion"
        - condition: "always"
        - multiple_of: 0
    - N16:
        - node_type: "KSampler"
        - seed: 21208813937248
        - control_after_generate: "randomize"
        - steps: 25
        - cfg: 2
        - sampler_name: "dpmpp_2m_sde"
        - scheduler: "karras"
        - denoise: 0.9
    - N17:
        - node_type: "VAEDecode"
    - N42:
        - node_type: "EmptyLatentImage"
        - width: 512
        - height: 512
        - batch_size: 1
    - N43:
        - node_type: "VAEDecode"
    - N46:
        - node_type: "ImageCompositeMasked"
        - x: 0
        - y: 0
        - resize_source: False
    - N47:
        - node_type: "SplitImageWithAlpha"
    - N51:
        - node_type: "DetailTransfer"
        - mode: "add"
        - blur_sigma: 0.5
        - blend_factor: 1
    - N52:
        - node_type: "SaveImage"
        - filename_prefix: "ComfyUI"
    - N58:
        - node_type: "easy ipadapterApply"
        - preset: "PLUS (high strength)"
        - lora_strength: 0.6
        - provider: "CPU"
        - weight: 1
        - weight_faceidv2: 1
        - start_at: 0
        - end_at: 1
        - cache_mode: "all"
        - use_tiled: False
    - N61:
        - node_type: "LoadAndApplyICLightUnet"
        - model_path: "IC-Light\iclight_sd15_fcon.safetensors"
    - N62:
        - node_type: "ICLightConditioning"
        - multiplier: 0.182
    - N82:
        - node_type: "VAEEncode"
    - N83:
        - node_type: "VAEEncode"

- Links:
    - L34: N4.clip -> N6.clip
    - L35: N4.clip -> N7.clip
    - L36: N14.image -> N12.images
    - L37: N11.image -> N14.image
    - L38: N58.model -> N16.model
    - L39: N62.positive -> N16.positive
    - L40: N62.negative -> N16.negative
    - L41: N82.latent -> N16.latent_image
    - L42: N16.latent -> N17.samples
    - L43: N4.vae -> N17.vae
    - L44: N14.width -> N42.width
    - L45: N14.height -> N42.height
    - L46: N42.latent -> N43.samples
    - L47: N4.vae -> N43.vae
    - L48: N43.image -> N46.destination
    - L49: N47.image -> N46.source
    - L50: N12.mask -> N46.mask
    - L51: N12.image -> N47.image
    - L52: N17.image -> N51.target
    - L53: N47.image -> N51.source
    - L54: N51.image -> N52.images
    - L55: N61.model -> N58.model
    - L56: N46.image -> N58.image
    - L57: N12.mask -> N58.attn_mask
    - L58: N4.model -> N61.model
    - L59: N6.conditioning -> N62.positive
    - L60: N7.conditioning -> N62.negative
    - L61: N4.vae -> N62.vae
    - L62: N83.latent -> N62.foreground
    - L63: N46.image -> N82.pixels
    - L64: N4.vae -> N82.vae
    - L65: N12.image -> N83.pixels
    - L66: N4.vae -> N83.vae
