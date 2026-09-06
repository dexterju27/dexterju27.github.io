"""Responsive derivatives of the existing photo; original stays untouched."""
from pathlib import Path
from PIL import Image,ImageOps
ROOT=Path(__file__).resolve().parents[1]
source=ImageOps.exif_transpose(Image.open(ROOT/'profil-photo.jpg')).convert('RGB')
out=ROOT/'assets/images';out.mkdir(parents=True,exist_ok=True)
for width in (480,960):
    portrait=ImageOps.fit(source,(width,int(width*1.25)),method=Image.Resampling.LANCZOS,centering=(.53,.45))
    portrait.save(out/('dexter-portrait-%s.webp'%width),'WEBP',quality=86,method=6)
    if width==960:portrait.save(out/'dexter-portrait.jpg','JPEG',quality=86,optimize=True,progressive=True)
for file in out.iterdir():print(file.name,file.stat().st_size)
