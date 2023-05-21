import torch
import os
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
# from shap_e.util.notebooks import create_pan_cameras, decode_latent_images, gif_widget

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
xm = load_model('transmitter', device=device)
model = load_model('text300M', device=device)
diffusion = diffusion_from_config(load_config('diffusion'))

batch_size = 4
guidance_scale = 15.0
username = input("Please enter your username:")
prompt = input("Please provide descriptions of the furniture you want to design:\n")

latents = sample_latents(
    batch_size=batch_size,
    model=model,
    diffusion=diffusion,
    guidance_scale=guidance_scale,
    model_kwargs=dict(texts=[prompt] * batch_size),
    progress=True,
    clip_denoised=True,
    use_fp16=True,
    use_karras=True,
    karras_steps=64,
    sigma_min=1e-3,
    sigma_max=160,
    s_churn=0,
)

render_mode = 'nerf' # you can change this to 'stf'
size = 64 # this is the size of the renders; higher values take longer to render.

# Example of saving the latents as meshes.
from shap_e.util.notebooks import decode_latent_mesh

os.mkdir(username)
for i, latent in enumerate(latents):
    t = decode_latent_mesh(xm, latent).tri_mesh()
    joined_path_ply = os.path.join(username, f'example_mesh_{i}.ply')
    with open(joined_path_ply, 'wb') as f:
        t.write_ply(f)
