# create nodes by instantiation
clipvisionencode_13 = CLIPVisionEncode()
emptylatentimage_5 = EmptyLatentImage(width=768, height=768, batch_size=1)
unclipcheckpointloader_32 = unCLIPCheckpointLoader(ckpt_name="""sd21-unclip-h.ckpt""")
clipvisionencode_36 = CLIPVisionEncode()
ksampler_3 = KSampler(seed=947446491266673, control_after_generate="""randomize""", steps=26, cfg=8, sampler_name="""uni_pc_bh2""", scheduler="""normal""", denoise=1)
cliptextencode_6 = CLIPTextEncode(text="""beautiful photograph""")
cliptextencode_7 = CLIPTextEncode(text="""bad hands""")
unclipconditioning_19 = unCLIPConditioning(strength=0.5, noise_augmentation=0.4000000000000002)
unclipconditioning_37 = unCLIPConditioning(strength=0.5, noise_augmentation=0.4000000000000002)