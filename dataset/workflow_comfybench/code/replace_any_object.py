# create nodes by instantiation
loadimage_33 = LoadImage(image="""cat_stand.jpg""")
vaeencodeforinpaint_38 = VAEEncodeForInpaint(grow_mask_by=0)
cliptextencode_59 = CLIPTextEncode(text="""text, watermark""")
cliptextencode_60 = CLIPTextEncode(text="""a dog""")
groundingdinosamsegmentSpaceLeftParensegmentSpaceanythingRightParen_101 = GroundingDinoSAMSegmentSpaceLeftParensegmentSpaceanythingRightParen(prompt="""cat""", threshold=0.2)
groundingdinomodelloaderSpaceLeftParensegmentSpaceanythingRightParen_102 = GroundingDinoModelLoaderSpaceLeftParensegmentSpaceanythingRightParen(model_name="""GroundingDINO_SwinT_OGC (694MB)""")
sammodelloaderSpaceLeftParensegmentSpaceanythingRightParen_103 = SAMModelLoaderSpaceLeftParensegmentSpaceanythingRightParen(model_name="""sam_vit_l (1.25GB)""")
ksampleradvanced_105 = KSamplerAdvanced(add_noise="""enable""", noise_seed=858603438157931, control_after_generate="""randomize""", steps=20, cfg=8, sampler_name="""dpmpp_2m""", scheduler="""normal""", start_at_step=0, end_at_step=10000, return_with_leftover_noise="""disable""")
vaedecode_106 = VAEDecode()
ksampleradvanced_109 = KSamplerAdvanced(add_noise="""enable""", noise_seed=576713408461301, control_after_generate="""randomize""", steps=20, cfg=8, sampler_name="""dpmpp_2m""", scheduler="""normal""", start_at_step=0, end_at_step=10000, return_with_leftover_noise="""disable""")
checkpointloadersimple_112 = CheckpointLoaderSimple(ckpt_name="""dreamshaper_8Inpainting.safetensors""")
growmask_113 = GrowMask(expand=45, tapered_corners=True)
saveimage_115 = SaveImage(filename_prefix="""ComfyUI""")

# link nodes by invocation
image_33, mask_33 = loadimage_33()
grounding_dino_model_102 = groundingdinomodelloaderSpaceLeftParensegmentSpaceanythingRightParen_102()
model_112, clip_112, vae_112 = checkpointloadersimple_112()
conditioning_59 = cliptextencode_59(clip=clip_112)
sam_model_103 = sammodelloaderSpaceLeftParensegmentSpaceanythingRightParen_103()
conditioning_60 = cliptextencode_60(clip=clip_112)
image_101, mask_101 = groundingdinosamsegmentSpaceLeftParensegmentSpaceanythingRightParen_101(sam_model=sam_model_103, grounding_dino_model=grounding_dino_model_102, image=image_33)
mask_113 = growmask_113(mask=mask_101)
latent_38 = vaeencodeforinpaint_38(pixels=image_33, vae=vae_112, mask=mask_113)
latent_105 = ksampleradvanced_105(model=model_112, positive=conditioning_60, negative=conditioning_59, latent_image=latent_38)
latent_109 = ksampleradvanced_109(model=model_112, positive=conditioning_60, negative=conditioning_59, latent_image=latent_105)
image_106 = vaedecode_106(samples=latent_109, vae=vae_112)
result_115 = saveimage_115(images=image_106)
