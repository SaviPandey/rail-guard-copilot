import os
import sys
import json
import math
import glob
import io
import requests
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips

VIDEO_W, VIDEO_H = 1080, 1920

# ── LOCALIZED SCRIPTS & CONFIGURATIONS ──────────────────────────────────────
LANG_CONFIGS = {
    "Hindi": {
        "lang_code": "hi",
        "title": "सुरक्षित रेल यात्रा नियम",
        "script": "नमस्ते! यात्रागार्ड में आपका स्वागत है। इस यात्रा में मैं आपका डिजिटल साथी हूँ। आपकी सुरक्षा के लिए कुछ ज़रूरी बातें: अपना फ़ोन चार्ज रखें, सफ़र में किसी अनजान व्यक्ति से खाने-पीने की चीज़ें न लें, और बिलकुल बेफ़िक्र रहें। हमारा सिस्टम हर मिनट आपकी ट्रेन पर नज़र रख रहा है, और स्टेशन आने से पहले हम आपको जगा देंगे। आपकी यात्रा मंगलमय हो!",
        "query": "indian railways train",
        "output": "videos/guidelines_hi.mp4"
    },
    "English": {
        "lang_code": "en",
        "title": "Rail Safety Guidelines",
        "script": "Hello! Welcome to YatraGuard. Think of me as your digital co-pilot for this journey. A few quick rules for your safety: Keep your phone charged, don't accept open food from strangers, and most importantly—relax. Our automated mesh is tracking your train every minute, and we will wake you up before your station arrives. Have a beautiful trip!",
        "query": "train passenger traveling",
        "output": "videos/guidelines_en.mp4"
    },
    "Marathi": {
        "lang_code": "mr",
        "title": "सुरक्षित रेल्वे प्रवास नियम",
        "script": "नमस्कार! यात्रागार्डमध्ये आपले स्वागत आहे. या प्रवासात मी तुमचा डिजिटल सोबती आहे. तुमच्या सुरक्षिततेसाठी काही महत्त्वाच्या गोष्टी: तुमचा फोन चार्ज ठेवा, प्रवासात अनोळखी व्यक्तींकडून खाण्यापिण्याच्या वस्तू घेऊ नका, आणि अजिबात काळजी करू नका. आमचे सिस्टीम दर मिनिटाला तुमच्या ट्रेनवर लक्ष ठेवून आहे, आणि स्टेशन येण्यापूर्वी आम्ही तुम्हाला जागे करू. तुमचा प्रवास सुखकर होवो!",
        "query": "indian train station",
        "output": "videos/guidelines_mr.mp4"
    }
}

# ── EXTRACT SYSTEM DEVANGARI / SYSTEM FONTS ─────────────────────────
def get_system_font():
    """Find a readable font path based on the operating system."""
    if sys.platform.startswith("win"):
        paths = [
            "C:\\Windows\\Fonts\\ Nirmala.ttf",
            "C:\\Windows\\Fonts\\arial.ttf"
        ]
        for p in paths:
            if os.path.exists(p): return p
    else:
        # Linux font fallback array
        for pattern in ["/usr/share/fonts/**/NotoSansDevanagari-Regular.ttf", "/usr/share/fonts/**/*.ttf"]:
            hits = glob.glob(pattern, recursive=True)
            if hits: return hits[0]
    return None

FONT_PATH = get_system_font()
print(f"[+] System typography routing complete. Target font: {FONT_PATH}")

# programmatically render text clips on image frames ─────────────
def text_to_imageclip(text, font_path, fontsize, color, max_width, duration, stroke_color=None, stroke_width=0):
    font = ImageFont.truetype(font_path, fontsize) if font_path else ImageFont.load_default()
    words, lines, current = text.split(), [], []
    
    for w in words:
        test = " ".join(current + [w])
        # Calculate text boundaries
        bbox = font.getbbox(test) if font_path else (0, 0, len(test)*10, fontsize)
        if bbox[2] > max_width and current:
            lines.append(" ".join(current))
            current = [w]
        else:
            current.append(w)
    if current:
        lines.append(" ".join(current))

    line_h = int(fontsize * 1.5)
    pad = stroke_width * 2 + 15
    img = Image.new("RGBA", (max_width, line_h * len(lines) + pad * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for i, line in enumerate(lines):
        line_w = font.getbbox(line)[2] if font_path else len(line)*10
        x = (max_width - line_w) // 2
        y = pad + i * line_h
        if stroke_color and stroke_width > 0:
            draw.text((x, y), line, font=font, fill=color, stroke_width=stroke_width, stroke_fill=stroke_color)
        else:
            draw.text((x, y), line, font=font, fill=color)

    return ImageClip(np.array(img), transparent=True).set_duration(duration)

# ── PEXELS IMAGE ENGINE ─────────────────────────────────────────────────────
def fetch_pexels_images(query, api_key, count=4):
    headers = {"Authorization": api_key}
    url = "https://api.pexels.com/v1/search"
    params = {"query": query, "per_page": count, "orientation": "portrait"}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=20)
        r.raise_for_status()
        return [photo["src"]["large2x"] for photo in r.json().get("photos", [])]
    except Exception as e:
        print(f"⚠️ Pexels query failed: {e}. Falling back to default backup images.")
        # Fallback to general premium public background queries if direct fails
        return []

def fit_to_canvas(img_url, target_w, target_h):
    res = requests.get(img_url, timeout=20)
    img = Image.open(io.BytesIO(res.content)).convert("RGB")
    sw, sh = img.size
    src_ratio, dst_ratio = sw / sh, target_w / target_h
    
    if src_ratio > dst_ratio:
        new_w = int(sh * dst_ratio)
        off = (sw - new_w) // 2
        img = img.crop((off, 0, off + new_w, sh))
    else:
        new_h = int(sw / dst_ratio)
        off = (sh - new_h) // 2
        img = img.crop((0, off, sw, off + new_h))
        
    return img.resize((target_w, target_h), Image.Resampling.LANCZOS)

def split_text(text, chunks_count):
    words = text.split()
    per_chunk = math.ceil(len(words) / chunks_count)
    return [" ".join(words[i:i + per_chunk]) for i in range(0, len(words), per_chunk)][:chunks_count]

def generate_pipeline(target_lang, pexels_key):
    cfg = LANG_CONFIGS[target_lang]
    Path("videos").mkdir(exist_ok=True)
    tmp_audio = f"videos/tmp_{cfg['lang_code']}.mp3"
    
    print(f"\n🚀 Starting pipeline execution for language: [{target_lang}]")
    
    # Step 1: Render Localized Audio Track via Google TTS
    print("[+] Rendering TTS voice synchronization track...")
    tts = gTTS(text=cfg['script'], lang=cfg['lang_code'], slow=False)
    tts.save(tmp_audio)
    
    audio = AudioFileClip(tmp_audio)
    total_duration = audio.duration
    print(f"[+] Sound track built seamlessly. Total duration: {total_duration:.2f}s")
    
    # Step 2: Grab Media Context from Pexels
    print(f"[+] Querying Pexels Media Matrix for: '{cfg['query']}'")
    urls = fetch_pexels_images(cfg['query'], pexels_key, count=4)
    if not urls:
        # Global backup fallback image pool if key is missing or expired
        urls = ["https://images.pexels.com/photos/2524368/pexels-photo-2524368.jpeg"]
        
    img_count = len(urls)
    slide_duration = total_duration / img_count
    chunks = split_text(cfg['script'], img_count)
    
    clips = []
    # Step 3: Stitch Video Layers Programmatically
    for i, url in enumerate(urls):
        print(f"  └─ Processing composition segment frame {i+1}/{img_count}")
        canvas_img = fit_to_canvas(url, VIDEO_W, VIDEO_H)
        
        # Save frame to numpy array for fast processing
        bg_clip = ImageClip(np.array(canvas_img)).set_duration(slide_duration)
        
        # Add localized text subtitle track overlay
        sub_clip = text_to_imageclip(
            chunks[i], font_path=FONT_PATH, fontsize=48, color="white",
            max_width=VIDEO_W - 140, duration=slide_duration,
            stroke_color="black", stroke_width=3
        ).set_position(("center", VIDEO_H - 450))
        
        layers = [bg_clip, sub_clip]
        
        # Add a premium stylized Header Title over the opening slide block
        if i == 0:
            title_clip = text_to_imageclip(
                cfg['title'], font_path=FONT_PATH, fontsize=72, color="#FF9933",
                max_width=VIDEO_W - 100, duration=min(4, slide_duration),
                stroke_color="black", stroke_width=4
            ).set_position(("center", 250))
            layers.append(title_clip)
            
        clips.append(CompositeVideoClip(layers, size=(VIDEO_W, VIDEO_H)))
        
    # Step 4: Concatenate Composition Elements & Compile Out MP4
    print("[+] Executing video compression codec matrix compilation...")
    final_video = concatenate_videoclips(clips, method="chain")
    final_video = final_video.set_audio(audio).set_duration(total_duration)
    
    final_video.write_videofile(
        cfg['output'], codec="libx264", audio_codec="aac", fps=24,
        preset="fast", threads=4, logger=None
    )
    
    if os.path.exists(tmp_audio):
        os.remove(tmp_audio)
    print(f"Video asset pipeline generation completed: {cfg['output']}")

if __name__ == "__main__":
    PEXELS_KEY = os.environ.get("PEXELS_API_KEY", "YOUR_PEXELS_KEY_HERE")
    
    if PEXELS_KEY == "YOUR_PEXELS_KEY_HERE":
        print("Error: Please provide a valid PEXELS_API_KEY environment variable.")
        sys.exit(1)
        
    # Generate the Hindi core guide file immediately
    generate_pipeline("Hindi", PEXELS_KEY)
