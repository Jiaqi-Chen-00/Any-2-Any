# create nodes by instantiation
ksampler_3 = KSampler(seed=249584040731174, control_after_generate="""randomize""", steps=20, cfg=7, sampler_name="""dpmpp_2m""", scheduler="""karras""", denoise=1)
checkpointloadersimple_4 = CheckpointLoaderSimple(ckpt_name="""dreamshaper_8.safetensors""")
emptylatentimage_5 = EmptyLatentImage(width=512, height=512, batch_size=1)
cliptextencode_6 = CLIPTextEncode(text="""a male, dancing in the street""")
cliptextencode_7 = CLIPTextEncode(text="""blurry, painting, drawing, photography, distorted, horror""")
vaedecode_8 = VAEDecode()
saveimage_9 = SaveImage(filename_prefix="""Result""")
vaeloader_11 = VAELoader(vae_name="""vae-ft-mse-840000-ema-pruned.safetensors""")
loadimage_12 = LoadImage(image="""woman_dance.jpg""")
controlnetloader_14 = ControlNetLoader(control_net_name="""control_v11p_sd15_openpose_fp16.safetensors""")
controlnetapply_16 = ControlNetApply(strength=0.9)
previewimage_17 = PreviewImage()
imagescale_24 = ImageScale(upscale_method="""nearest-exact""", width=512, height=512, crop="""disabled""")
dwpreprocessor_28 = DWPreprocessor(detect_hand="""disable""", detect_body="""enable""", detect_face="""disable""", resolution=512, bbox_detector="""yolox_l.onnx""", pose_estimator="""dw-ll_ucoco_384_bs5.torchscript.pt""")

# link nodes by invocation
model_4, clip_4, vae_4 = checkpointloadersimple_4()
conditioning_6 = cliptextencode_6(clip=clip_4)
vae_11 = vaeloader_11()
control_net_14 = controlnetloader_14()
latent_5 = emptylatentimage_5()
image_12, mask_12 = loadimage_12()
image_28, pose_keypoint_28 = dwpreprocessor_28(image=image_12)
conditioning_7 = cliptextencode_7(clip=clip_4)
result_17 = previewimage_17(images=image_28)
image_24 = imagescale_24(image=image_28)
conditioning_16 = controlnetapply_16(conditioning=conditioning_6, control_net=control_net_14, image=image_24)
latent_3 = ksampler_3(model=model_4, positive=conditioning_16, negative=conditioning_7, latent_image=latent_5)
image_8 = vaedecode_8(samples=latent_3, vae=vae_11)
result_9 = saveimage_9(images=image_8)
