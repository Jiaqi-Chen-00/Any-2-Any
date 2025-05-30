- Nodes:
    - N4:
        - node_type: "CheckpointLoaderSimple"
        - ckpt_name: "majicmixRealistic_v7.safetensors"
    - N11:
        - node_type: "CLIPSetLastLayer"
        - stop_at_clip_layer: -2
    - N12:
        - node_type: "LoraLoader"
        - lora_name: "more_details.safetensors"
        - strength_model: 0.8
        - strength_clip: 0.8
    - N13:
        - node_type: "BNK_CLIPTextEncodeAdvanced"
        - token_normalization: "realistic,1girl,solo,upper body,black hair,red lips,sleeveless,looking at viewer,leaf,plant,green theme"
        - weight_interpretation: "none"
    - N14:
        - node_type: "BNK_CLIPTextEncodeAdvanced"
        - token_normalization: "badhandv4,EasyNegative,ng_deepnegative_v1_75t,(badhandv4:1.2),(worst quality:2),(low quality:2),(normal quality:2),lowres,bad anatomy,bad hands,watermark,moles,nsfw,"
        - weight_interpretation: "none"
    - N17:
        - node_type: "EmptyLatentImage"
        - width: 512
        - height: 768
        - batch_size: 1
    - N18:
        - node_type: "VAEDecode"
    - N19:
        - node_type: "VAELoader"
        - vae_name: "vae-ft-mse-840000-ema-pruned.safetensors"
    - N20:
        - node_type: "DWPreprocessor"
        - detect_hand: "enable"
        - detect_body: "enable"
        - detect_face: "enable"
        - resolution: 512
        - bbox_detector: "yolox_l.onnx"
        - pose_estimator: "dw-ll_ucoco_384_bs5.torchscript.pt"
    - N23:
        - node_type: "LoadImage"
        - image: "woman_portrait.jpg"
    - N24:
        - node_type: "ControlNetApplyAdvanced"
        - strength: 0.9
        - start_percent: 0
        - end_percent: 1
    - N25:
        - node_type: "DiffControlNetLoader"
        - control_net_name: "control_v11p_sd15_openpose_fp16.safetensors"
    - N27:
        - node_type: "MiDaS-DepthMapPreprocessor"
        - a: 6.28
        - bg_threshold: 0.1
        - resolution: 512
    - N28:
        - node_type: "ControlNetApplyAdvanced"
        - strength: 1
        - start_percent: 0
        - end_percent: 1
    - N29:
        - node_type: "DiffControlNetLoader"
        - control_net_name: "control_v11f1p_sd15_depth_fp16.safetensors"
    - N53:
        - node_type: "ReActorFaceSwap"
        - enabled: True
        - swap_model: "inswapper_128.onnx"
        - facedetection: "YOLOv5l"
        - face_restore_model: "codeformer-v0.1.0.pth"
        - face_restore_visibility: 1
        - codeformer_weight: 0.5
        - detect_gender_input: "no"
        - detect_gender_source: "no"
        - input_faces_index: "0"
        - source_faces_index: "0"
        - console_log_level: 1
    - N62:
        - node_type: "KSampler"
        - seed: 1093069514427779
        - control_after_generate: "randomize"
        - steps: 30
        - cfg: 7
        - sampler_name: "dpmpp_2m"
        - scheduler: "karras"
        - denoise: 1
    - N63:
        - node_type: "SaveImage"
        - filename_prefix: "ComfyUI"

- Links:
    - L27: N12.clip -> N11.clip
    - L28: N4.model -> N12.model
    - L29: N4.clip -> N12.clip
    - L30: N11.clip -> N13.clip
    - L31: N11.clip -> N14.clip
    - L32: N62.latent -> N18.samples
    - L33: N19.vae -> N18.vae
    - L34: N23.image -> N20.image
    - L35: N13.conditioning -> N24.positive
    - L36: N14.conditioning -> N24.negative
    - L37: N25.control_net -> N24.control_net
    - L38: N20.image -> N24.image
    - L39: N4.model -> N25.model
    - L40: N23.image -> N27.image
    - L41: N24.positive -> N28.positive
    - L42: N24.negative -> N28.negative
    - L43: N29.control_net -> N28.control_net
    - L44: N27.image -> N28.image
    - L45: N4.model -> N29.model
    - L46: N18.image -> N53.input_image
    - L47: N23.image -> N53.source_image
    - L48: N12.model -> N62.model
    - L49: N28.positive -> N62.positive
    - L50: N28.negative -> N62.negative
    - L51: N17.latent -> N62.latent_image
    - L52: N53.image -> N63.images
