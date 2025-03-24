# create nodes by instantiation
checkpointloadersimple_4 = CheckpointLoaderSimple(ckpt_name="""dreamshaper_8.safetensors""")
emptylatentimage_5 = EmptyLatentImage(width=512, height=512, batch_size=1)
cliptextencode_6 = CLIPTextEncode(text="""a bird, open wings,""")
cliptextencode_7 = CLIPTextEncode(text="""horror,lowres, zombie,""")
vaedecode_8 = VAEDecode()
saveimage_9 = SaveImage(filename_prefix="""Comfy""")
ksampler_17 = KSampler(seed=797967395221167, control_after_generate="""randomize""", steps=27, cfg=4, sampler_name="""dpmpp_2m_sde""", scheduler="""karras""", denoise=1)
controlnetapply_26 = ControlNetApply(strength=0.8)
controlnetloader_27 = ControlNetLoader(control_net_name="""control_v11p_sd15_scribble_fp16.safetensors""")
loadimage_28 = LoadImage(image="""simple_graffiti.png""")
getimagesizePLUS_31 = GetImageSizePLUS()
imageinvert_32 = ImageInvert()

# link nodes by invocation
model_4, clip_4, vae_4 = checkpointloadersimple_4()
conditioning_6 = cliptextencode_6(clip=clip_4)
control_net_27 = controlnetloader_27()
conditioning_7 = cliptextencode_7(clip=clip_4)
image_28, mask_28 = loadimage_28()
image_32 = imageinvert_32(image=image_28)
conditioning_26 = controlnetapply_26(conditioning=conditioning_6, control_net=control_net_27, image=image_32)
width_31, height_31, count_31 = getimagesizePLUS_31(image=image_28)
latent_5 = emptylatentimage_5(height=height_31, width=width_31)
latent_17 = ksampler_17(model=model_4, positive=conditioning_26, negative=conditioning_7, latent_image=latent_5)
image_8 = vaedecode_8(samples=latent_17, vae=vae_4)
result_9 = saveimage_9(images=image_8)
