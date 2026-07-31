def create_svg(filename, title, subtitle):
    svg_content = f'''<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0a1a" />
      <stop offset="100%" stop-color="#1a0b2e" />
    </linearGradient>
    <linearGradient id="grid-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(0, 255, 255, 0)" />
      <stop offset="50%" stop-color="rgba(0, 255, 255, 0.2)" />
      <stop offset="100%" stop-color="rgba(255, 0, 255, 0.6)" />
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="url(#grid-grad)" stroke-width="1.5" />
    </pattern>
    <style>
      @keyframes moveGrid {{
        0% {{ transform: translateY(0); }}
        100% {{ transform: translateY(40px); }}
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 1; text-shadow: 0 0 10px #0ff, 0 0 20px #0ff; }}
        50% {{ opacity: 0.7; text-shadow: 0 0 5px #0ff, 0 0 10px #0ff; }}
      }}
      @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
      }}
      .grid-layer {{ animation: moveGrid 2s linear infinite; }}
      .text-glow {{
        font-family: 'Courier New', monospace;
        font-weight: bold;
        fill: #ffffff;
        animation: pulse 3s infinite;
      }}
      .sub-glow {{
        font-family: 'Courier New', monospace;
        fill: #ff00ff;
        font-size: 14px;
        letter-spacing: 4px;
      }}
    </style>
  </defs>
  
  <rect width="100%" height="100%" fill="url(#bg)" />
  
  <g class="grid-layer">
    <!-- Oversized rect to allow continuous scrolling without clipping -->
    <rect x="0" y="-40" width="800" height="280" fill="url(#grid)" />
  </g>
  
  <rect width="100%" height="100%" fill="url(#grid-grad)" style="mix-blend-mode: overlay;" />

  <g style="animation: float 4s ease-in-out infinite;">
    <text x="400" y="100" font-size="40" text-anchor="middle" class="text-glow">{title}</text>
    <text x="400" y="130" text-anchor="middle" class="sub-glow">{subtitle}</text>
  </g>
</svg>'''
    with open(filename, 'w') as f:
        f.write(svg_content)
    print(f"Generated {filename}")

create_svg('assets/banner-top.svg', 'NEO-TOKYO.exe', 'INITIALIZING PROTOCOLS...')
create_svg('assets/banner-bottom.svg', 'SYSTEM // SECURE', 'CONNECTION TERMINATED.')
