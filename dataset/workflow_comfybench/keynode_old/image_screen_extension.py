# create nodes by instantiation
checkpointloadersimple_4 = CheckpointLoaderSimple(ckpt_name="""dreamshaper_8.safetensors""")
cliptextencode_6 = CLIPTextEncode(text="""an image of iceberg""")
cliptextencode_7 = CLIPTextEncode(text="""illustration, painting, text, watermark, copyright, signature, notes""")
imagepadforoutpaint_11 = ImagePadForOutpaint(left=256, top=0, right=256, bottom=0, feathering=0)
vaeencodeforinpaint_12 = VAEEncodeForInpaint(grow_mask_by=16)
ksampler_21 = KSampler(seed=1, control_after_generate="""randomize""", steps=20, cfg=7, sampler_name="""dpmpp_2m""", scheduler="""karras""", denoise=1)
vaedecode_23 = VAEDecode()
checkpointloadersimple_25 = CheckpointLoaderSimple(ckpt_name="""dreamshaper_8Inpainting.safetensors""")
vaeloader_70 = VAELoader(vae_name="""vae-ft-mse-840000-ema-pruned.safetensors""")
loadimage_78 = LoadImage(image="""iceberg.jpg""")
saveimage_79 = SaveImage(filename_prefix="""ComfyUI""")
